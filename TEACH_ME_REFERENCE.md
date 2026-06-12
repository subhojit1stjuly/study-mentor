# 🎓 Teach Me Learning System - Working Professional Setup

This repository uses the **Teach Me** structured learning system optimized for working professionals.

## 📍 Teach Me Location
**Git Submodule**: `D:\Projects\CS_AI_Study\teach_me\` (from https://github.com/subhojit1stjuly/teach_me)

> 💡 The teach_me system is now a git submodule! Updates can be pulled with:
> ```bash
> cd teach_me
> git pull origin master
> ```

## ⏰ Your Study Schedule (Working Professional)

**Monday-Friday**:
- 🌅 Morning: 1 hour (7:00-8:00 AM) - Theory & concepts
- 🌙 Evening: 2 hours (8:00-10:00 PM) - Practice & coding

**Saturday-Sunday**:
- 🎯 Weekend: 8 hours/day - Deep work & projects

**Total**: ~31 hours/week (Perfect for professional upskilling!)

## 🔄 Optimized Daily Workflow

### ☀️ Morning Routine (1 hour) - Theory Focus

**Monday-Friday 7:00-8:00 AM** - Before work

```powershell
cd D:\Projects\CS_AI_Study

# Quick review (5 min)
# - Check yesterday's progress
# - Review learning objectives for today

# Study session (50 min)
/teachme.learn
# - Read concepts from roadmap
# - Watch video lectures
# - Review patterns/algorithms
# - Take notes

# Quick wrap-up (5 min)
# - Mark module as "in progress"
# - Bookmark stopping point
```

**Goal**: Understand concepts before practicing at night

---

### 🌙 Evening Routine (2 hours) - Practice Focus

**Monday-Friday 8:00-10:00 PM** - After work

```powershell
cd D:\Projects\CS_AI_Study

# Warm-up (10 min)
# - Review morning concepts
# - Read teach_me exercises for today

# Coding practice (1h 40min)
# - Solve 1-2 LeetCode problems (45 min each)
# - Write solutions in algorithms/ directory
# - Document approach and learnings

# Update progress (10 min)
cd ..\ShowCase\agentAi\teach_me
# - Update progress.json
# - Check off completed exercises
# - Prepare tomorrow's morning reading
```

**Goal**: Apply morning theory to real problems

---

### 🎯 Weekend Deep Dive (8 hours/day)

**Saturday-Sunday** - Focused learning blocks

#### Saturday Schedule (8 hours)
```
09:00-11:00 (2h): Study Block 1
  - Deep dive into complex topics
  - Work through teach_me modules
  
11:00-11:15: Break ☕

11:15-13:15 (2h): Study Block 2
  - Continue module work
  - Practice medium/hard problems

13:15-14:00: Lunch Break 🍽️

14:00-16:00 (2h): Study Block 3
  - Solve 3-4 problems
  - Code in CS_AI_Study

16:00-16:15: Break ☕

16:15-18:00 (1h 45min): Study Block 4
  - Review week's learning
  - Update all progress
  - Plan next week
```

**Goal**: Make major progress on current skill

---

## 📊 Skill Mapping (Your 12-Month Plan)

| Timeline | teach_me Skill | CS_AI_Study Directory | Weekly Time Split |
|----------|----------------|----------------------|-------------------|
| **Weeks 1-4** | 003-arrays-and-strings | algorithms/ | Morning: Theory<br>Evening: LC Easy<br>Weekend: LC Medium |
| **Weeks 5-8** | 012-linked-lists | algorithms/ | Same pattern |
| **Weeks 9-12** | 010-stack-and-queue | algorithms/ | Same pattern |
| **Weeks 13-16** | 013-hashing, 007-sorting | algorithms/ | Same pattern |
| **Weeks 17-20** | 011-heap | algorithms/ | Same pattern |
| **Weeks 21-28** | 002-graphs, 001-dp | algorithms/ | Morning: Theory<br>Evening: LC Med<br>Weekend: LC Hard |
| **Weeks 29-36** | 006-greedy, 005-backtracking | algorithms/ | Same pattern |
| **Weeks 37-44** | ML/AI skills | ai/, ml/ | Projects on weekends |
| **Weeks 45-52** | System Design + Mock interviews | system-design/ | Mock interviews weekends |

## 🎯 Weekly Study Template

### Weekly Breakdown (31 hours)

**Weekday Evenings (10 hrs)**:
- Solve 10-12 LeetCode problems
- 2-3 problems per night (Monday-Friday)
- Focus: Medium difficulty (with some Easy warm-ups)

**Weekend (16 hrs)**:
- Complete 2-3 teach_me modules
- Solve 6-8 LeetCode problems (including Hard)
- Work on capstone projects
- Weekly review and planning

### Sample Week (Month 1 - Arrays & Strings)

| Day | Time | Activity | teach_me | CS_AI_Study |
|-----|------|----------|----------|-------------|
| **Mon** | 1h AM | Read: Array patterns | Module 1.1 | - |
| | 2h PM | Solve: Two Sum, Best Time to Buy Stock | - | 2 Easy problems |
| **Tue** | 1h AM | Read: Sliding window technique | Module 1.2 | - |
| | 2h PM | Solve: Longest Substring, Max Subarray | - | 2 Medium problems |
| **Wed** | 1h AM | Read: Two pointers | Module 1.3 | - |
| | 2h PM | Solve: Container With Water, 3Sum | - | 2 Medium problems |
| **Thu** | 1h AM | Review week's patterns | Review | - |
| | 2h PM | Solve: Product Except Self, Rotate Array | - | 2 Medium problems |
| **Fri** | 1h AM | Read: String patterns | Module 1.4 | - |
| | 2h PM | Solve: Valid Anagram, Group Anagrams | - | 2 Easy/Medium |
| **Sat** | 8h | Deep dive: Complete Modules 1.5-1.7 | 3 modules | 4-5 problems (incl. 1 Hard) |
| **Sun** | 8h | Practice: Mixed problems + Review | Exercises | 4-5 problems + weekly review |

**Weekly Output**: 
- ✅ 7 teach_me modules completed
- ✅ 18-20 LeetCode problems solved
- ✅ All concepts documented

---

## 🚀 Quick Commands for Working Professionals

### Morning Quick Start (< 2 minutes)
```powershell
# Open teach_me in VS Code
code D:\Projects\ShowCase\agentAi\teach_me

