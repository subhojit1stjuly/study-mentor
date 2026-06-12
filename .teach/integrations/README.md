# Teach Me - Integration Guide

This document explains how to integrate the Teach Me learning system with different AI assistants and development tools.

## GitHub Copilot Integration

### Setup

1. **Agent Registration**

   The Teach Me agents are defined in `.teach/agents/` and can be invoked using the `/teachme.*` command pattern:
   
   - `/teachme.philosophy` - Create learning philosophy
   - `/teachme.define` - Define new skill
   - `/teachme.assess` - Assess knowledge level
   - `/teachme.roadmap` - Create learning roadmap
   - `/teachme.validate` - Validate learning path
   - `/teachme.modules` - Generate learning modules
   - `/teachme.learn` - Start learning session

2. **VS Code Settings**

   Copy or merge `.vscode/teach-me-settings.json` into your `.vscode/settings.json`:
   
   ```json
   {
     "chat.tools.terminal.autoApprove": {
       ".teach/scripts/powershell/": true
     },
     "chat.promptFilesRecommendations": {
       "teachme.philosophy": true,
       "teachme.define": true,
       "teachme.assess": true,
       "teachme.roadmap": true,
       "teachme.validate": true,
       "teachme.modules": true,
       "teachme.learn": true
     }
   }
   ```

3. **Enable Agent Discovery**

   Ensure `.teach/agents/` directory is in your workspace and agent files have `.agent.md` extension.

### Usage with GitHub Copilot

Open GitHub Copilot Chat and use the slash commands:

```
/teachme.define I want to master dynamic programming
```

The agent will guide you through the learning workflow.

## Claude / Other AI Assistants

### Integration via Context Files

1. **Share Agent Instructions**

   When starting a conversation, provide context:
   
   ```
   I'm using the Teach Me learning system. The agent workflow is defined in:
   .teach/agents/teachme.[step].agent.md
   
   Current step: [philosophy/define/assess/roadmap/validate/modules/learn]
   ```

2. **Use PowerShell Scripts**

   The PowerShell scripts can be run independently:
   
   ```powershell
   .teach/scripts/powershell/create-new-skill.ps1 -SkillName "React Hooks"
   ```

3. **Manual Workflow**

   Follow the agent outlines manually and have AI help with specific steps.

## Command-Line Integration

### PowerShell Module (Optional)

Create a PowerShell module for easy access:

```powershell
# In your PowerShell profile
$TeachMePath = "D:\Projects\ShowCase\agentAi\teach_me"
function Invoke-TeachMe {
    param([string]$Command)
    & "$TeachMePath\.teach\scripts\powershell\$Command.ps1" @args
}

# Usage
Invoke-TeachMe create-new-skill -SkillName "System Design"
```

### Aliases

Add to your profile:

```powershell
Set-Alias new-skill "$TeachMePath\.teach\scripts\powershell\create-new-skill.ps1"
Set-Alias roadmap "$TeachMePath\.teach\scripts\powershell\setup-roadmap.ps1"
Set-Alias modules "$TeachMePath\.teach\scripts\powershell\setup-modules.ps1"
```

## MCP Server Integration (Future)

The Teach Me system could be exposed as an MCP (Model Context Protocol) server:

### Proposed MCP Tools

- `teachme_create_skill` - Create new skill
- `teachme_get_progress` - Get learning progress
- `teachme_update_module` - Update module completion
- `teachme_generate_exercises` - Generate practice problems
- `teachme_assess_knowledge` - Run assessment

### Proposed MCP Resources

- `teachme://skills` - List all skills
- `teachme://skill/{id}` - Get skill details
- `teachme://philosophy` - Learning philosophy
- `teachme://active` - Active skill info

### Implementation

See `.teach/integrations/mcp/` for future MCP server implementation.

## Web Dashboard Integration (Future)

A web-based dashboard could provide:

- Progress visualization
- Module completion tracking
- Exercise submission and grading
- Community features (study groups, shared roadmaps)
- Integration with learning platforms (LeetCode, Kaggle, etc.)

## API Integration (Future)

RESTful API for programmatic access:

```
GET  /api/skills
POST /api/skills
GET  /api/skills/{id}
PUT  /api/skills/{id}/progress
GET  /api/skills/{id}/modules
POST /api/skills/{id}/modules/{module_id}/complete
```

## Learning Platform Integration

### LeetCode

Link practice modules to LeetCode problem sets:

```markdown
## Practice Problems
- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
```

### Kaggle

For ML skills, link to Kaggle competitions and datasets:

```markdown
## Datasets
- [Titanic](https://www.kaggle.com/c/titanic)
- [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
```

### YouTube / Course Platforms

Embed video resources:

```markdown
## Video Resources
- [CS50 Algorithms](https://www.youtube.com/watch?v=...)
- [Coursera ML Course](https://www.coursera.org/...)
```

## Export / Import

### Export Learning Path

```powershell
# Export skill for sharing
Export-TeachMeSkill -SkillId "001-dynamic-programming" -OutputPath "./exported-skill.json"
```

### Import Learning Path

```powershell
# Import shared skill
Import-TeachMeSkill -InputPath "./exported-skill.json"
```

### Share Templates

Domain-specific templates in `.teach/domains/` can be shared:

```
.teach/domains/competitive-coding/
.teach/domains/machine-learning/
.teach/domains/web-development/
```

## Community Integration

### GitHub Repository Template

Create a template repository with:
- `.teach/` system directory
- Sample skills
- Domain templates
- Documentation

### Discussion Forums

Link to community:
- GitHub Discussions
- Discord server
- Reddit community
- Stack Overflow tag

---

## Current Integration Status

✅ **Implemented**:
- PowerShell automation scripts
- Agent workflow files
- Template system
- VS Code settings
- Manifest files

🔄 **In Progress**:
- Domain-specific templates
- Sample skills
- Documentation

📋 **Planned**:
- MCP server implementation
- Web dashboard
- API endpoints
- Platform integrations
- Community features

---

For questions or contributions, see the main README.md
