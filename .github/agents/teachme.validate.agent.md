---
description: Validate learning path for consistency, completeness, and alignment with skill objectives and philosophy.
handoffs: 
  - label: Create Modules
    agent: teachme.modules
    prompt: Break the roadmap into learning modules
    send: true
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

This command performs a comprehensive validation of the learning path to ensure consistency between skill definition, assessment results, roadmap, and philosophy.

1. **Locate skill and artifacts**:
   - Load `skills/###-skill-name/skill-definition.md`
   - Load `skills/###-skill-name/roadmap.md` (if exists)
   - Load `skills/###-skill-name/progress.json`
   - Load `.teach/memory/philosophy.md`
   - Load assessment results if available

2. **Validation checks to perform**:

   ### Check 1: Skill Definition Completeness
   
   Verify skill-definition.md has:
   - ✅ At least 3 learning objectives defined
   - ✅ Each objective has priority (P1, P2, P3)
   - ✅ Success criteria for each objective
   - ✅ Real-world applications defined
   - ✅ Prerequisites clearly listed
   - ✅ No remaining template placeholders
   
   **Report**: List missing elements or mark PASS

   ### Check 2: Philosophy Alignment
   
   Compare roadmap against philosophy principles:
   - ✅ Learning pace matches philosophy (self-paced vs structured)
   - ✅ Resource types match preferences (video vs reading vs hands-on)
   - ✅ Time commitment is realistic and matches philosophy
   - ✅ Assessment thresholds match philosophy (strict vs lenient)
   - ✅ Spaced repetition included if philosophy requires it
   
   **Report**: Highlight misalignments with specific recommendations

   ### Check 3: Roadmap Coverage
   
   Verify roadmap covers all skill objectives:
   - For each objective in skill-definition.md:
     - ✅ Is it addressed in roadmap phases?
     - ✅ Are resources provided to learn it?
     - ✅ Is there a way to practice it?
     - ✅ Is there assessment for mastery?
   
   **Report**: List any objectives not covered or inadequately addressed

   ### Check 4: Prerequisite Handling
   
   Check if prerequisites are addressed:
   - ✅ Are required prerequisites covered before advanced topics?
   - ✅ If assessment showed gaps, are they addressed?
   - ✅ Is there a module for prerequisites or recommendation to learn separately?
   
   **Report**: Flag any prerequisite gaps in learning sequence

   ### Check 5: Assessment Alignment
   
   If assessment was completed:
   - ✅ Does roadmap start at appropriate level (based on current_level)?
   - ✅ Are identified gaps from assessment addressed?
   - ✅ Are strengths leveraged (can skip certain modules)?
   - ✅ Is estimated timeline realistic given current level?
   
   **Report**: Highlight mismatches between assessment and roadmap

   ### Check 6: Resource Quality
   
   Check if roadmap provides adequate resources:
   - ✅ At least 2 learning resources per category (books, courses, videos)
   - ✅ Resources are specific (not generic "search online")
   - ✅ Mix of free and paid options provided
   - ✅ Practice platforms identified
   - ✅ Community/support options listed
   
   **Report**: Note missing or inadequate resource recommendations

   ### Check 7: Timeline Feasibility
   
   Validate timeline makes sense:
   - Calculate total estimated hours from all modules
   - Compare against time commitment in roadmap
   - Check if timeline is achievable
   - ✅ Timeline accounts for review/spaced repetition time
   - ✅ Timeline includes buffer for difficult concepts
   - ✅ Phases are balanced (not 80% in one phase)
   
   **Report**: Flag unrealistic timelines with adjusted recommendations

   ### Check 8: Progress Tracking Setup
   
   Verify tracking mechanisms:
   - ✅ progress.json exists and is initialized
   - ✅ Milestones defined for motivation
   - ✅ Checkpoints defined between phases
   - ✅ Success metrics are measurable
   
   **Report**: Note missing tracking elements

   ### Check 9: Domain-Specific Requirements
   
   Check for domain-specific considerations:
   - **Competitive Coding**: Problem sets, time complexity analysis, interview prep
   - **Machine Learning**: Math prerequisites, datasets, model evaluation
   - **Web Development**: Projects, deployment, best practices
   - **System Design**: Case studies, trade-off analysis
   - **AI Engineering**: LLM access, API keys, compute resources
   
   **Report**: Flag missing domain-critical elements

   ### Check 10: Motivation & Sustainability
   
   Check for learning sustainability:
   - ✅ Milestones defined every 1-2 weeks
   - ✅ Variety in learning methods (not just reading or just coding)
   - ✅ Progress celebration points identified
   - ✅ Fallback strategies for when stuck
   - ✅ Accountability mechanisms (optional but recommended)
   
   **Report**: Suggest additions for better motivation

