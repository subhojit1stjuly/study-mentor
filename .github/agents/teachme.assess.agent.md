---
description: Run diagnostic assessment to determine current skill level, identify knowledge gaps, and customize the learning path.
handoffs: 
  - label: Create Learning Roadmap
    agent: teachme.roadmap
    prompt: Create a roadmap based on assessment results. I want to use...
    send: true
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

This command runs a diagnostic assessment to determine the learner's current skill level and identify knowledge gaps. The results will customize the learning roadmap and module sequence.

1. **Locate the active skill**:
   - Check for `.teach/memory/active-skill.json` to find current skill
   - Or read user input if they specify a skill ID
   - Or prompt user to select from `skills/` directory
   - Load `skills/###-skill-name/skill-definition.md`

2. **Check for existing assessment**:
   - Look in `skills/###-skill-name/` for previous assessment files
   - If recent assessment exists (< 7 days old), ask if user wants to retake
   - Show previous results and allow user to proceed or retake

3. **Copy assessment template**:
   - Copy `.teach/templates/assessment-template.md` to `skills/###-skill-name/assessment-diagnostic.md`
   - Set assessment type to "Diagnostic"
   - Set date to today

4. **Generate assessment questions**:
   Based on the learning objectives in skill-definition.md, create:
   
   **Part 1: Conceptual Understanding** (3-5 questions)
   - Test understanding of fundamental concepts
   - Open-ended explanation questions
   - Identify if prerequisites are met
   
   **Part 2: Applied Knowledge** (3-5 problems)
   - Easy (⭐): Tests basic application
   - Medium (⭐⭐): Tests intermediate concepts
   - Hard (⭐⭐⭐): Tests advanced understanding
   - Include test cases and expected outputs
   - Problems should align with skill objectives
   
   **Part 3: Pattern Recognition** (2-3 scenarios)
   - Present problem descriptions without explicit technique mention
   - Ask user to identify appropriate approach
   - Tests ability to recognize when to apply concepts
   
   **Part 4: Teaching & Explanation** (1-2 tasks)
   - Ask user to explain a concept as if teaching a beginner
   - Tests depth of understanding
   - If user can't teach it, they don't fully understand it

5. **Configure assessment parameters**:
   - **Time Limit**: Set based on skill complexity and philosophy
   - **Passing Score**: Default 70% for diagnostic (to identify gaps)
   - **Format**: Mixed (questions + coding + explanation)
   - **Tools Allowed**: Documentation only for diagnostic (no full internet)
   - **Retry Policy**: Unlimited (this is for learning, not evaluation)

6. **Present assessment to user**:
   Display: "I've created a diagnostic assessment to determine your current level. The assessment has X questions and should take about Y minutes."
   
   **Important**: You can either:
   - Have the user complete the assessment inline (recommended for shorter assessments)
   - Direct them to open `skills/###-skill-name/assessment-diagnostic.md` and fill it out
   - For coding problems, they can use their preferred IDE
   
   Ask: "Would you like to complete the assessment now, or open the file and return when done?"

7. **If completing inline**:
   - Present questions one at a time or in sections
   - Wait for user responses
   - Record answers in the assessment file as you go
   - Provide encouraging feedback between sections
   - Don't reveal correct answers yet

8. **If completing offline**:
   - Instruct user to open the file
   - Explain how to mark answers
   - Tell them to return with `/teachme.assess --review` when done
   - Save progress

9. **Evaluate responses** (when user returns or after inline completion):
   - Score each part objectively
   - For coding problems: Check correctness, efficiency, code quality
   - For explanations: Check clarity, accuracy, completeness
   - For pattern recognition: Check if identified correct approach
   
   Calculate:
   - Part scores (percentage for each part)
   - Overall score
   - Pass/fail status based on threshold

10. **Identify gaps and strengths**:
    
    **Strengths** - What they got right:
    - List concepts they clearly understand
    - Note any areas of exceptional knowledge
    
    **Areas for Improvement** - What needs practice:
    - Concepts with partial understanding
    - Recommend specific modules or resources
    
    **Knowledge Gaps** - Critical missing prerequisites:
    - Foundational concepts they don't know
    - Required action before proceeding
    - May need to learn prerequisites first

