#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Create a comprehensive learning roadmap for a skill.

.DESCRIPTION
    This script generates a detailed learning roadmap with resources, timeline,
    and learning strategy. It wraps the teachme.roadmap agent workflow.

.PARAMETER SkillId
    The skill ID to create roadmap for (defaults to active skill)

.PARAMETER Force
    Overwrite existing roadmap if it exists

.EXAMPLE
    .\setup-roadmap.ps1
    
.EXAMPLE
    .\setup-roadmap.ps1 -SkillId "001-dynamic-programming" -Force
#>

param(
    [Parameter(Position=0)]
    [string]$SkillId = "",
    
    [Parameter()]
    [switch]$Force
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
Write-TeachHeader "Setup Learning Roadmap"

# Get repository root
$repoRoot = Get-RepoRoot
if (-not $repoRoot) {
    Write-Failure "Could not find Teach Me root directory (.teach/)"
    exit 1
}

# Get skill ID
if (-not $SkillId) {
    $SkillId = Get-ActiveSkill
    if (-not $SkillId) {
        Write-Failure "No active skill found"
        Write-Info "Use -SkillId parameter or create a skill first with /teachme.define"
        exit 1
    }
}

Write-Info "Creating roadmap for skill: $SkillId"

# Get skill path
$skillPath = Get-SkillPath -SkillId $SkillId
if (-not $skillPath) {
    Write-Failure "Skill not found: $SkillId"
    exit 1
}

# Check prerequisites
Write-Info "Checking prerequisites..."

# 1. Skill definition must exist
if (-not (Test-SkillFile -FileName "skill-definition.md" -SkillId $SkillId)) {
    Write-Failure "skill-definition.md not found"
    Write-Info "Run /teachme.define first to create skill definition"
    exit 1
}
Write-Success "Skill definition exists"

# 2. Philosophy recommended
if (-not (Test-HasPhilosophy)) {
    Write-Alert "Learning philosophy not found (recommended but not required)"
    Write-Info "Roadmap will be more personalized with a learning philosophy"
    Write-Host ""
    
    $response = Read-Host "Continue without philosophy? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Info "Run /teachme.philosophy to create your learning philosophy"
        exit 0
    }
}

# 3. Assessment recommended
$assessmentExists = Test-SkillFile -FileName "assessment-diagnostic.md" -SkillId $SkillId
if (-not $assessmentExists) {
    Write-Alert "No assessment found (recommended but not required)"
    Write-Info "Roadmap will be more customized if you run /teachme.assess first"
    Write-Host ""
    
    $response = Read-Host "Continue without assessment? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Info "Run /teachme.assess to evaluate your current level first"
        exit 0
    }
} else {
    Write-Success "Assessment found - roadmap will be customized to your level"
}

# Check if roadmap already exists
$roadmapPath = Join-Path $skillPath "roadmap.md"
if ((Test-Path $roadmapPath) -and -not $Force) {
    Write-Alert "Roadmap already exists"
    Write-Host "Path: $roadmapPath"
    Write-Host ""
    
    $response = Read-Host "Overwrite existing roadmap? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Info "Aborted. Use -Force to overwrite without prompting"
        exit 0
    }
}

# Copy roadmap template
$templatePath = Join-Path $repoRoot ".teach\templates\roadmap-template.md"
if (-not (Test-Path $templatePath)) {
    Write-Failure "Roadmap template not found: $templatePath"
    exit 1
}

try {
    Copy-Item $templatePath $roadmapPath -Force
    Write-Success "Created roadmap from template"
} catch {
    Write-Failure "Could not copy roadmap template: $_"
    exit 1
}

# Read skill definition to extract basic info
$definitionPath = Join-Path $skillPath "skill-definition.md"
$skillName = "Unknown Skill"
$domain = "general"

try {
    $definitionContent = Get-Content $definitionPath -Raw
    if ($definitionContent -match '# Skill Definition:\s*(.+)') {
        $skillName = $matches[1].Trim()
    }
    if ($definitionContent -match '(?m)^Domain:\s*(.+)$') {
        $domain = $matches[1].Trim().ToLower()
    }
} catch {
    Write-Alert "Could not parse skill definition"
}

# Update roadmap with skill info
try {
    $content = Get-Content $roadmapPath -Raw
    $content = $content -replace '\[SKILL_NAME\]', $skillName
    $content = $content -replace '\[SKILL_ID\]', $SkillId
    $content = $content -replace '\[YYYY-MM-DD\]', (Get-Date -Format "yyyy-MM-dd")
    $content = $content -replace '\[PATH_TO_SKILL_DEFINITION\]', "skill-definition.md"
    
    Set-Content $roadmapPath $content
    Write-Success "Updated roadmap metadata"
} catch {
    Write-Alert "Could not update roadmap metadata: $_"
}

# Update progress
$progress = Get-SkillProgress -SkillId $SkillId
if ($progress) {
    try {
        $updates = @{
            skill_status = "planning"
            current_phase = "Phase 0: Planning"
        }
        Update-SkillProgress -Updates $updates -SkillId $SkillId
        Write-Success "Updated progress status"
    } catch {
        Write-Alert "Could not update progress: $_"
    }
}

# Check for domain-specific roadmap template
$domainTemplate = Join-Path $repoRoot ".teach\domains\$domain\roadmap-template.md"
if (Test-Path $domainTemplate) {
    Write-Info "Found domain-specific roadmap template for: $domain"
    Write-Host "Consider incorporating domain-specific guidance from:"
    Write-Host $domainTemplate -ForegroundColor Cyan
}

# Print next steps
Write-Host ""
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "  ✓ Roadmap Template Created!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "Roadmap: " -NoNewline
Write-Host $roadmapPath -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Customize the roadmap with your preferences:" -ForegroundColor White
Write-Host "     - Learning resources (books, courses, videos)" -ForegroundColor Gray
Write-Host "     - Time commitment and timeline" -ForegroundColor Gray
Write-Host "     - Practice platforms and tools" -ForegroundColor Gray
Write-Host "  2. Review and adjust the 3-phase module sequence" -ForegroundColor White
Write-Host "  3. Run /teachme.validate to check consistency" -ForegroundColor White
Write-Host "  4. Run /teachme.modules to create detailed modules" -ForegroundColor White
Write-Host ""
Write-Info "The /teachme.roadmap agent can help fill in details automatically"
Write-Host ""

exit 0
