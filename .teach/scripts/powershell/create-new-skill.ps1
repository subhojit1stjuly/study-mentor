#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Create a new learning skill with directory structure and initial files.

.DESCRIPTION
    This script creates a new skill directory with the necessary structure
    and initializes skill-definition.md and progress.json. It wraps the
    teachme.define agent workflow.

.PARAMETER SkillName
    The name of the skill to learn (e.g., "Dynamic Programming", "React Hooks")

.PARAMETER Description
    Optional description of what you want to learn

.PARAMETER Domain
    Optional domain category (competitive-coding, machine-learning, web-development, etc.)

.PARAMETER SetActive
    Set this skill as the active skill after creation (default: true)

.EXAMPLE
    .\create-new-skill.ps1 -SkillName "Dynamic Programming"
    
.EXAMPLE
    .\create-new-skill.ps1 -SkillName "React Hooks" -Domain "web-development" -Description "Master React Hooks for modern web development"
#>

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$SkillName,
    
    [Parameter(Position=1)]
    [string]$Description = "",
    
    [Parameter()]
    [ValidateSet("competitive-coding", "machine-learning", "ai-engineering", "web-development", "system-design", "data-science", "mobile-development", "devops", "other")]
    [string]$Domain = "",
    
    [Parameter()]
    [bool]$SetActive = $true
)

# Import common functions
$commonScript = Join-Path $PSScriptRoot "common.ps1"
if (Test-Path $commonScript) {
    . $commonScript
} else {
    Write-Error "Common script not found: $commonScript"
    exit 1
}

# Main script
Write-TeachHeader "Create New Learning Skill"

# Get repository root
$repoRoot = Get-RepoRoot
if (-not $repoRoot) {
    Write-Failure "Could not find Teach Me root directory (.teach/)"
    Write-Host "Make sure you're in a Teach Me workspace"
    exit 1
}

Write-Info "Repository root: $repoRoot"

# Check if philosophy exists (recommended)
if (-not (Test-HasPhilosophy)) {
    Write-Alert "Learning philosophy not found"
    Write-Host "It's recommended to create your learning philosophy first"
    Write-Host "Run: /teachme.philosophy or create one manually"
    Write-Host ""
    
    $response = Read-Host "Continue without philosophy? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Info "Aborted. Create philosophy first with /teachme.philosophy"
        exit 0
    }
}

# Generate skill ID
$skillId = Get-NextSkillId -SkillName $SkillName
Write-Info "Generated skill ID: $skillId"

# Create skill directory
$skillPath = Join-Path $repoRoot "skills\$skillId"
if (Test-Path $skillPath) {
    Write-Failure "Skill directory already exists: $skillPath"
    exit 1
}

try {
    New-Item -ItemType Directory -Path $skillPath -Force | Out-Null
    Write-Success "Created skill directory: $skillPath"
} catch {
    Write-Failure "Could not create skill directory: $_"
    exit 1
}

# Create exercises subdirectory
try {
    New-Item -ItemType Directory -Path (Join-Path $skillPath "exercises") -Force | Out-Null
    Write-Success "Created exercises directory"
} catch {
    Write-Failure "Could not create exercises directory: $_"
}

# Create projects subdirectory
try {
    New-Item -ItemType Directory -Path (Join-Path $skillPath "projects") -Force | Out-Null
    Write-Success "Created projects directory"
} catch {
    Write-Failure "Could not create projects directory: $_"
}

# Copy skill-definition template
$templatePath = Join-Path $repoRoot ".teach\templates\skill-definition-template.md"
$definitionPath = Join-Path $skillPath "skill-definition.md"