11. **Determine current level**:
    Based on assessment results:
    - **Beginner**: < 50% on diagnostic, missing foundational concepts
    - **Intermediate**: 50-75%, understands basics, needs practice
    - **Advanced**: > 75%, strong foundation, ready for complex topics
    
    Or if skill has specific criteria, use those.

12. **Update skill definition**:
    Add "Clarifications" section to `skills/###-skill-name/skill-definition.md`:
    ```markdown
    ## Clarifications

    **Assessment Date**: YYYY-MM-DD

    **Current Level Determination**: [Level] (based on diagnostic score)

    ### Identified Gaps

    1. **Gap**: [Specific missing knowledge]
       - **Impact**: [How this affects learning]
       - **Recommended Action**: [What to study first]

    ### Strengths

    1. **Strength**: [Existing knowledge]
       - **Leverage**: [How to build on this]
    ```

13. **Customize learning path recommendations**:
    Based on level and gaps:
    - **If Beginner**: Start from Module 01, include prerequisite refreshers
    - **If Intermediate**: Can skip early modules, start at Module 04-05
    - **If Advanced**: Focus on advanced modules and projects, skip basics
    - Identify which modules need extra practice
    - Suggest which modules can be completed quickly

14. **Update progress.json**:
    ```json
    {
      "current_level": "beginner/intermediate/advanced",
      "assessment_date": "YYYY-MM-DD",
      "assessment_score": 65.5,
      "strengths": ["list", "of", "strengths"],
      "gaps": ["list", "of", "gaps"],
      "recommended_starting_module": "M04",
      "modules_to_skip": ["M01", "M02"],
      "modules_needing_extra_practice": ["M07", "M09"]
    }
    ```

15. **Output detailed feedback**:
    
    **Assessment Results Summary**:
    - Overall score: X%
    - Current level: [Level]
    - Passing status: [PASSED / NEEDS REVIEW]
    
    **Strengths**: [List with checkmarks ✅]
    
    **Areas for Improvement**: [List with warnings ⚠️]
    
    **Knowledge Gaps**: [List with alerts ❌]
    
    **Recommended Next Steps**:
    - If gaps exist: Study [prerequisite] before proceeding
    - If passed: Proceed to `/teachme.roadmap` to create learning path
    - Suggested starting point: Module XX
    - Modules to skip: [list]
    - Focus areas: [list]

16. **Encourage and motivate**:
    - Acknowledge effort in completing assessment
    - Frame gaps as opportunities, not deficiencies
    - Celebrate strengths
    - Emphasize that assessment helps customize path for faster learning
    - Remind that assessments can be retaken as they progress

**Important Notes**:

- **This is diagnostic, not evaluative**: The goal is to customize the learning path, not to grade the learner
- **No pressure**: Encourage honesty - it's better to identify gaps now than struggle later
- **Adaptive**: If user struggles significantly, offer to create a prerequisite learning path first
- **Growth mindset**: Frame everything positively - gaps are normal and fixable
- **Privacy**: Assessment results stay local, never shared

**Domain-Specific Assessment Strategies**:

**Competitive Coding**:
- Include 2-3 coding problems of varying difficulty
- Test knowledge of data structures and algorithms
- Check time complexity analysis skills

**Machine Learning**:
- Test theoretical understanding (concepts, math)
- Include coding exercise (implement simple model)
- Test ability to interpret results and metrics

**Web Development**:
- Test HTML/CSS/JS fundamentals
- Small coding exercise (build a simple component)
- Test debugging skills

**System Design**:
- Present design scenario
- Evaluate architecture decisions and trade-offs
- Test knowledge of scalability patterns

**AI Engineering**:
- Test LLM prompting skills
- Check understanding of RAG, embeddings, agents
- Small implementation exercise

Adjust question types and difficulty based on skill domain.
