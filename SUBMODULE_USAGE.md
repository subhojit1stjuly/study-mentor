# 🔄 Git Submodule Workflows - teach_me System

**CS_AI_Study** now uses **teach_me** as a git submodule for reusable, version-controlled learning infrastructure.

---

## 📦 What is a Git Submodule?

A **submodule** is a git repository embedded inside another git repository. Think of it as a link to a specific version of another repo.

**Benefits**:
- ✅ **Single source of truth**: teach_me lives at https://github.com/subhojit1stjuly/teach_me
- ✅ **Auto-updates**: Pull latest teach_me changes without manual copying
- ✅ **Reusable**: Add teach_me to any project with one command
- ✅ **Version control**: Lock to specific teach_me versions if needed

**Current Setup**:
```
CS_AI_Study/
├── teach_me/               # Git submodule (https://github.com/subhojit1stjuly/teach_me)
├── .github/agents/         # Agents injected from teach_me
└── .gitmodules             # Submodule configuration
```

---

## 🚀 Common Workflows

### **1. Clone CS_AI_Study (New Machine)**

When cloning CS_AI_Study to a new machine, you need to also initialize the submodule:

```bash
# Option A: Clone with submodules (recommended)
git clone --recurse-submodules https://github.com/subhojit1stjuly/study-mentor.git CS_AI_Study
cd CS_AI_Study

# Option B: Clone normally, then init submodule
git clone https://github.com/subhojit1stjuly/study-mentor.git CS_AI_Study
cd CS_AI_Study
git submodule init
git submodule update
```

**Then inject agents** (if using copy method):
```powershell
# No admin needed (copy method)
.\teach_me\.teach\scripts\powershell\inject-agents.ps1 -Method copy

# Or with admin (symlink method - auto-updates)
# Run PowerShell as Administrator:
.\teach_me\.teach\scripts\powershell\inject-agents.ps1 -Method symlink
```

**Verify**:
```bash
# Check submodule status
git submodule status

# Should show:
# f54de6a... teach_me (heads/master)

# Check agents
ls .github/agents/teachme.*.agent.md
# Should list 7 agents
```

---

### **2. Update teach_me System**

When teach_me repo gets updates (new features, bug fixes, new skills), pull them:

```bash
cd D:\Projects\CS_AI_Study

# Enter submodule
cd teach_me

# Pull latest changes
git pull origin master

# Return to main repo
cd ..

# Commit the updated submodule reference
git add teach_me
git commit -m "Update teach_me submodule to latest"
git push
```

**If using copy method for agents**, re-inject after update:
```powershell
.\teach_me\.teach\scripts\powershell\inject-agents.ps1 -Method copy
git add .github/agents
git commit -m "Update agents from teach_me"
git push
```

**If using symlink method**, agents auto-update! No re-injection needed. ✨

---

### **3. Check Submodule Status**

```bash
cd D:\Projects\CS_AI_Study

# Check current submodule commit
git submodule status

# See if submodule has uncommitted changes
cd teach_me
git status
cd ..

# See if submodule has updates available
cd teach_me
git fetch
git status
cd ..
```

---

### **4. Lock teach_me to Specific Version**

If you want stability (e.g., during exam prep), lock to a specific version:

```bash
cd D:\Projects\CS_AI_Study\teach_me

# See available versions
git tag
# Or: git log --oneline

# Checkout specific commit or tag
git checkout v1.0.0
# Or: git checkout f54de6a

cd ..

# Commit the locked version
git add teach_me
git commit -m "Lock teach_me to v1.0.0 for stability"
git push
```

**To unlock and return to latest**:
```bash
cd teach_me
git checkout master
git pull
cd ..
git add teach_me
git commit -m "Update teach_me to latest"
git push
```

---

### **5. Add teach_me to Another Project**

Want to use teach_me in a different project? Easy!

```bash
cd D:\Projects\NewProject

# Add as submodule
git submodule add https://github.com/subhojit1stjuly/teach_me.git teach_me

# Initialize
git submodule init
git submodule update

# Inject agents
.\teach_me\.teach\scripts\powershell\inject-agents.ps1 -Method copy

# Commit
git add .gitmodules teach_me .github/agents
git commit -m "Add teach_me learning system"
git push
```

**Now both projects share the same teach_me system!** 🎉