# Check today's module
cd D:\Projects\ShowCase\agentAi\teach_me
$activeSkill = Get-Content ".\.teach\memory\active-skill.json" | ConvertFrom-Json
$skillId = $activeSkill.skill_id
Write-Host "📚 Today: $skillId" -ForegroundColor Cyan

# Start reading from roadmap
code ".\skills\$skillId\roadmap.md"
```

### Evening Quick Start (< 2 minutes)
```powershell
# Open CS_AI_Study for coding
code D:\Projects\CS_AI_Study

# Check exercises for today
cd D:\Projects\ShowCase\agentAi\teach_me
$activeSkill = (Get-Content ".\.teach\memory\active-skill.json" | ConvertFrom-Json).skill_id
Get-ChildItem ".\skills\$activeSkill\exercises\" -File | Select-Object -First 3
```

### Weekend Batch Command
```powershell
# Open workspace with both repos
code --new-window D:\Projects\ShowCase\agentAi\teach_me D:\Projects\CS_AI_Study

# Or create workspace file (one-time setup)
$workspace = @{
    folders = @(
        @{ path = "D:\Projects\ShowCase\agentAi\teach_me"; name = "🎓 Learning System" }
        @{ path = "D:\Projects\CS_AI_Study"; name = "💻 Practice" }
    )
} | ConvertTo-Json
$workspace | Out-File "D:\Projects\GooglePrep.code-workspace"

# Then just open:
code "D:\Projects\GooglePrep.code-workspace"
```

---

## 📈 Progress Tracking (Weekly Habit)

### Sunday Evening Review (30 min)

```powershell
cd D:\Projects\ShowCase\agentAi\teach_me

# 1. Check week's completion (5 min)
Get-ChildItem .\skills -Directory | ForEach-Object {
    if (Test-Path "$_\progress.json") {
        $p = Get-Content "$_\progress.json" -Raw | ConvertFrom-Json
        if ($p.skill_status -eq "learning") {
            $completion = if ($p.total_modules -gt 0) { 
                [math]::Round(($p.modules_completed / $p.total_modules) * 100, 1) 
            } else { 0 }
            Write-Host "📊 $($_.Name): $($p.modules_completed)/$($p.total_modules) modules ($completion%)" -ForegroundColor Cyan
            Write-Host "   Hours this week: $($p.weekly_hours)" -ForegroundColor Gray
        }
    }
}

# 2. Count problems solved (10 min)
cd D:\Projects\CS_AI_Study
# Review git log for week's commits
git log --since="7 days ago" --oneline --all

# 3. Update MASTER_ROADMAP.md (10 min)
# - Mark completed milestones
# - Adjust timeline if needed
# - Celebrate wins! 🎉

