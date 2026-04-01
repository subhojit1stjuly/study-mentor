---
name: interview-prep
description: "Use when: preparing for coding interviews, FAANG interview preparation, practicing behavioral questions, senior engineer interview prep, staff engineer interview, system design interview, coding round practice, mock interviews, Amazon leadership principles, Google interview, Meta interview, Apple interview, Microsoft interview, negotiating offers, resume review, technical interview tips."
argument-hint: "Type of prep (e.g., 'behavioral', 'coding round', 'system design interview', 'Amazon LP')"
---

# Interview Preparation Roadmap

A structured roadmap for preparing for senior/staff-level engineering interviews at top companies (Google, Meta, Amazon, Apple, Microsoft, Netflix, and top startups).

## When to Use

- Starting comprehensive interview preparation
- Practicing specific interview round types
- Preparing for a specific company
- Running mock interview sessions
- Reviewing behavioral / STAR stories
- Negotiating offers

---

## Phase 0: Foundation — Know the Process

> **Goal**: Understand what top companies look for at senior/staff level.

### Senior/Staff Level Expectations

| Dimension | What They Assess |
|-----------|-----------------|
| **Technical Depth** | Can you solve hard problems efficiently and discuss trade-offs? |
| **System Design** | Can you design scalable systems and drive architectural decisions? |
| **Communication** | Can you explain your thinking clearly, ask good questions, drive the conversation? |
| **Leadership** | Can you influence without authority, mentor others, make decisions with ambiguity? |
| **Impact** | Have you delivered meaningful results? Can you quantify your impact? |

### Interview Rounds (Typical)

| Round | Duration | What They Test |
|-------|----------|---------------|
| Phone Screen | 45-60 min | Coding + communication |
| Coding (x2) | 45 min each | DSA, problem solving, code quality |
| System Design | 45-60 min | Architecture, scalability, trade-offs |
| Behavioral (x1-2) | 45 min | Leadership, conflict, impact stories |
| Hiring Manager | 30-45 min | Culture fit, career goals, team match |

---

## Phase 1: Coding Interview Prep

> **Goal**: Solve medium/hard problems consistently within 25-30 minutes.

### Strategy

```
1. PATTERN RECOGNITION  → Learn the 15 core patterns (see dsa-mastery skill)
2. TARGETED PRACTICE    → 3-5 problems per pattern, increasing difficulty
3. TIMED PRACTICE       → Solve under interview conditions (35 min, no hints)
4. REVIEW & REFLECT     → Analyze mistakes, note patterns you missed
5. MOCK                 → Practice with a partner or interviewer.io
```

### Weekly Schedule (12-week plan)

| Weeks | Focus | Problems/Week |
|-------|-------|--------------|
| 1-2 | Arrays, Strings, Hashing | 10 (Easy/Medium) |
| 3-4 | Linked Lists, Stacks, Queues | 10 |
| 5-6 | Trees, Graphs, BFS/DFS | 12 |
| 7-8 | Dynamic Programming | 12 |
| 9-10 | Advanced (Heap, Trie, Backtracking, Binary Search on Answer) | 10 |
| 11-12 | Mixed practice + timed mocks | 10 |

### Problem Lists

| List | Problems | Best For |
|------|----------|----------|
| NeetCode 150 | 150 | Pattern-based, curated |
| Blind 75 | 75 | Time-constrained prep |
| LeetCode Top Interview 150 | 150 | Comprehensive |
| Sean Prashad's Patterns | 170+ | Pattern-organized |

### Senior-Level Coding Tips
- **Think aloud** — interviewer wants to see your process
- **Clarify first** — ask about constraints, edge cases, input size
- **Start working** — a brute force solution beats silence
- **Analyze before optimizing** — state complexity, then improve
- **Test your code** — walk through an example, check edge cases
- **Discuss alternatives** — "We could also use X, which would give us..."

---

## Phase 2: System Design Interview Prep

> **Goal**: Drive a 45-minute design discussion confidently.

### Framework

```
1. REQUIREMENTS (5 min)
   → Functional: What does the system do?
   → Non-functional: Scale, latency, availability, consistency
   → Scope: What's in/out for this discussion?

2. ESTIMATION (3 min)
   → Users, QPS (peak), storage, bandwidth
   → Quick math to justify decisions

3. API DESIGN (3 min)
   → Key endpoints with request/response
   → Pagination, authentication noted

4. DATA MODEL (5 min)
   → Schema, SQL vs NoSQL choice (justified)
   → Access patterns drive schema design

5. HIGH-LEVEL DESIGN (10 min)
   → ASCII diagram with all components
   → Data flow explained step by step

6. DEEP DIVES (15 min)
   → YOU pick 2-3 areas that matter most
   → Show depth: caching strategy, database scaling, real-time delivery
   → Discuss trade-offs proactively

7. WRAP-UP (4 min)
   → Bottlenecks and how to address them
   → Monitoring, alerting, failure scenarios
   → What you'd add with more time
```

