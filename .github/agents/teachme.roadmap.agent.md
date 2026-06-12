---
description: Create a customized learning roadmap with resources, timeline, and learning strategy based on skill definition and assessment results.
handoffs: 
  - label: Break Into Modules
    agent: teachme.modules
    prompt: Break the roadmap into detailed learning modules
    send: true
  - label: Create Assessment
    agent: teachme.assess
    prompt: Create formative assessment for progress check
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

This command creates a comprehensive learning roadmap based on the skill definition and assessment results (if available).

1. **Locate the active skill**:
   - Check `.teach/memory/active-skill.json` for current skill
   - Or use skill ID from user input
   - Load `skills/###-skill-name/skill-definition.md`
   - Load `skills/###-skill-name/progress.json`

2. **Check prerequisites**:
   - Ensure skill definition exists (if not, run `/teachme.define` first)
   - Check if assessment was completed
   - If no assessment: Ask if user wants to run `/teachme.assess` first (recommended)
   - Can proceed without assessment but roadmap will be generic

3. **Load context**:
   - Read `.teach/memory/philosophy.md` for learning preferences
   - Read assessment results if available (current level, gaps, strengths)
   - Note user input about technologies, resources, or preferences

4. **Copy roadmap template**:
   - Copy `.teach/templates/roadmap-template.md` to `skills/###-skill-name/roadmap.md`
   - Set skill ID, date, and link to skill definition

5. **Gather learning context from user**:
   
   Ask about (if not in user input or philosophy):
   
   **Tech Stack / Tools** (if applicable):
   - "What programming language / framework do you want to use?"
   - For competitive coding: Python, Java, C++?
   - For ML: TensorFlow, PyTorch, scikit-learn?
   - For web dev: React, Vue, vanilla JS?
   
   **Learning Resources**:
   - "Do you prefer video courses, books, interactive coding platforms, or documentation?"
   - Any specific courses or platforms you already have access to?
   
   **Timeline**:
   - "How much time can you dedicate? (e.g., 2 hours/day, 10 hours/week)"
   - "What's your target timeline? (e.g., 3 months, 6 months, 1 year)"
   
   **Practice Platforms**:
   - For coding: LeetCode, HackerRank, CodeWars?
   - For ML: Kaggle, Google Colab?
   - Personal projects?

6. **Fill Learning Context section**:
   - **Current Level**: From assessment or ask user (Beginner/Intermediate/Advanced)
   - **Target Level**: Based on skill definition objectives
   - **Learning Style**: From philosophy or ask
   - **Time Commitment**: Specific schedule
   - **Preferred Resources**: Video, books, interactive, docs
   - **Learning Environment**: Self-paced, course, mentored
   - **Success Timeline**: Estimate based on time commitment and level
   - **Primary Motivation**: From philosophy or skill definition
   - **Practice Platforms**: Specific platforms for this skill

7. **Check philosophy alignment**:
   - Read `.teach/memory/philosophy.md`
   - Ensure roadmap respects learning principles
   - Example: If philosophy says "practice-driven", emphasize hands-on exercises
   - Example: If philosophy says "self-paced", don't set rigid deadlines
   - Example: If philosophy says "spaced repetition", build in review sessions

8. **Research and recommend resources**:
   
   For each category, suggest 2-3 options:
   
   **Books**: Find relevant books for this skill and level
   - Include title, author, why recommended
   - Note if it's beginner-friendly, reference, or advanced
   
   **Online Courses**: Research available courses
   - Platform, instructor, duration, key topics
   - Free vs paid options
   - Match to learning style
   
   **Video Tutorials**: Find quality video content
   - YouTube channels, playlists, specific series
   - Note teaching style and length
   
   **Practice Platforms**: Recommend specific platforms
   - Based on skill domain
   - Competitive coding: LeetCode, HackerRank, Codeforces
   - ML: Kaggle, Google Colab, Fast.ai
   - Web dev: freeCodeCamp, Frontend Mentor
   
   **Documentation & References**: Official docs and cheat sheets
   
   **Community & Support**: Forums, Discord, study groups

9. **Design module sequence**:
   
   Based on skill objectives (P1, P2, P3) and assessment results, organize into 3 phases:
   
   **Phase 1: Foundation** (Weeks 1-2 or adjust based on time commitment)
   - Cover all P1 (critical) learning objectives
   - Build solid understanding of core concepts
   - Aim for 3-4 modules
   - Checkpoint: Can explain core concepts and solve basic problems
   
   **Phase 2: Skill Development** (Weeks 3-6 or adjust)
   - Cover P2 (intermediate) objectives
   - Diverse practice and pattern recognition
   - Aim for 5-7 modules
   - Checkpoint: Can solve intermediate problems, recognize patterns
   
   **Phase 3: Mastery & Application** (Weeks 7-12 or adjust)
   - Cover P3 (advanced) objectives
   - Real-world projects and optimization
   - Interview prep or capstone
   - Aim for 5-6 modules
   - Checkpoint: Can teach others, apply in novel contexts
   
   **Adjust based on assessment**:
   - If current level is Intermediate: Condense Phase 1, expand Phase 2-3
   - If Advanced: Skip Phase 1, focus on Phase 3 and projects
   - If Beginner: Add prerequisite module before Phase 1 if needed