# 4. Plan next week (5 min)
# - Set goals for next 5 weekdays
# - Plan weekend deep dive topic
```

---

## 💡 Pro Tips for Working Professionals

### 1. **Protect Your Morning Study Time**
- Set alarm 1h 15min before work start
- Study in same location (routine = discipline)
- Phone on airplane mode
- Coffee ready the night before ☕

### 2. **Optimize Evening Sessions**
- Have dinner before 8 PM study time
- Clear desk, close distractions
- Use Pomodoro: 50 min work + 10 min break
- Track problems in spreadsheet

### 3. **Maximize Weekend Deep Dives**
- **Saturday = New concepts** (teach_me modules)
- **Sunday = Pure practice** (CS_AI_Study problems)
- Batch similar problems (all DP, all graphs, etc.)
- Take proper breaks - this is a marathon!

### 4. **Track Time Honestly**
```json
// Update progress.json weekly
{
  "total_hours_actual": 125.5,
  "weekly_breakdown": {
    "weekday_morning": 5.0,
    "weekday_evening": 10.0,
    "weekend": 16.0
  },
  "last_updated": "2026-06-15"
}
```

### 5. **Use Commute Time (Optional)**
- Review flashcards (Anki)
- Watch algorithm videos (2x speed)
- Listen to system design podcasts
- **Bonus**: +5-10 hrs/week if you commute!

---

## 🎯 Realistic Skill Completion Timeline

Based on **31 hrs/week** (professional pace):

| Skill | Estimated Time | Timeline | Status |
|-------|---------------|----------|--------|
| 003-arrays-and-strings | 40 hours | 5-6 weeks | Start here |
| 012-linked-lists | 25 hours | 3-4 weeks | |
| 010-stack-and-queue | 20 hours | 2-3 weeks | |
| 013-hashing-hash-tables | 20 hours | 2-3 weeks | |
| 007-binary-search-sorting | 25 hours | 3-4 weeks | |
| 011-heap-priority-queue | 30 hours | 4 weeks | |
| 002-graph-algorithms | 50 hours | 6-8 weeks | Deep skill |
| 001-dynamic-programming | 60 hours | 8-10 weeks | Most time |
| 006-greedy-algorithms | 25 hours | 3-4 weeks | |
| 005-backtracking-recursion | 30 hours | 4 weeks | |

**Total DSA**: ~325 hours = ~10-11 months at 31 hrs/week ✅

**Remaining time**: ML + System Design + Mock Interviews

---

## 🚦 Getting Started (Tonight!)

### ⏰ **Tonight's 2-Hour Session** (Set Up Everything)

**8:00-8:15 PM** (15 min): Setup
```powershell
# 1. Create workspace file
code --new-window D:\Projects\ShowCase\agentAi\teach_me D:\Projects\CS_AI_Study

# 2. This reference is already in CS_AI_Study ✅
```

**8:15-8:30 PM** (15 min): Create Philosophy
```powershell
cd D:\Projects\ShowCase\agentAi\teach_me
# In GitHub Copilot Chat: /teachme.philosophy

# Include:
# - Schedule: 1h morning + 2h evening + 16h weekend = 31h/week
# - Timeline: 12 months (March 2026 → March 2027)
# - Learning style: Theory in morning, practice at night
# - Pace: Professional (working full-time)
# - Goal: Google L5/L6 (Senior SWE / Senior AI Engineer)
```

**8:30-9:00 PM** (30 min): Assess First Skill
```powershell
# Recommended: Start with Arrays & Strings (most foundational)
# In Copilot Chat: /teachme.assess
# Choose skill: 003-arrays-and-strings
```

**9:00-9:30 PM** (30 min): Generate Roadmap
```powershell
# In Copilot Chat: /teachme.roadmap
# AI will create personalized 5-6 week plan based on your assessment
```

**9:30-10:00 PM** (30 min): Solve First Problem!
```powershell
cd D:\Projects\CS_AI_Study\algorithms

# Warm-up: LC-1 Two Sum (Easy)
# Goal: Get familiar with CS_AI_Study workflow
# Document solution with comments
```

---

### 📅 **Tomorrow Morning** (First Real Session)

**7:00-8:00 AM**:
```powershell
cd D:\Projects\ShowCase\agentAi\teach_me

# Generate detailed modules
# In Copilot Chat: /teachme.modules

# Start Module 1.1 - Array Fundamentals
# Read, take notes, prepare for evening practice
```

**Tomorrow Evening 8:00-10:00 PM**:
```powershell
# Solve 2 problems from Module 1.1 exercises
# Update progress
# Feel the momentum! 🚀
```

---

## 📚 Key Files Reference

**teach_me** (Learning system):
- `.teach/memory/philosophy.md` - Your professional learning strategy
- `skills/003-arrays-and-strings/roadmap.md` - Your first 5-6 weeks
- `skills/003-arrays-and-strings/modules.md` - Daily breakdown
- `skills/003-arrays-and-strings/progress.json` - Track your 31 hrs/week

**CS_AI_Study** (Practice workspace):
- `MASTER_ROADMAP.md` - 12-month overview
- `algorithms/` - All your solutions
- `TEACH_ME_REFERENCE.md` - This file!

---

**Ready to start tonight?** 🚀

```powershell
cd D:\Projects\ShowCase\agentAi\teach_me
# In GitHub Copilot Chat: /teachme.philosophy
```

Then follow the 2-hour setup above. By 10 PM, you'll have:
- ✅ Learning philosophy defined
- ✅ First skill assessed
- ✅ Personalized roadmap generated
- ✅ First problem solved

**Let's do this!** 💪📚🎯