if (Test-Path $templatePath) {
    try {
        Copy-Item $templatePath $definitionPath
        
        # Replace placeholders
        $content = Get-Content $definitionPath -Raw
        $content = $content -replace '\[SKILL_NAME\]', $SkillName
        $content = $content -replace '\[SKILL_ID\]', $skillId
        $content = $content -replace '\[YYYY-MM-DD\]', (Get-Date -Format "yyyy-MM-dd")
        $content = $content -replace '\[BRIEF_DESCRIPTION\]', $(if ($Description) { $Description } else { "To be defined" })
        $content = $content -replace '\[DOMAIN\]', $(if ($Domain) { $Domain } else { "To be determined" })
        
        Set-Content $definitionPath $content
        Write-Success "Created skill-definition.md"
    } catch {
        Write-Failure "Could not create skill definition: $_"
    }
} else {
    Write-Alert "Template not found, creating basic skill-definition.md"
    
    $basicContent = @"
# Skill Definition: $SkillName

**Skill ID**: $skillId
**Created**: $(Get-Date -Format "yyyy-MM-dd")
**Domain**: $(if ($Domain) { $Domain } else { "To be determined" })

## Description

$Description

## Learning Objectives

### Priority 1 (Critical - Must Learn)
- [ ] **OBJ-001**: [Define your P1 objectives]

### Priority 2 (Important - Should Learn)
- [ ] **OBJ-002**: [Define your P2 objectives]

### Priority 3 (Nice to Have - Could Learn)
- [ ] **OBJ-003**: [Define your P3 objectives]

## Prerequisites

### Required Prerequisites
- **PRE-001**: [Required knowledge]

### Recommended Prerequisites
- **REC-001**: [Helpful but not required]

---
Next Step: Run '/teachme.assess' to evaluate your current level
"@
    
    Set-Content $definitionPath $basicContent
    Write-Success "Created basic skill-definition.md"
}

# Initialize progress.json
$progressPath = Join-Path $skillPath "progress.json"
$progressData = @{
    skill_id = $skillId
    skill_name = $SkillName
    skill_status = "defining"
    created_date = (Get-Date -Format "yyyy-MM-dd")
    last_updated = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    current_phase = "Phase 0: Setup"
    total_modules = 0
    modules_completed = 0
    total_hours_estimated = 0
    total_hours_actual = 0
}

try {
    $progressData | ConvertTo-Json -Depth 10 | Set-Content $progressPath
    Write-Success "Created progress.json"
} catch {
    Write-Failure "Could not create progress.json: $_"
}

# Create README
$readmePath = Join-Path $skillPath "README.md"
$readmeContent = @"
# $SkillName

**Skill ID**: $skillId
**Created**: $(Get-Date -Format "yyyy-MM-dd")

## Description

$Description

## Learning Path

This skill follows the Teach Me learning workflow:

1. **Define** (`/teachme.define`) - ✓ Complete
2. **Assess** (`/teachme.assess`) - Define learning objectives and assess current level
3. **Roadmap** (`/teachme.roadmap`) - Create comprehensive learning plan
4. **Validate** (`/teachme.validate`) - Verify consistency and completeness
5. **Modules** (`/teachme.modules`) - Break into detailed learning modules
6. **Learn** (`/teachme.learn`) - Execute and master the skill

## Files

- `skill-definition.md` - Learning objectives, prerequisites, success criteria
- `progress.json` - Current progress and completion tracking
- `assessment-*.md` - Diagnostic and checkpoint assessments
- `roadmap.md` - Comprehensive learning plan with resources
- `modules.md` - Detailed module breakdown with exercises
- `exercises/` - Practice problems and solutions
- `projects/` - Capstone and learning projects

## Next Steps

Run `/teachme.assess` to evaluate your current knowledge level and customize the learning path.
"@

Set-Content $readmePath $readmeContent
Write-Success "Created README.md"

# Set as active skill if requested
if ($SetActive) {
    $activeSkillPath = Join-Path $repoRoot ".teach\memory\active-skill.json"
    $activeData = @{
        skill_id = $skillId
        skill_name = $SkillName
        last_updated = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    }
    
    try {
        $activeData | ConvertTo-Json | Set-Content $activeSkillPath
        Write-Success "Set as active skill"
    } catch {
        Write-Alert "Could not set as active skill: $_"
    }
}

# Print summary
Write-Host ""
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "  ✓ Skill Created Successfully!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "Skill: " -NoNewline
Write-Host $SkillName -ForegroundColor Cyan
Write-Host "ID: " -NoNewline
Write-Host $skillId -ForegroundColor Cyan
Write-Host "Path: " -NoNewline
Write-Host $skillPath -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Review and complete skill-definition.md" -ForegroundColor White
Write-Host "  2. Run /teachme.assess to evaluate your current level" -ForegroundColor White
Write-Host "  3. Run /teachme.roadmap to create your learning path" -ForegroundColor White
Write-Host ""

exit 0
