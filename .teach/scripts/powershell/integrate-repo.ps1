<#
.SYNOPSIS
    Integrate Teach Me system with an existing repository

.DESCRIPTION
    Copies or links the Teach Me learning system to an existing project,
    optionally creating project-specific skills

.PARAMETER TargetRepo
    Path to the existing repository

.PARAMETER Method
    Integration method: 'copy', 'symlink', or 'reference'

.PARAMETER CreateSkill
    Create a new skill specific to the target project

.EXAMPLE
    .\integrate-repo.ps1 -TargetRepo "D:\Projects\MyApp" -Method copy
    .\integrate-repo.ps1 -TargetRepo "D:\Projects\MyApp" -Method symlink -CreateSkill
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$TargetRepo,
    
    [Parameter(Mandatory=$false)]
    [ValidateSet('copy', 'symlink', 'reference')]
    [string]$Method = 'copy',
    
    [Parameter(Mandatory=$false)]
    [switch]$CreateSkill
)

# Load common utilities
. "$PSScriptRoot\common.ps1"

function Test-Administrator {
    $user = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($user)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

Write-TeachHeader "Integrate Teach Me System"

# Validate target repository
if (-not (Test-Path $TargetRepo)) {
    Write-Failure "Target repository not found: $TargetRepo"
    exit 1
}

Write-Info "Target repository: $TargetRepo"
Write-Info "Integration method: $Method"

$teachRoot = Find-TeachRoot
$repoRoot = Get-RepoRoot

switch ($Method) {
    'copy' {
        Write-Host "`nCopying Teach Me system..." -ForegroundColor Cyan
        
        # Copy .teach directory
        $targetTeach = Join-Path $TargetRepo ".teach"
        if (Test-Path $targetTeach) {
            Write-Alert ".teach directory already exists in target"
            $response = Read-Host "Overwrite? (y/N)"
            if ($response -ne 'y') {
                Write-Info "Aborted"
                exit 0
            }
            Remove-Item $targetTeach -Recurse -Force
        }
        
        Copy-Item -Path $teachRoot -Destination $targetTeach -Recurse
        Write-Success "Copied .teach/ directory"
        
        # Copy skills directory (empty structure)
        $targetSkills = Join-Path $TargetRepo "skills"
        if (-not (Test-Path $targetSkills)) {
            New-Item -ItemType Directory -Path $targetSkills | Out-Null
            Copy-Item -Path (Join-Path $repoRoot "skills\.gitkeep") -Destination $targetSkills -ErrorAction SilentlyContinue
            Write-Success "Created skills/ directory"
        }
        
        # Create integration README
        $integrationReadme = @"
# Teach Me Learning System

This repository includes the Teach Me learning system for personalized skill development.

## Integration Details
- Integrated on: $(Get-Date -Format "yyyy-MM-dd HH:mm")
- Method: Copy
- Source: $repoRoot

## Quick Start

1. Create your learning philosophy:
   ``````
   /teachme.philosophy
   ``````

2. Create a skill for this project:
   ``````powershell
   .\.teach\scripts\powershell\create-new-skill.ps1 -SkillName "Your Skill Name"
   ``````

3. Follow the learning workflow:
   - /teachme.assess - Evaluate your level
   - /teachme.roadmap - Create learning plan
   - /teachme.modules - Break into modules
   - /teachme.learn - Start learning!

## Documentation

See the main Teach Me documentation for full details:
$repoRoot\README.md
"@
        
        Set-Content -Path (Join-Path $TargetRepo "TEACH_ME.md") -Value $integrationReadme
        Write-Success "Created TEACH_ME.md documentation"
        
        Write-Host ""
        Write-Success "Integration complete!"
        Write-Host "`nNext steps:"
        Write-Host "  1. cd `"$TargetRepo`""
        Write-Host "  2. Review TEACH_ME.md"
        Write-Host "  3. Run: .\.teach\scripts\powershell\create-new-skill.ps1"
    }
    
    'symlink' {
        if (-not (Test-Administrator)) {
            Write-Failure "Symbolic links require Administrator privileges"
            Write-Info "Please run PowerShell as Administrator and try again"
            exit 1
        }
        
        Write-Host "`nCreating symbolic links..." -ForegroundColor Cyan
        
        # Create symlink for .teach
        $targetTeach = Join-Path $TargetRepo ".teach"
        if (Test-Path $targetTeach) {
            Write-Alert ".teach already exists in target"
            exit 1
        }
        
        New-Item -ItemType SymbolicLink -Path $targetTeach -Target $teachRoot | Out-Null
        Write-Success "Created symlink: .teach/ -> $teachRoot"
        
        # Create symlink for skills (optional - they might want separate skills)
        $response = Read-Host "Link skills directory too? (Y/n)"
        if ($response -ne 'n') {
            $targetSkills = Join-Path $TargetRepo "skills"
            $sourceSkills = Join-Path $repoRoot "skills"
            
            if (-not (Test-Path $targetSkills)) {
                New-Item -ItemType SymbolicLink -Path $targetSkills -Target $sourceSkills | Out-Null
                Write-Success "Created symlink: skills/ -> $sourceSkills"
            }
        }
        
        Write-Host ""
        Write-Success "Symbolic links created!"
        Write-Info "Changes in either location will sync automatically"
    }
    
    'reference' {
        Write-Host "`nCreating reference configuration..." -ForegroundColor Cyan
        
        $referenceConfig = @"
# Teach Me Reference Configuration

## Learning System Location
$repoRoot

## How to Use

### Option 1: Use commands from learning repo
``````powershell
cd $repoRoot
# Run learning commands here, reference this project in exercises
``````

### Option 2: Copy specific skills
``````powershell
# Copy just the skills you need
Copy-Item -Path "$repoRoot\skills\001-*" -Destination ".\learning" -Recurse
``````

### Option 3: Create project-specific skill
Create a skill in the main Teach Me repo that references this project:

``````markdown
# In skill-definition.md
## Related Project
Repository: $TargetRepo
Purpose: Apply learning to real project

## Practice Approach
1. Study concepts in Teach Me
2. Apply to code in: $TargetRepo
3. Track progress centrally
``````

## Quick Access Commands

``````powershell
# Open learning system
cd $repoRoot

# Create skill for this project
.\.teach\scripts\powershell\create-new-skill.ps1 -SkillName "$(Split-Path $TargetRepo -Leaf) Development"
``````
"@
        
        Set-Content -Path (Join-Path $TargetRepo ".teach-reference.md") -Value $referenceConfig
        Write-Success "Created .teach-reference.md"
        
        Write-Host ""
        Write-Info "Reference configuration created"
        Write-Info "See .teach-reference.md for usage instructions"
    }
}

# Optionally create a skill for this project
if ($CreateSkill) {
    $projectName = Split-Path $TargetRepo -Leaf
    Write-Host "`nCreating project-specific skill..." -ForegroundColor Cyan
    
    $skillName = Read-Host "Skill name (default: $projectName Development)"
    if ([string]::IsNullOrWhiteSpace($skillName)) {
        $skillName = "$projectName Development"
    }
    
    $description = Read-Host "Skill description"
    if ([string]::IsNullOrWhiteSpace($description)) {
        $description = "Master the technologies and patterns used in the $projectName project"
    }
    
    # Determine domain based on project type
    $domain = "web-development"  # Default
    Write-Host "`nAvailable domains:"
    Write-Host "  1. competitive-coding"
    Write-Host "  2. machine-learning"
    Write-Host "  3. ai-engineering"
    Write-Host "  4. web-development (default)"
    Write-Host "  5. system-design"
    
    $domainChoice = Read-Host "Select domain (1-5)"
    switch ($domainChoice) {
        '1' { $domain = 'competitive-coding' }
        '2' { $domain = 'machine-learning' }
        '3' { $domain = 'ai-engineering' }
        '4' { $domain = 'web-development' }
        '5' { $domain = 'system-design' }
    }
    
    # Run create-new-skill script
    & "$PSScriptRoot\create-new-skill.ps1" -SkillName $skillName -Domain $domain -Description $description -SetActive $true
    
    # Add project reference to skill definition
    $activeSkill = Get-ActiveSkill
    if ($activeSkill) {
        $skillPath = Get-SkillPath -SkillId $activeSkill
        $definitionPath = Join-Path $skillPath "skill-definition.md"
        
        if (Test-Path $definitionPath) {
            $projectReference = @"


## Related Project

**Repository**: $TargetRepo
**Purpose**: Apply learning to real-world codebase

### Practice Integration
- Study concepts in this skill
- Apply techniques in project repository  
- Reference project code in exercises
- Build features as capstone projects
"@
            Add-Content -Path $definitionPath -Value $projectReference
            Write-Success "Added project reference to skill definition"
        }
    }
}

Write-Host ""
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "  ✓ Integration Complete!" -ForegroundColor Green  
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