### Must-Practice Systems

| Priority | System | Key Concepts |
|----------|--------|-------------|
| Critical | URL Shortener | Hashing, read-heavy, database |
| Critical | Chat System (WhatsApp) | WebSocket, ordering, E2E encryption |
| Critical | News Feed (Twitter) | Fan-out, ranking, caching |
| Critical | Video Streaming (Netflix) | CDN, transcoding, adaptive bitrate |
| High | Ride Sharing (Uber) | Geospatial, matching, real-time |
| High | Notification System | Priority queues, multi-channel, delivery |
| High | Rate Limiter | Token bucket, distributed, Redis |
| High | Distributed Cache | Consistent hashing, eviction |
| Medium | Search Engine | Crawler, inverted index, ranking |
| Medium | Payment System | Idempotency, distributed transactions |

---

## Phase 3: Behavioral Interview Prep

> **Goal**: Tell compelling stories that demonstrate senior-level impact.

### STAR+ Method

```
S — SITUATION: Set context (team, company, stakes, constraints)
T — TASK: Your specific responsibility (not the team's)
A — ACTION: What YOU did — be specific (technologies, decisions, conversations)
R — RESULT: Quantified outcome (metrics, revenue, time saved, users impacted)
+ — REFLECTION: What you learned, what you'd do differently
```

### Story Bank (Prepare 8-10 Stories)

You need stories that cover these themes:

| Theme | Example Question |
|-------|-----------------|
| **Technical Leadership** | "Tell me about a time you led a major technical decision" |
| **Conflict Resolution** | "Describe a disagreement with a team member/manager" |
| **Ambiguity** | "Tell me about a project with unclear requirements" |
| **Failure & Learning** | "Tell me about a time something went wrong" |
| **Mentoring** | "How have you helped junior engineers grow?" |
| **Cross-Team Collaboration** | "Tell me about working across teams to deliver a project" |
| **Customer Impact** | "Tell me about a time you improved the user experience" |
| **Innovation** | "Tell me about something you built that wasn't asked for" |
| **Tight Deadline** | "Tell me about delivering under pressure" |
| **Data-Driven Decision** | "Tell me about using data to make a decision" |

### Company-Specific Prep

| Company | Focus | Key Principles |
|---------|-------|---------------|
| **Amazon** | Leadership Principles (16 LPs) | Customer Obsession, Ownership, Bias for Action, Disagree & Commit, Earn Trust |
| **Google** | Googleyness + Leadership | Cognitive ability, role-related knowledge, general cognitive ability, leadership |
| **Meta** | Impact + Collaboration | Move fast, be bold, focus on impact, build social value |
| **Apple** | Craft + Detail | Attention to detail, design thinking, passion for the product |
| **Microsoft** | Growth Mindset | Learn-it-all vs know-it-all, collaboration, customer empathy |

---

## Phase 4: Offer Negotiation

> **Goal**: Maximize your total compensation package.

### Framework

```
1. NEVER give a number first
2. Get MULTIPLE offers if possible (leverage)
3. Negotiate total comp (base + equity + bonus + signing)
4. Consider: team, growth, WLB, location, mission
5. Be professional and grateful — not adversarial
6. Get it in writing
```

### Compensation Components

| Component | What to Negotiate |
|-----------|------------------|
| Base Salary | Band limits, ask for top of band |
| Equity (RSUs/Options) | Vesting schedule, refresh grants, strike price |
| Signing Bonus | One-time, can often be increased |
| Annual Bonus | Target %, actual variability |
| Relocation | If applicable, often generous |
| Other | PTO, start date, title, team placement, remote flexibility |

---

## Progress Tracking

- Save prep materials under `interview/` folder
- Create `interview/progress.md` to track completed topics
- Save your STAR stories in `interview/stories.md`
- Track solved problems in `interview/problems-log.md`
- Log mock interview feedback in `interview/mock-logs.md`

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| Cracking the Coding Interview | Book | Coding interview fundamentals |
| System Design Interview (Alex Xu) | Book | System design prep |
| Behavioral Interview Guide (levels.fyi) | Article | STAR stories and frameworks |
| interviewing.io | Platform | Mock interviews with engineers |
| Pramp | Platform | Free peer mock interviews |
| Glassdoor | Reference | Company-specific interview questions |
| levels.fyi | Reference | Compensation benchmarks |
