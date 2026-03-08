"""An agent graph with a completeness evaluation loop and bullet-point summarizer.

After the agent responds, a secondary node evaluates if the response has enough
substance to summarize. If complete, generates bullet points; otherwise loops back
to the agent for more information. Terminates after a safe message limit.
"""
from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage

from app.state import MessagesState
from app.models import get_chat_model
from app.tools import get_tool_belt


class CompletenessResult(BaseModel):
    is_complete: bool = Field(description="Whether the response has enough substance to summarize")


class BulletSummary(BaseModel):
    bullets: List[str] = Field(description="List of key takeaways as bullet points")


def _build_model_with_tools():
    """Return a chat model instance bound to the current tool belt."""
    model = get_chat_model()
    return model.bind_tools(get_tool_belt())


def call_model(state: MessagesState) -> dict:
    """Invoke the model with the accumulated messages and append its response."""
    model = _build_model_with_tools()
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}


def route_to_action_or_completeness(state: MessagesState):
    """Decide whether to execute tools or run the completeness evaluator."""
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "action"
    return "completeness"


_completeness_prompt = ChatPromptTemplate.from_template(
    "Given an initial query and a final response, determine if the response "
    "has enough substance to generate a meaningful summary.\n\n"
    "Initial Query:\n{initial_query}\n\n"
    "Final Response:\n{final_response}\n\n"
    "A response is complete if it provides concrete information, answers, or actionable details. "
    "A response is NOT complete if it's vague, says 'I don't know', or needs more context."
)


def completeness_node(state: MessagesState) -> dict:
    """Evaluate if the response has enough substance to summarize."""
    if len(state["messages"]) > 10:
        return {"messages": [AIMessage(content="COMPLETENESS:END")]}

    initial_query = state["messages"][0]
    final_response = state["messages"][-1]

    structured_model = get_chat_model(model_name="gpt-4.1-mini").with_structured_output(CompletenessResult)
    result = (_completeness_prompt | structured_model).invoke(
        {
            "initial_query": initial_query.content,
            "final_response": final_response.content,
        }
    )

    decision = "Y" if result.is_complete else "N"
    return {"messages": [AIMessage(content=f"COMPLETENESS:{decision}")]}


def completeness_decision(state: MessagesState):
    """Route to summarize on 'COMPLETENESS:Y', loop back on 'N', or end on safety limit."""
    if any(getattr(m, "content", "") == "COMPLETENESS:END" for m in state["messages"][-1:]):
        return END

    last = state["messages"][-1]
    text = getattr(last, "content", "")
    if "COMPLETENESS:Y" in text:
        return "summarize"
    return "continue"


_bullet_prompt = ChatPromptTemplate.from_template(
    "Review the following conversation and extract the key takeaways as a concise bullet-point list.\n\n"
    "Conversation:\n{conversation}\n\n"
    "Generate 3-5 bullet points summarizing the most important information."
)


def bullet_pointer_node(state: MessagesState) -> dict:
    """Generate a bullet-point summary of the conversation."""
    conversation_text = "\n".join(
        f"{getattr(m, 'type', 'unknown').upper()}: {getattr(m, 'content', '')}"
        for m in state["messages"]
        if getattr(m, "content", "")
    )

    structured_model = get_chat_model(model_name="gpt-4.1-mini").with_structured_output(BulletSummary)
    result = (_bullet_prompt | structured_model).invoke({"conversation": conversation_text})

    bullet_text = "\n".join(f"• {bullet}" for bullet in result.bullets)
    summary_message = f"**Key Takeaways:**\n{bullet_text}"
    
    return {"messages": [AIMessage(content=summary_message)]}


def build_graph():
    """Build an agent graph with completeness evaluation and bullet-point summarizer."""
    graph = StateGraph(MessagesState)
    tool_node = ToolNode(get_tool_belt())
    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)
    graph.add_node("completeness", completeness_node)
    graph.add_node("summarize", bullet_pointer_node)
    graph.add_edge(START, "agent")
    graph.add_conditional_edges(
        "agent",
        route_to_action_or_completeness,
        {"action": "action", "completeness": "completeness"},
    )
    graph.add_conditional_edges(
        "completeness",
        completeness_decision,
        {"continue": "agent", "summarize": "summarize", END: END},
    )
    graph.add_edge("summarize", END)
    graph.add_edge("action", "agent")
    return graph


graph = build_graph().compile()