3. **Generate validation report**:

   Create a comprehensive report with sections:

   ```markdown
   # Learning Path Validation Report
   
   **Skill**: [Skill Name]
   **Validation Date**: [DATE]
   **Overall Status**: [PASS / PASS WITH WARNINGS / NEEDS REVISION]
   
   ## Summary
   
   [Brief overview of validation results]
   
   - **Passed Checks**: X/10
   - **Warnings**: Y issues requiring attention
   - **Critical Issues**: Z issues requiring immediate fix
   
   ## Detailed Results
   
   ### ✅ Passing Checks
   
   - Check 1: Skill Definition Completeness - PASS
   - Check 3: Roadmap Coverage - PASS
   ...
   
   ### ⚠️ Warnings (Should Fix)
   
   #### Check 2: Philosophy Alignment
   - **Issue**: Roadmap suggests 3 hours/day but philosophy says 2 hours/day
   - **Impact**: May lead to burnout or unrealistic expectations
   - **Recommendation**: Adjust roadmap timeline to match 2 hours/day commitment
   
   #### Check 6: Resource Quality
   - **Issue**: Only 1 video resource provided, learner prefers video
   - **Impact**: Limited alternatives if first resource doesn't work
   - **Recommendation**: Add 2 more video tutorial options
   
   ### ❌ Critical Issues (Must Fix)
   
   #### Check 5: Assessment Alignment
   - **Issue**: Assessment identified gap in "recursion basics" but roadmap doesn't address it
   - **Impact**: Learner will struggle with DP modules without recursion foundation
   - **Recommendation**: Add "Recursion Fundamentals" module before DP modules, or create prerequisite learning path
   
   ## Coverage Analysis
   
   **Learning Objectives Coverage**:
   
   | Objective | Priority | Covered in Roadmap? | Resources | Practice | Assessment |
   |-----------|----------|---------------------|-----------|----------|------------|
   | [Obj 1] | P1 | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
   | [Obj 2] | P1 | ⚠️ Partial | ⚠️ Limited | ✅ Yes | ❌ No |
   | [Obj 3] | P2 | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
   
   ## Recommendations
   
   ### Immediate Actions (Required)
   1. [Critical fix 1]
   2. [Critical fix 2]
   
   ### Suggested Improvements (Optional)
   1. [Enhancement 1]
   2. [Enhancement 2]
   
   ### Timeline Adjustments
   - Original estimate: X months
   - Adjusted estimate: Y months (accounting for prerequisite work and realistic pace)
   
   ## Next Steps
   
   - [ ] Address critical issues above
   - [ ] Review and implement suggested improvements
   - [ ] Re-run `/teachme.validate` to confirm fixes
   - [ ] Proceed to `/teachme.modules` once validation passes
   ```

4. **Save validation report**:
   - Save to `skills/###-skill-name/validation-report.md`
   - Timestamp the validation

5. **Output to user**:
   
   **If PASS**:
   - "✅ Learning path validation complete - No critical issues found!"
   - "Your learning path is well-structured and ready to go."
   - "Found X minor suggestions for improvement (see report for details)"
   - "Next step: Run `/teachme.modules` to break into detailed modules"
   
   **If PASS WITH WARNINGS**:
   - "⚠️ Validation complete - Found Y warnings to address"
   - "Your path will work but could be improved"
   - "Review validation-report.md for specific recommendations"
   - "You can proceed to modules or fix warnings first"
   
   **If NEEDS REVISION**:
   - "❌ Critical issues found that should be fixed before proceeding"
   - "Found Z critical issues (see validation-report.md for details)"
   - "Recommended actions:"
     1. [First critical fix]
     2. [Second critical fix]
   - "After fixing, re-run `/teachme.validate`"
   - "Don't worry - these are normal adjustments to optimize your learning!"

6. **Provide actionable guidance**:
   
   For each issue found, provide:
   - **What's wrong**: Clear description of the issue
   - **Why it matters**: Impact on learning effectiveness
   - **How to fix**: Specific actionable recommendation
   - **Example**: If applicable, show what good looks like

7. **Track validation history**:
   
   Append to progress.json:
   ```json
   "validation_history": [
     {
       "date": "YYYY-MM-DD",
       "status": "PASS WITH WARNINGS",
       "passed_checks": 8,
       "warnings": 2,
       "critical_issues": 0
     }
   ]
   ```

**Important Notes**:

- **This is helpful, not punitive**: Frame all issues as opportunities to improve learning effectiveness
- **Prioritize**: Clearly distinguish critical issues from nice-to-haves
- **Be specific**: Don't just say "add more resources" - suggest specific resources
- **Context matters**: Consider learner's level, time, and goals when validating
- **Automated checks**: This can catch issues the learner might miss
- **Iterative**: Validation can be run multiple times as roadmap evolves

**When to run this command**:

- After creating/updating roadmap (before creating modules)
- After major changes to skill definition
- If learner feels stuck or path doesn't feel right
- Periodically (every 2-4 weeks) to ensure still on track
- Before final capstone to ensure all objectives covered

**Philosophy alignment examples**:

If philosophy says "Practice-Driven Learning":
- ✅ GOOD: 60% of time on exercises, 40% on theory
- ❌ BAD: 80% reading/watching, 20% coding

If philosophy says "Self-Paced Mastery":
- ✅ GOOD: "Complete when you understand, typically 2-4 weeks"
- ❌ BAD: "Must complete Phase 1 by Week 2"

If philosophy says "Spaced Repetition":
- ✅ GOOD: Review schedule built into roadmap
- ❌ BAD: No mention of reviewing previous concepts

This validation ensures learning path is optimized for the specific learner.