---

### **6. Remove Submodule (if needed)**

To remove teach_me submodule and go back to copied files:

```bash
cd D:\Projects\CS_AI_Study

# 1. Deinitialize
git submodule deinit -f teach_me

# 2. Remove from git
git rm -f teach_me

# 3. Clean up .git/modules
rm -rf .git/modules/teach_me

# 4. Commit removal
git commit -m "Remove teach_me submodule"
git push

# 5. Manually copy teach_me files back if needed
```

---

## 🎯 Daily Usage (After Setup)

### **Morning Study Session**
```bash
cd D:\Projects\CS_AI_Study

# Open in VS Code
code .

# In Copilot Chat (Ctrl+Alt+I):
/teachme.learn
```

### **Check Progress**
```bash
# View current skill progress
cat teach_me/skills/003-arrays-and-strings/progress.json

# View roadmap
cat teach_me/skills/003-arrays-and-strings/roadmap.md
```

### **Practice Code**
```bash
# Your practice code goes in algorithms/ (not in submodule!)
cd algorithms/arrays-strings
# Code here...
```

**Important**: Never modify files inside `teach_me/` submodule for your work! Use:
- `algorithms/` for your practice code
- `ai/`, `ml/` for your projects
- `notes/` for your study notes

---

## 🔍 Troubleshooting

### **Submodule shows as modified but I didn't change anything**

This means the submodule has uncommitted changes or is at a different commit:

```bash
cd teach_me
git status
# If clean but still shows modified in parent:
git log -1
# Note the commit hash

cd ..
git diff teach_me
# Shows expected vs actual commit
```

**Fix**: Either commit changes in submodule, or reset:
```bash
cd teach_me
git checkout master
git pull
cd ..
git add teach_me
git commit -m "Update submodule reference"
```

### **Agents not found in Copilot CLI**

```bash
# Check agents exist
ls .github/agents/teachme.*.agent.md

# Re-inject if missing
.\teach_me\.teach\scripts\powershell\inject-agents.ps1 -Method copy

# Reload VS Code window
# Ctrl+Shift+P → "Reload Window"
```

### **Submodule folder is empty after clone**

You forgot to initialize the submodule:

```bash
git submodule init
git submodule update
```

Or re-clone with:
```bash
git clone --recurse-submodules <repo-url>
```

### **Can't pull submodule updates**

```bash
cd teach_me

# Check if you're in detached HEAD state
git branch
# If shows (HEAD detached at ...), checkout master:
git checkout master

# Now pull
git pull origin master
```

---

## 📚 Quick Reference Card

```bash
# Clone with submodules
git clone --recurse-submodules <repo>

# Update teach_me
cd teach_me && git pull && cd ..

# Check submodule status
git submodule status

# Add teach_me to new project
git submodule add https://github.com/subhojit1stjuly/teach_me.git teach_me

# Re-inject agents (if using copy)
.\teach_me\.teach\scripts\powershell\inject-agents.ps1 -Method copy

# Lock to version
cd teach_me && git checkout v1.0.0 && cd .. && git add teach_me

# Return to latest
cd teach_me && git checkout master && git pull && cd .. && git add teach_me
```

---

## 🎓 Philosophy: Why Submodules?

**Before** (copied files):
- teach_me in 2 places: `teach_me/` and `CS_AI_Study/`
- Manual sync needed
- Updates require copying again
- Can't reuse in other projects easily

**After** (submodule):
- teach_me in 1 place: GitHub
- CS_AI_Study references it
- Updates with `git pull`
- Reusable: `git submodule add` to any project

**Analogy**: 
- Copied files = Photocopying a textbook (out of date, duplicates)
- Submodule = Library link (always current, single source)

---

## 🚀 Next Steps

1. ✅ **Use teach_me**: Open VS Code, type `/teachme.philosophy`
2. ⏰ **Set reminder**: Update teach_me monthly with `cd teach_me && git pull`
3. 🌟 **Share**: Add teach_me submodule to other learning projects
4. 📈 **Track**: Your progress in `teach_me/skills/*/progress.json`

---

**Questions?** Check:
- [Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- CS_AI_STUDY_SETUP.md for teach_me workflow
- TEACH_ME_REFERENCE.md for working professional schedule

**Happy Learning!** 🎓
