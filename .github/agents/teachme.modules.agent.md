---
description: Break down the learning roadmap into detailed, actionable learning modules with exercises, resources, and checkpoints.
handoffs: 
  - label: Start Learning
    agent: teachme.learn
    prompt: Begin learning with the first module
    send: true
  - label: Validate Module Plan
    agent: teachme.validate
    prompt: Validate the module breakdown
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

This command breaks down the learning roadmap into detailed, day-by-day modules with specific learning activities, exercises, and checkpoints.

1. **Load context**:
   - Load `skills/###-skill-name/skill-definition.md`
   - Load `skills/###-skill-name/roadmap.md` (required)
   - Load `skills/###-skill-name/progress.json`
   - Load `.teach/memory/philosophy.md`
   - Check if validation was run (recommended but not required)

2. **Verify roadmap exists**:
   - If roadmap doesn't exist: "Please run `/teachme.roadmap` first to create a learning path"
   - If roadmap is incomplete: Flag issues and suggest fixing

3. **Copy modules template**:
   - Copy `.teach/templates/modules-template.md` to `skills/###-skill-name/modules.md`
   - Initialize with skill name and metadata

4. **Extract roadmap structure**:
   - Identify the 3 phases (Foundation, Development, Mastery)
   - Note the module sequence from roadmap
   - Extract estimated time commitments
   - Note current level and any modules to skip

5. **Generate detailed modules for each phase**:

   For each phase in the roadmap, create detailed modules:

   ### Phase 1: Foundation
   
   For each concept/topic in Phase 1:
   
   **Module Structure**:
   - Module ID: M001, M002, etc.
   - Phase Tag: [P1-Foundation]
   - Module Name: Clear, descriptive name
   - Learning Activity: Study theory, practice, project, review
   - Estimated Time: Be specific (2 hours, 3 hours)
   - Difficulty: Easy, Medium, Hard (⭐⭐⭐)
   
   **Module Types**:
   - **Theory Module**: Reading/watching to learn concepts
     - Include specific resources
     - Key takeaways to understand
     - Self-check questions
   
   - **Practice Module**: Hands-on exercises
     - Number of problems (e.g., "10 basic problems")
     - Passing threshold (e.g., "Must score 8/10")
     - Problem difficulty level
     - Link to exercises directory
   
   - **Project Module**: Build something real
     - Project description
     - Skills applied
     - Time estimate
     - Success criteria
   
   - **Checkpoint Module**: Assessment before advancing
     - Quiz or practical test
     - Passing score requirement
     - Covers previous modules
     - Must pass to proceed
   
   **Include parallel markers [P]**:
   - Mark modules that can be studied in parallel
   - Only mark parallel if truly independent
   - Example: M008 [P] and M009 [P] can be studied together

6. **Create specific module details**:

   For each module, provide:
   
   ```markdown
   ### M001: Introduction & Overview
   
   **Learning Objective**: [Specific objective from skill-definition.md]
   
   **Resources**:
   - [PRIMARY] [Specific video/article/chapter with link]
   - [ALTERNATIVE] [Different explanation style]
   - [REFERENCE] [Documentation or cheat sheet]
   
   **Prerequisites**: [None / M000 completed]
   
   **Key Topics**:
   1. [Subtopic 1 with brief explanation]
   2. [Subtopic 2]
   3. [Subtopic 3]
   
   **Study Tips**:
   - [Specific advice for this module]
   - [Common confusion point and how to clarify]
   - [Visualization or analogy that helps]
   
   **Self-Check Questions**:
   1. Can you explain [concept] without looking?
   2. What are the trade-offs of [approach]?
   3. When would you use [technique]?
   
   **Estimated Time**: [X hours]
   
   **Next Steps**: Complete M002 practice to reinforce
   ```

7. **Generate exercises for practice modules**:

   For each practice module, create actual exercises:
   
   Create directory: `skills/###-skill-name/exercises/module-01/`
   
   For competitive coding:
   ```markdown
   # Module 01 Practice Exercises
   
   ## Exercise 1.1: Two Sum (Easy)
   
   **Problem**: Given an array of integers and a target, return indices of two numbers that add up to target.
   
   **Examples**:
   - Input: nums = [2,7,11,15], target = 9
   - Output: [0,1] (because nums[0] + nums[1] == 9)
   
   **Constraints**:
   - 2 ≤ nums.length ≤ 10^4
   - -10^9 ≤ nums[i] ≤ 10^9
   - Only one valid answer exists
   
   **Test Cases**:
   ```python
   assert two_sum([2,7,11,15], 9) == [0,1]
   assert two_sum([3,2,4], 6) == [1,2]
   assert two_sum([3,3], 6) == [0,1]
   ```
   
   **Hints** (reveal after 10 minutes):
   - Hint 1: Brute force is O(n²) - can we do better?
   - Hint 2: Consider using a hash map to track seen numbers
   - Hint 3: For each number, check if (target - number) exists
   
   **Solution** (reveal after 20 minutes or after solving):
   ```python
   def two_sum(nums, target):
       seen = {}
       for i, num in enumerate(nums):
           complement = target - num
           if complement in seen:
               return [seen[complement], i]
           seen[num] = i
       return []
   ```
   
   **Explanation**:
   - We use a hash map to store numbers we've seen
   - For each number, we check if its complement exists
   - Time: O(n), Space: O(n)
   
   **Related Problems**:
   - Three Sum
   - Two Sum II
   ```
   
   Generate 10-15 exercises per practice module