10. **Define learning strategy**:
    
    **Daily Practice**: Specific recommendation based on time commitment
    - Example: "Spend 1 hour on new concepts, 1 hour on practice problems"
    
    **Spaced Repetition**: Create review schedule
    - Week 3: Review Phase 1
    - Week 5: Review Phase 1 + early Phase 2
    - Week 7: Comprehensive review
    - Week 9: Focus on weak areas
    - Week 11: Final review
    
    **Active Recall**: How to test without looking at solutions
    - Redo problems from scratch
    - Explain concepts aloud
    - Teach someone else
    
    **Deliberate Practice**: Focus on weak areas
    - Spend 70% time on challenging topics, 30% on review
    - Don't just practice what's comfortable
    
    **Project Application**: Build something real
    - After every 3-4 modules, apply in a mini-project
    - Phase 3 includes capstone project

11. **Identify common pitfalls**:
    
    Research common mistakes for this skill:
    - ⚠️ **Pitfall 1**: [Common mistake] → [How to avoid]
    - ⚠️ **Pitfall 2**: [Learning trap] → [Better approach]
    - ⚠️ **Pitfall 3**: [What students often do wrong] → [Correct strategy]
    
    Examples for competitive coding:
    - ⚠️ Reading solutions too quickly → Try for 30+ minutes first
    - ⚠️ Not analyzing time complexity → Always analyze before coding
    - ⚠️ Practicing only easy problems → Mix difficulties

12. **Design motivation maintenance strategy**:
    
    **Milestones**: Define achievement points every 2 weeks
    - Completed foundation phase
    - Solved first hard problem
    - Built first project
    
    **Progress Tracking**: Use progress.json, celebrate wins
    
    **Accountability**: Suggest study groups or sharing progress
    
    **Rewards**: Suggest personal rewards for completing phases

13. **Define assessment strategy**:
    
    **Diagnostic Assessment**: Already done (if `/teachme.assess` was run)
    
    **Formative Assessments**: During learning
    - Practice exercises after each concept
    - Mini-quizzes every 3-4 modules
    - Self-checks before advancing
    
    **Summative Assessments**: End of each phase
    - Phase capstone project or comprehensive quiz
    - Must pass to advance to next phase
    
    **Final Mastery Assessment**: End of skill
    - Complex project or mock interview
    - Teaching session or open source contribution

14. **Create philosophy alignment table**:
    
    For each principle in philosophy.md:
    | Philosophy Principle | How This Roadmap Aligns | Adjustment Needed? |
    |---------------------|-------------------------|-------------------|
    | [Principle] | [Specific alignment] | [Yes/No - what?] |
    
    If adjustments needed, update roadmap accordingly

15. **Estimate timeline**:
    
    Based on:
    - Number of modules planned
    - Time commitment per day/week
    - Current level (can skip modules or need extra time)
    - Complexity of skill
    
    Provide realistic estimate: "With X hours/day, expect to complete in Y months"
    Include range: "3-4 months depending on progress"

16. **Save roadmap**:
    - Write to `skills/###-skill-name/roadmap.md`
    - Update `progress.json` with estimated timeline and phases

17. **Output summary**:
    
    **Learning Roadmap Created**:
    - **Timeline**: X months with Y hours/week
    - **Phases**: 3 phases, Z total modules
    - **Resources**: Recommended books, courses, platforms
    - **Starting Point**: [Module to start based on assessment]
    - **Can Skip**: [Modules if advanced]
    - **Extra Focus**: [Modules needing more time based on gaps]
    
    **Next Steps**:
    - Review the roadmap in `skills/###-skill-name/roadmap.md`
    - Adjust resources if needed
    - Run `/teachme.modules` to break into detailed learning modules
    - Or make changes and re-run this command

18. **Encourage action**:
    - "Your personalized learning path is ready!"
    - "The roadmap is customized based on your [level/goals/preferences]"
    - "Next, run `/teachme.modules` to break this into day-by-day learning modules"

**Important Notes**:

- **Personalization is key**: Use assessment results and philosophy to customize
- **Flexibility**: Make it clear the roadmap can be adjusted as they learn
- **Resources matter**: Provide specific, actionable resource recommendations
- **Motivation**: Build in strategies to maintain momentum
- **Realistic**: Don't overpromise - set achievable timelines
- **Check domain templates**: If `.teach/domains/[domain]/` exists, use domain-specific roadmap structure

**Domain-Specific Roadmap Considerations**:

**Competitive Coding**:
- Focus on algorithm patterns and problem-solving strategies
- Recommend specific problem lists (e.g., "Blind 75", "NeetCode 150")
- Include mock interview practice
- Daily problem-solving as core activity

**Machine Learning**:
- Balance theory (math, concepts) with implementation
- Include dataset exploration and model building
- Recommend Kaggle competitions for practice
- Math prerequisites may need separate modules

**Web Development**:
- Project-based learning path
- Build progressively complex applications
- Include deployment and best practices
- Modern tooling and frameworks

**System Design**:
- Case study-based learning
- Trade-off analysis for each pattern
- Mock design interviews
- Real-world architecture examples

**AI Engineering**:
- Hands-on with LLMs, prompting, RAG
- Build functional AI applications
- Include evaluation and monitoring
- Stay current with rapidly evolving field

Adjust roadmap structure to fit domain naturally.
