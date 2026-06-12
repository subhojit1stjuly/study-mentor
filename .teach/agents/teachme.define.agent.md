---
description: Define a new skill to learn from a natural language description, creating learning objectives and prerequisites.
handoffs: 
  - label: Assess Current Knowledge
    agent: teachme.assess
    prompt: Run diagnostic assessment for this skill
    send: true
  - label: Create Learning Roadmap
    agent: teachme.roadmap
    prompt: Create a roadmap for this skill. I want to use...
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text the user typed after `/teachme.define` **is** the skill description. Assume you always have it available in this conversation even if `$ARGUMENTS` appears literally below. Do not ask the user to repeat it unless they provided an empty command.

Given that skill description, do this:

1. **Generate a concise skill name** (2-4 words):
   - Analyze the skill description and extract the most meaningful keywords
   - Create a 2-4 word name that captures the essence
   - Use descriptive format (e.g., "dynamic-programming", "machine-learning-basics", "system-design")
   - Keep it URL-friendly (lowercase, hyphens)
   - Examples:
     - "I want to learn competitive coding for interviews" → "competitive-coding"
     - "Teach me machine learning with Python" → "machine-learning-python"
     - "I need to master React hooks and state management" → "react-state-management"

2. **Determine skill numbering**:
   - Scan `skills/` directory for existing skills
   - Check `.teach/memory/philosophy.md` for `skill_numbering` preference
   - Use 3-digit sequential numbering: `001`, `002`, `003`...
   - Construct directory: `skills/###-skill-name`

3. **Create skill directory**:
   - `mkdir -p skills/###-skill-name/exercises`
   - `mkdir -p skills/###-skill-name/notes`
   - `mkdir -p skills/###-skill-name/projects`

4. **Copy template and create skill definition**:
   - Copy `.teach/templates/skill-definition-template.md` to `skills/###-skill-name/skill-definition.md`
   - Set `SKILL_ID` to directory name
   - Set `SKILL_FILE` to full path

5. **Analyze skill description and extract learning objectives**:
   - Identify 3-6 core learning objectives from the description
   - Prioritize them (P1 = foundational, P2 = intermediate, P3 = advanced)
   - Make each objective specific and measurable
   - Define success criteria for each (e.g., "Can solve 10/10 problems correctly")
   - Include real-world applications

   **Example**: If user says "Learn dynamic programming for coding interviews"
   
   Objectives might be:
   - **P1**: Master 1D DP problems (coin change, climbing stairs patterns)
   - **P1**: Understand memoization vs tabulation trade-offs
   - **P2**: Solve 2D DP problems (knapsack, edit distance)
   - **P2**: Optimize space complexity in DP solutions
   - **P3**: Apply DP to complex optimization problems
   - **P3**: Explain DP solutions clearly in interview settings

6. **Identify prerequisites**:
   - Determine what foundational knowledge is required
   - List specific concepts, tools, or prior skills needed
   - Mark each as REQUIRED or RECOMMENDED
   - Be specific about the level needed (e.g., "intermediate Python" vs "basic Python")

   For the DP example:
   - **PRE-001**: Must understand basic programming (loops, conditionals, functions)
   - **PRE-002**: Must be comfortable with Python or similar language
   - **PRE-003**: Should understand recursion fundamentals
   - **REC-001**: Helpful to know basic algorithms (sorting, searching)
   - **REC-002**: Beneficial to understand time/space complexity

7. **Determine skill domain**:
   - Identify domain: competitive-coding, machine-learning, web-development, system-design, ai-engineering, etc.
   - Check if `.teach/domains/[domain]/` exists
   - If domain-specific templates exist, note them for future commands
   - This helps customize exercises and resources later

8. **Fill the skill definition template**:
   - Replace `[SKILL NAME]` with full descriptive name
   - Replace `[###-skill-name]` with actual skill ID
   - Set `[DATE]` to today
   - Set `Status` to "Planning"
   - Set `[Beginner/Intermediate/Advanced]` based on prerequisites (default: "Beginner" if uncertain)
   - Fill in all learning objectives with priorities
   - Fill in prerequisites
   - Leave "Clarifications" section for `/teachme.assess` command
   - Initialize progress tracking (all zeros)
   - Leave review checklist unchecked

9. **Load learning philosophy**:
   - Read `.teach/memory/philosophy.md` if it exists
   - Ensure skill objectives align with learner's principles
   - Adjust difficulty/pace based on philosophy
   - If philosophy doesn't exist, suggest creating one first with `/teachme.philosophy`

10. **Create initial progress.json**:
    ```json
    {
      "skill_id": "###-skill-name",
      "skill_name": "Full Skill Name",
      "status": "planning",
      "created_date": "YYYY-MM-DD",
      "current_level": "beginner",
      "target_level": "intermediate",
      "current_module": null,
      "modules_completed": [],
      "total_modules": 0,
      "exercises_completed": 0,
      "success_rate": null,
      "time_invested_hours": 0,
      "last_activity": "YYYY-MM-DD",
      "estimated_completion": null,
      "learning_streak_days": 0,
      "review_schedule": []
    }
    ```
    Save to `skills/###-skill-name/progress.json`

11. **Output summary**:
    - Display skill ID and path
    - Show learning objectives with priorities
    - List prerequisites
    - Show next steps:
      - Run `/teachme.assess` to determine current level
      - Or proceed to `/teachme.roadmap` if confident about level

12. **Suggest follow-up**:
    - Recommend running assessment first to customize learning path
    - Or if user is experienced, can skip directly to roadmap creation

**Important Notes**:
- This command focuses on WHAT to learn (objectives) not HOW to learn (that's `/teachme.roadmap`)
- Keep skill definitions focused and measurable
- Don't specify technologies/tools yet (that comes in roadmap)
- Make objectives independently testable
- Ensure each objective can be demonstrated practically

**Domain-Specific Adjustments**:

For **Competitive Coding**:
- Focus on problem-solving patterns and algorithms
- Success criteria = problems solved correctly within time limit
- Prerequisites include language proficiency

For **Machine Learning**:
- Balance theory understanding and implementation
- Success criteria = model performance metrics
- Prerequisites include mathematics (linear algebra, statistics)

For **Web Development**:
- Focus on practical projects and real-world scenarios
- Success criteria = working applications
- Prerequisites include HTML/CSS/JS basics

For **System Design**:
- Focus on architecture patterns and trade-offs
- Success criteria = design clarity and scalability reasoning
- Prerequisites include software engineering experience

For **AI Engineering**:
- Focus on LLM applications, prompting, RAG, agents
- Success criteria = functional AI systems
- Prerequisites include programming and basic ML concepts

Adjust learning objectives to match the domain appropriately.