8. **Calculate phase totals**:

   For each phase, calculate:
   - Total modules
   - Total estimated hours
   - Number of practice exercises
   - Number of checkpoints
   
   Provide phase summary:
   ```markdown
   **Total Phase 1 Time**: ~16 hours over 2 weeks at 2 hours/day
   ```

9. **Create spaced repetition schedule**:

   Build review schedule into modules:
   
   ```markdown
   ## Spaced Repetition Schedule
   
   | Week | Review Topics | Time | Activities |
   |------|---------------|------|------------|
   | 3 | Phase 1 concepts | 1 hour | Redo 5 problems, explain concepts aloud |
   | 5 | Phase 1 + early Phase 2 | 1.5 hours | Mixed problem set, identify patterns |
   | 7 | All Phase 1 & 2 | 2 hours | Comprehensive quiz, project review |
   ```
   
   Include review modules:
   - R001-REVIEW: Week 3 Review
   - R002-REVIEW: Week 5 Review
   - etc.

10. **Initialize progress tracking**:

    Add to modules.md:
    ```markdown
    ## Progress Tracking
    
    **Modules Completed**: [0/33] (0%)
    
    **Phase Progress**:
    - Phase 1 (Foundation): [0/7] modules
    - Phase 2 (Development): [0/10] modules
    - Phase 3 (Mastery): [0/13] modules
    - Review: [0/3] sessions
    
    **Time Invested**: [0 hours] of estimated [113.5 hours]
    
    **Current Success Rate**: N/A
    
    **Stuck Points**: [Note any modules where struggling]
    
    **Breakthroughs**: [Note "aha" moments]
    ```

11. **Add adjustment log section**:
    
    ```markdown
    ## Adjustment Log
    
    **Pace Adjustments**:
    - [DATE]: [What changed and why]
    
    **Resource Changes**:
    - [DATE]: [Better resource found]
    
    **Custom Additions**:
    - [DATE]: [Extra practice added]
    ```

12. **Domain-specific module generation**:

    **Competitive Coding**:
    - Modules focus on algorithm patterns
    - Include LeetCode/HackerRank problem links
    - Emphasize time/space complexity analysis
    - Mock interview practice in Phase 3
    
    **Machine Learning**:
    - Balance theory and implementation modules
    - Include Jupyter notebook exercises
    - Dataset exploration modules
    - Model evaluation and interpretation
    - Math prerequisites if needed
    
    **Web Development**:
    - Project-based modules
    - Each module builds a feature
    - Include deployment and testing
    - Progressive complexity
    
    **System Design**:
    - Case study modules
    - Trade-off analysis exercises
    - Design document writing
    - Mock interview practice
    
    **AI Engineering**:
    - LLM prompting exercises
    - RAG system implementation
    - Agent building modules
    - Evaluation and monitoring

13. **Validate module sequence**:

    Ensure:
    - Prerequisites are respected (can't do M005 before M003)
    - Difficulty progression is smooth
    - Theory followed by practice
    - Regular checkpoints
    - Balanced time per module
    - Achievable in stated timeline

14. **Update progress.json**:
    ```json
    {
      "total_modules": 33,
      "modules": [
        {
          "id": "M001",
          "name": "Introduction & Overview",
          "phase": "P1-Foundation",
          "status": "not-started",
          "estimated_hours": 2,
          "actual_hours": 0,
          "completed_date": null
        },
        ...
      ]
    }
    ```

15. **Output summary**:

    **Module Breakdown Complete**:
    - **Total Modules**: 33 modules across 3 phases
    - **Foundation**: 7 modules (~16 hours)
    - **Development**: 10 modules (~40 hours)
    - **Mastery**: 13 modules (~58 hours)
    - **Review Sessions**: 3 scheduled review periods
    - **Total Estimated Time**: 114 hours over 12 weeks
    
    **Exercises Created**:
    - [X] Foundation practice exercises
    - [X] Intermediate problem sets
    - [X] Advanced challenges
    - [X] Project templates
    
    **Next Steps**:
    - Review modules.md to see full breakdown
    - Start learning with `/teachme.learn` command
    - Or adjust modules if needed and re-run this command
    
    **Ready to Begin Learning!** 🚀

16. **Provide encouragement**:
    - "Your personalized learning modules are ready!"
    - "Each module is designed to build on the previous one"
    - "Remember: it's okay to adjust pace as you learn"
    - "Run `/teachme.learn` when ready to start Module 01"

**Important Notes**:

- **Granularity**: Make modules small enough to complete in one session (1-4 hours)
- **Actionable**: Each module should have clear inputs, activities, and outputs
- **Measurable**: Include success criteria and self-checks
- **Flexible**: Make it clear modules can be adjusted based on progress
- **Motivating**: Build in quick wins and regular achievements
- **Realistic**: Don't overload modules - better to have more smaller modules

**Module Difficulty Calibration**:

Based on current_level from assessment:
- **Beginner**: Start with more foundational modules, smaller steps
- **Intermediate**: Can handle larger modules, skip some basics
- **Advanced**: Focus on advanced topics and projects, condense foundations

**Exercise Generation Guidelines**:

- **Easy (⭐)**: Direct application of single concept
- **Medium (⭐⭐)**: Combine 2-3 concepts, some problem-solving required
- **Hard (⭐⭐⭐)**: Multiple concepts, optimization needed, edge cases

Always include:
- Clear problem statement
- Examples
- Test cases
- Hints (progressive)
- Solution with explanation
- Time/space complexity analysis (for coding problems)
- Related problems for further practice

This creates a complete, actionable learning plan ready for execution.
