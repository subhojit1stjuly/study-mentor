Run a mock interview session.

Round type: $ARGUMENTS

---

If no round type is specified, ask: "Which type of mock interview? (1) Coding, (2) System Design, (3) Behavioral"

Read the interview prep skill for full evaluation criteria: `@.claude/skills/interview-prep/SKILL.md`

---

## Coding Round (45 min)

1. Present a LeetCode-style problem appropriate for senior level (Medium or Hard)
   - State the problem clearly with input/output examples
   - Do NOT reveal the optimal approach or hints unless asked
2. Let the candidate ask clarifying questions (answer them in character as interviewer)
3. Let the candidate think aloud and code — do not interrupt unless they're stuck for 5+ minutes
4. If stuck, give one progressive hint at a time

**Evaluation** (after candidate submits):
- Correctness: Does it work on all cases?
- Time complexity: Did they get the optimal or near-optimal solution?
- Code quality: Clean, readable, proper naming?
- Communication: Did they explain their thinking?
- Scores: Problem Solving (1-5), Code Quality (1-5), Communication (1-5), Overall (1-5)

---

## System Design Round (45 min)

1. Give a system to design (e.g., "Design a URL shortener", "Design Twitter's feed")
2. Let the candidate drive — follow the framework but don't over-guide:
   - Requirements → Estimation → API → Data Model → HLD → Deep Dives → Trade-offs
3. Ask probing questions: "How would this scale to 10M users?", "What happens if the database goes down?"
4. Let them drive for ~35 minutes

**Evaluation** (after design is complete):
- Requirements gathering: Did they clarify scope?
- Architecture: Is the design sound and complete?
- Deep dives: Did they go deep on critical components?
- Trade-offs: Did they justify their choices?
- Scores: Requirements (1-5), Architecture (1-5), Deep Dives (1-5), Trade-offs (1-5), Communication (1-5)

---

## Behavioral Round (30 min)

1. Ask 4-5 behavioral questions — mix of:
   - Leadership: "Tell me about a time you led a project under tight constraints"
   - Conflict: "Describe a disagreement with a colleague — how did you resolve it?"
   - Failure: "Tell me about a significant mistake you made and what you learned"
   - Impact: "What's the most impactful project you've worked on?"
   - Ambiguity: "Tell me about a time you had to make a decision with incomplete information"
2. After each answer: brief feedback on STAR structure and content
3. Probe deeper if the answer is vague: "What was YOUR specific role?", "What was the measurable outcome?"

**Evaluation** (after all questions):
- Specificity: Were stories concrete with real details?
- Impact: Was the impact quantified and significant?
- Self-Awareness: Did they reflect honestly, including on failures?
- Communication: Was the STAR structure clear?
- Scores: Specificity (1-5), Impact (1-5), Self-Awareness (1-5), Communication (1-5)

---

## End of Session — Summary

Provide:
1. **Overall Assessment** — 2-3 sentence summary of the session
2. **Top 2 Strengths** — what they did well
3. **Top 2 Areas to Improve** — specific, actionable feedback
4. **Action Items** — concrete steps for the next practice session
5. **Score Card** — all dimension scores in a table

Save the full mock interview log (problem/question, candidate answers, scores, feedback) to `interview/mock-logs.md` with today's date and round type as the header.
