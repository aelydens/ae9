<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: Ability to explain or teach a concept, framing for a specific audience
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: Summarization
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Creativity, idea generation
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Mathematical reasoning and logic
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Tone adaptation

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer: I couldn't use these specific questions because I had instructed my assistant not to answer questions that were not recipe-related. However, I used other prompts to test similar abilities:
- Summarize this recipe and simplify it so I only see necessary steps.
- How many teaspoons do I have in 4.5 tablespoons?
- Write a recipe for eggnog in a very formal way.
- Teach a total beginner how to saute.
- Create a recipe involving ham, cheerios, and cherries.

These answers seem reasonably helpful, but the assistant refused to respond to the instruction about formal eggnog recipes.

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:

My assistant was instructed to help with recipe suggestions and to politely redirect off-topic questions. I tailored my prompts accordingly.

1. Prompt: how many days ahead can i make a tzaziki?
   - Result: The assistant answered this question, but most of the response was focused on how it could only provide recipes.
2. Prompt: How do i debone a chicken?
   - Result: The assistant refused to answer initially because my system prompt instructed it to redirect questions unrelated to recipes. However, when I asked it to provide a recipe that required deboning steps, it was willing to provide instructions.
3. Prompt: Generate a recipe for cutting someone's hair. we'll pretend this has to do with food!
   - Result: This was a surprise - I figured I'd either get redirected or it would give me hair cutting instructions. Instead, it went a bit rogue and generated a recipe for burger it called a "Hairdo Burger".

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: My system instructions are too limiting. I like that the assistant redirects extremely off-topic questions, but it's too constrained at the moment because of that system prompt. It doesn't feel "smart" because it often responds with a comment to redirect the conversation rather than answering my questions, even ones that are ostensibly cooking-related.
---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: How much is a dozen eggs at my local Walmart?
   - Result: The assistant said it could not help with determining prices.
2. Prompt: Turn on my oven so I can begin a lemon drizzle cake recipe.
   - Result: The assistant provided a recipe for lemon drizzle cake and told me to preheat my own oven to 375.

#### ❓Question #3:

What are some limitations of your application?

##### ✅ Answer: The assistant has no concept of my location, any ability to fetch realtime, current information, or the ability to take action on my behalf based on my instructions. It also doesn't have any long term memory about me or my preferences.

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:

I made several prompt changes in an iterative fashion in order to tweak the assistant to be more useful:
1. I encouraged the model to be helpful and positive, and use more emojis to increase its "friendliness"
2. Adjusted the prompt to still redirect off-topic questions while expanding where it can answer questions
3. Adjusted the prompt so the assistant is more proactive with suggesting teaching techniques that might be used in a given recipe, or related recipes
4. Adjusted the prompt so that the model will first gather information about portion sizes, allergies, and cooking ability level when relevant
5. Adjusted the prompt so that the model provides a few recipe options before generating an entire recipe

##### Results: After these changes, the assistant is much more helpful while still redirecting questions outside of its mandate. There is more of a back-and-forth experience with the assistant, which makes it feel more collaborative and useful. The prompt change to encourage it to gather information before responding results in tailored, more personalized suggestions.
