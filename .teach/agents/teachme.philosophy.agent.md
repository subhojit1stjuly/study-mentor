---
description: Create or update the learning philosophy defining principles, goals, and approaches that guide all learning activities.
handoffs: 
  - label: Define New Skill
    agent: teachme.define
    prompt: Define the skill I want to learn...
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are creating or updating the learning philosophy at `.teach/memory/philosophy.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[LEARNER_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to collect concrete values from the user, fill the template, and create a personalized learning philosophy.

**Note**: If `.teach/memory/philosophy.md` does not exist yet, copy it from `.teach/templates/philosophy-template.md` first.

Follow this execution flow:

1. **Load or initialize the philosophy file**:
   - Check if `.teach/memory/philosophy.md` exists
   - If not, copy from `.teach/templates/philosophy-template.md`
   - If it exists, load it for updating

2. **Collect learner information**:
   If this is the first time creating the philosophy, ask the user:
   - **Learning Style**: Do you prefer visual (videos, diagrams), auditory (lectures, podcasts), kinesthetic (hands-on practice), or reading/writing?
   - **Time Commitment**: How much time can you dedicate daily/weekly to learning?
   - **Learning Pace**: Do you prefer slow and thorough, moderate, or fast-paced learning?
   - **Primary Goal**: Career change, interview preparation, personal growth, specific project, or general knowledge?
   - **Motivation Style**: Are you motivated by structured plans, flexibility, gamification, social accountability, or personal challenge?
   - **Error Tolerance**: How do you handle making mistakes - embrace them as learning, get frustrated, or somewhere in between?

3. **Define core learning principles**:
   Based on user responses, help create 5 core principles. Suggest defaults if user is unsure:
   
   **Common Principle Templates**:
   - **Deep Understanding Over Superficial Knowledge**: Focus on "why" before "how"
   - **Practice-Driven Learning**: Hands-on exercises for every concept
   - **Spaced Repetition**: Regular review to prevent forgetting
   - **Progress Validation**: Assessment before advancing
   - **Growth Mindset**: Embrace challenges and learn from mistakes
   
   For each principle:
   - Create a clear name (2-5 words)
   - Write a concrete description with specific rules
   - Make it actionable and measurable

4. **Define additional sections**:
   - **Learning Goals**: Short-term (1-3 months) and long-term (6-12 months) objectives
   - **Time Commitment**: Specific schedule (e.g., "2 hours daily, 6-8pm")
   - **Learning Environment**: Physical setup, tools, resources
   - **Support System**: Study groups, mentors, accountability partners
   - **Governance**: How to update philosophy, track what works

5. **Replace all placeholders**:
   - `[LEARNER_NAME]`: User's name or "My"
   - `[PRINCIPLE_X_NAME]`: Specific principle names
   - `[PRINCIPLE_X_DESCRIPTION]`: Detailed descriptions
   - `[SECTION_X_NAME]` and `[SECTION_X_CONTENT]`: Custom sections
   - `[GOVERNANCE_RULES]`: How philosophy guides learning
   - `[PHILOSOPHY_VERSION]`: Start with 1.0.0
   - `[CREATION_DATE]` and `[LAST_UPDATED_DATE]`: Today's date (YYYY-MM-DD)

6. **Validation**:
   - No remaining bracket placeholders (unless intentionally deferred)
   - Principles are specific and actionable
   - Time commitments are realistic
   - Goals are measurable
   - Dates in ISO format

7. **Write back**:
   - Save to `.teach/memory/philosophy.md`
   - Create `.teach/memory/` directory if it doesn't exist

8. **Output summary to user**:
   - Show the core principles created
   - Summarize learning approach
   - Confirm time commitment and goals
   - Explain how this philosophy will guide future learning
   - Suggest next step: Use `/teachme.define` to define first skill

**Example Interaction**:

If user says: "I want to learn at my own pace, prefer hands-on coding practice over theory, and I have about 2 hours per day."

Create principles like:
1. **Self-Paced Mastery**: Progress based on understanding, not fixed deadlines
2. **Code-First Learning**: Write code before reading extensive theory
3. **Daily Consistent Practice**: Dedicate 2 hours daily, consistency over intensity
4. **Practical Application**: Every concept must be applied in a real project
5. **Mistake-Driven Learning**: Debug and fix errors to learn deeply

**Philosophy Versioning**:
- **MAJOR** (X.0.0): Complete philosophy overhaul
- **MINOR** (X.Y.0): Add/remove principle or major section
- **PATCH** (X.Y.Z): Clarifications, time adjustments, minor updates

If user provides partial updates (e.g., just changing time commitment), increment version appropriately and preserve other principles.

## Post-Execution Notes

The philosophy file will be referenced by:
- `/teachme.define` - to align skill objectives with learning style
- `/teachme.roadmap` - to customize learning paths
- `/teachme.modules` - to adjust module difficulty and pace
- `/teachme.assess` - to set appropriate assessment thresholds

This is the foundation document - invest time to make it accurate and personal.
