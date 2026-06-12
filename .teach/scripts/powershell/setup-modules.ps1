#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Break down the learning roadmap into detailed modules with exercises.

.DESCRIPTION
    This script generates detailed learning modules from the roadmap, including
    specific exercises, resources, and checkpoints. Wraps teachme.modules agent.

.PARAMETER SkillId
    The skill ID to create modules for (defaults to active skill)

.PARAMETER Force
    Overwrite existing modules if they exist

.EXAMPLE
    .\setup-modules.ps1
    
.EXAMPLE
    .\setup-modules.ps1 -SkillId "001-dynamic-programming" -Force
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
Write-TeachHeader "Setup Learning Modules"

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
        Write-Info "Use -SkillId parameter or create a skill first"
        exit 1
    }
}

Write-Info "Creating modules for skill: $SkillId"

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
    Write-Info "Run /teachme.define first"
    exit 1
}
Write-Success "Skill definition exists"

# 2. Roadmap must exist
if (-not (Test-SkillFile -FileName "roadmap.md" -SkillId $SkillId)) {
    Write-Failure "roadmap.md not found"
    Write-Info "Run /teachme.roadmap first to create learning plan"
    exit 1
}
Write-Success "Roadmap exists"

# 3. Validation recommended
$validationExists = Test-SkillFile -FileName "validation-report.md" -SkillId $SkillId
if (-not $validationExists) {
    Write-Alert "No validation report found (recommended but not required)"
    Write-Info "Running /teachme.validate ensures your roadmap is consistent"
    Write-Host ""
    
    $response = Read-Host "Continue without validation? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Info "Run /teachme.validate to check roadmap consistency first"
        exit 0
    }
} else {
    Write-Success "Validation passed - roadmap is consistent"
}

# Check if modules already exist
$modulesPath = Join-Path $skillPath "modules.md"
if ((Test-Path $modulesPath) -and -not $Force) {
    Write-Alert "Modules already exist"
    Write-Host "Path: $modulesPath"
    Write-Host ""
    
    $response = Read-Host "Overwrite existing modules? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Info "Aborted. Use -Force to overwrite without prompting"
        exit 0
    }
}

# Copy modules template
$templatePath = Join-Path $repoRoot ".teach\templates\modules-template.md"
if (-not (Test-Path $templatePath)) {
    Write-Failure "Modules template not found: $templatePath"
    exit 1
}

try {
    Copy-Item $templatePath $modulesPath -Force
    Write-Success "Created modules from template"
} catch {
    Write-Failure "Could not copy modules template: $_"
    exit 1
}

# Read skill definition
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

# Update modules with skill info
try {
    $content = Get-Content $modulesPath -Raw
    $content = $content -replace '\[SKILL_NAME\]', $skillName
    $content = $content -replace '\[SKILL_ID\]', $SkillId
    $content = $content -replace '\[YYYY-MM-DD\]', (Get-Date -Format "yyyy-MM-dd")
    
    Set-Content $modulesPath $content
    Write-Success "Updated modules metadata"
} catch {
    Write-Alert "Could not update modules metadata: $_"
}

# Parse roadmap to extract module structure
Write-Info "Parsing roadmap structure..."
$roadmapPath = Join-Path $skillPath "roadmap.md"

try {
    $roadmapContent = Get-Content $roadmapPath -Raw
    
    # Extract estimated timeline
    $estimatedWeeks = 12  # Default
    if ($roadmapContent -match '(\d+)\s*(?:weeks?|months?)') {
        $estimatedWeeks = [int]$matches[1]
    }
    
    Write-Success "Estimated timeline: $estimatedWeeks weeks"
} catch {
    Write-Alert "Could not parse roadmap details"
}

# Initialize module tracking in progress.json
$progress = Get-SkillProgress -SkillId $SkillId
if ($progress) {
    try {
        $updates = @{
            skill_status = "ready"
            current_phase = "Phase 1: Foundation"
            total_modules = 0
            modules_completed = 0
            modules = @()
        }
        Update-SkillProgress -Updates $updates -SkillId $SkillId
        Write-Success "Initialized module tracking"
    } catch {
        Write-Alert "Could not update progress: $_"
    }
}

# Check for domain-specific module patterns
$domainTemplate = Join-Path $repoRoot ".teach\domains\$domain\modules-template.md"
if (Test-Path $domainTemplate) {
    Write-Info "Found domain-specific module template for: $domain"
    Write-Host "Consider incorporating domain-specific exercises from:"
    Write-Host $domainTemplate -ForegroundColor Cyan
}

# Create exercises directory structure
$exercisesDir = Join-Path $skillPath "exercises"
if (-not (Test-Path $exercisesDir)) {
    New-Item -ItemType Directory -Path $exercisesDir -Force | Out-Null
}

# Create phase directories for exercises
@("phase-1-foundation", "phase-2-development", "phase-3-mastery") | ForEach-Object {
    $phaseDir = Join-Path $exercisesDir $_
    if (-not (Test-Path $phaseDir)) {
        New-Item -ItemType Directory -Path $phaseDir -Force | Out-Null
    }
}
Write-Success "Created exercise directory structure"

# Print next steps
Write-Host ""
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "  ✓ Module Template Created!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "Modules: " -NoNewline
Write-Host $modulesPath -ForegroundColor Cyan
Write-Host "Exercises: " -NoNewline
Write-Host $exercisesDir -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. The /teachme.modules agent will:" -ForegroundColor White
Write-Host "     - Break roadmap into detailed daily modules" -ForegroundColor Gray
Write-Host "     - Generate practice exercises with solutions" -ForegroundColor Gray
Write-Host "     - Create checkpoint assessments" -ForegroundColor Gray
Write-Host "     - Set up spaced repetition schedule" -ForegroundColor Gray
Write-Host "  2. Run /teachme.modules to populate with AI-generated content" -ForegroundColor White
Write-Host "  3. Review and customize the generated modules" -ForegroundColor White
Write-Host "  4. Run /teachme.learn to begin your learning journey!" -ForegroundColor White
Write-Host ""
Write-Info "The module generation process may take a few minutes"
Write-Host ""

exit 0
