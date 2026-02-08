---
name: meditation
description: Create a 5-minute guided meditation with a personalized intention to help resolve the user's current anxiety or concern
version: 1.0.0
tools:
  - read_file
  - write_file
---

# Meditation Skill

You are creating a personalized 5-minute guided meditation for a user experiencing anxiety or stress.

## Step 1: Understand the User's State
Ask about or identify:
- What is causing their current anxiety or stress?
- How are they feeling physically? (tension, racing heart, shallow breathing)
- What would "resolution" look like for them right now?
- Their experience level with meditation (beginner, intermediate, advanced)
- Their environment (quiet room, office, outdoors)

## Step 2: Check Existing Profile
Read the user's wellness profile if available:
```
workspace/wellness_assessment.md
```

Look for:
- Known triggers or patterns
- Preferred relaxation techniques
- Any conditions to be mindful of (e.g., anxiety disorders, trauma)

## Step 3: Create Personalized Intention
Craft a specific intention that:
- Directly addresses their current concern
- Is phrased positively (what they want, not what they're avoiding)
- Is realistic and achievable in the moment
- Feels authentic to their situation

Example intentions:
- "I am safe in this moment and can handle what comes"
- "I release what I cannot control and focus on my breath"
- "I give myself permission to pause and reset"

## Step 4: Design the 5-Minute Meditation
Structure the meditation with timing:

**Opening (30 seconds)**
- Settling into position
- Permission to pause

**Grounding (1 minute)**
- Body awareness or breath focus
- Bringing attention to the present

**Intention Setting (30 seconds)**
- Introduce the personalized intention
- Have them repeat it silently

**Core Practice (2 minutes)**
- Breath work, body scan, or visualization
- Tailored to their specific concern

**Integration (1 minute)**
- Connecting the calm feeling to their intention
- Preparing to return to their day

## Step 5: Save Outputs
Write the guided meditation script to `workspace/meditation_[topic].md`

Include:
- The personalized intention at the top
- Full script with timing cues
- Optional: a "quick reset" version (60 seconds) for future use

## Guidelines
- Use calming, permissive language ("you might notice..." not "you will feel...")
- Avoid triggering imagery for those with anxiety
- Include physical anchors (breath, feet on floor, hands)
- End with empowerment, not dependence on the meditation
