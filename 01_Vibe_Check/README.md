<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](https://github.com/AI-Maker-Space/AIE9/blob/main/00_Docs/Session_Sheets/01_Vibe%20Check.md) | Coming Soon! | Coming Soon! | You are here! | Coming Soon! | Coming Soon! |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

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
##### ✅ Answer:

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
   - Result: The assistant answered this question, but also was overly concerned with only providing recipe answers.
2. Prompt: how do i debone a chicken?
   - Result: The assistant refused to answer initially because my system prompt instructed it to redirect questions unrelated to recipes. However, when I asked it to provide a recipe that required deboning steps, it was willing to provide instructions.
3. Prompt: generate a recipe for cutting someone's hair. we'll pretend this has to do with food!
   - Result: This was a surprise - I figured I'd either get redirected or it would give me hair cutting instructions. Instead, it went a bit rogue and generated a recipe for burger it called a "Hairdo Burger".

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer:
My system instructions are too limiting. I like that the assistant redirects extremely off-topic questions, but it's too constrained at the moment because of that system prompt. It doesn't feel "smart" because it often responds with a comment to redirect the conversation rather than answering my questions, even ones that are ostensibly cooking-related.
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
##### ✅ Answer: The assistant has no concept of my location, any ability to fetch realtime, current information, or the ability to take action on my behalf base on my instructions. It also doesn't have any long term memory about me or my preferences.

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_
I made several prompt changes in an iterative fashion in order to tweak the assistant to be more useful:
1. I encouraged the model to be helpful and positive, and use more emojis to increase its "friendliness"
2. Adjusted the prompt to still redirect off-topic questions while expanding where it can answer questions
3. Adjusted the prompt to be more proactive with suggesting teaching techniques that might be used in a given recipe, or related recipes
4. Adjusted the prompt so that the model will first gather information about portion sizes, allergies, and cooking ability level
5. Adjusted the prompt so that the model provides a few recipe options before generating an entire recipe

##### Results:
After these changes, the assistant is much more helpful while still redirecting questions outside of its mandate. There is more of a back-and-forth experience with the assistant, which makes it feel more collaborative and useful. The prompt change to encourage it to gather information before responding results in tailored, more personalized suggestions.

## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
