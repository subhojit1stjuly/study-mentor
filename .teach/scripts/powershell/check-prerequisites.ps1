#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Check prerequisites for learning a skill or running a command.

.DESCRIPTION
    Validates that all prerequisites are met before starting a learning workflow
    step. Can check for philosophy, skill definition, roadmap, modules, etc.

.PARAMETER SkillId
    The skill ID to check (defaults to active skill)

.PARAMETER CheckPhilosophy
    Check if learning philosophy exists

.PARAMETER CheckSkillDefinition
    Check if skill definition exists

.PARAMETER CheckAssessment
    Check if assessment has been completed

.PARAMETER CheckRoadmap
    Check if roadmap exists

.PARAMETER CheckModules
    Check if modules exist

.PARAMETER All
    Check all prerequisites

.PARAMETER Quiet
    Suppress output, only return exit code (0 = pass, 1 = fail)

.EXAMPLE
    .\check-prerequisites.ps1 -All
    
.EXAMPLE
    .\check-prerequisites.ps1 -CheckRoadmap -SkillId "001-dynamic-programming"
    
.EXAMPLE
    .\check-prerequisites.ps1 -CheckPhilosophy -Quiet
#>

param(
    [Parameter(Position=0)]
    [string]$SkillId = "",
    
    [Parameter()]
    [switch]$CheckPhilosophy,
    
    [Parameter()]
    [switch]$CheckSkillDefinition,
    
    [Parameter()]
    [switch]$CheckAssessment,
    
    [Parameter()]
    [switch]$CheckRoadmap,
    
    [Parameter()]
    [switch]$CheckModules,
    
    [Parameter()]
    [switch]$All,
    
    [Parameter()]
    [switch]$Quiet
)

# Import common functions
$commonScript = Join-Path $PSScriptRoot "common.ps1"
if (Test-Path $commonScript) {
    . $commonScript
} else {
    if (-not $Quiet) {
        Write-Error "Common script not found: $commonScript"
    }
    exit 1
}

# Track pass/fail
$allPassed = $true
$checks = @()

# If All is specified, enable all checks
if ($All) {
    $CheckPhilosophy = $true
    $CheckSkillDefinition = $true
    $CheckAssessment = $true
    $CheckRoadmap = $true
    $CheckModules = $true
}

# If no checks specified, show usage
if (-not ($CheckPhilosophy -or $CheckSkillDefinition -or $CheckAssessment -or $CheckRoadmap -or $CheckModules)) {
    if (-not $Quiet) {
        Write-Host "Usage: check-prerequisites.ps1 [options]"
        Write-Host ""
        Write-Host "Options:"
        Write-Host "  -CheckPhilosophy       Check if learning philosophy exists"
        Write-Host "  -CheckSkillDefinition  Check if skill definition exists"
        Write-Host "  -CheckAssessment       Check if assessment completed"
        Write-Host "  -CheckRoadmap          Check if roadmap exists"
        Write-Host "  -CheckModules          Check if modules exist"
        Write-Host "  -All                   Check all prerequisites"
        Write-Host "  -SkillId <id>          Skill ID (defaults to active)"
        Write-Host "  -Quiet                 Suppress output"
        Write-Host ""
    }
    exit 0
}

if (-not $Quiet) {
    Write-TeachHeader "Prerequisite Check"
}

# Get repository root
$repoRoot = Get-RepoRoot
if (-not $repoRoot) {
    if (-not $Quiet) {
        Write-Failure "Could not find Teach Me root directory (.teach/)"
    }
    exit 1
}

# Check philosophy
if ($CheckPhilosophy) {
    $philosophyPath = Join-Path $repoRoot ".teach\memory\philosophy.md"
    if (Test-Path $philosophyPath) {
        $checks += [PSCustomObject]@{
            Check = "Learning Philosophy"
            Status = "✓ Pass"
            Message = "Philosophy file exists"
        }
        if (-not $Quiet) {
            Write-Success "Learning philosophy exists"
        }
    } else {
        $allPassed = $false
        $checks += [PSCustomObject]@{
            Check = "Learning Philosophy"
            Status = "✗ Fail"
            Message = "Philosophy not found. Run /teachme.philosophy"
        }
        if (-not $Quiet) {
            Write-Failure "Learning philosophy not found"
            Write-Info "Run /teachme.philosophy to create your learning philosophy"
        }
    }
}

# Get skill ID for skill-specific checks
if ($CheckSkillDefinition -or $CheckAssessment -or $CheckRoadmap -or $CheckModules) {
    if (-not $SkillId) {
        $SkillId = Get-ActiveSkill
        if (-not $SkillId) {
            if (-not $Quiet) {
                Write-Failure "No active skill found"
                Write-Info "Use -SkillId parameter or create a skill first"
            }
            exit 1
        }
    }
    
    $skillPath = Get-SkillPath -SkillId $SkillId
    if (-not $skillPath) {
        if (-not $Quiet) {
            Write-Failure "Skill not found: $SkillId"
        }
        exit 1
    }
    
    if (-not $Quiet) {
        Write-Info "Checking skill: $SkillId"
    }
}

# Check skill definition
if ($CheckSkillDefinition) {
    $definitionPath = Join-Path $skillPath "skill-definition.md"
    if (Test-Path $definitionPath) {
        # Check if it's populated (not just template)
        $content = Get-Content $definitionPath -Raw
        if ($content -match '\[.*?\]' -and $content -match 'PLACEHOLDER') {
            $allPassed = $false
            $checks += [PSCustomObject]@{
                Check = "Skill Definition"
                Status = "⚠ Warning"
                Message = "Definition exists but has placeholders"
            }
            if (-not $Quiet) {
                Write-Alert "Skill definition has placeholders to fill"
            }
        } else {
            $checks += [PSCustomObject]@{
                Check = "Skill Definition"
                Status = "✓ Pass"
                Message = "Definition complete"
            }
            if (-not $Quiet) {
                Write-Success "Skill definition exists and populated"
            }
        }
    } else {
        $allPassed = $false
        $checks += [PSCustomObject]@{
            Check = "Skill Definition"
            Status = "✗ Fail"
            Message = "Definition not found. Run /teachme.define"
        }
        if (-not $Quiet) {
            Write-Failure "Skill definition not found"
            Write-Info "Run /teachme.define to create skill definition"
        }
    }
}

# Check assessment
if ($CheckAssessment) {
    $assessmentPath = Join-Path $skillPath "assessment-diagnostic.md"
    if (Test-Path $assessmentPath) {
        $checks += [PSCustomObject]@{
            Check = "Assessment"
            Status = "✓ Pass"
            Message = "Diagnostic assessment completed"
        }
        if (-not $Quiet) {
            Write-Success "Assessment completed"
        }
    } else {
        # Assessment is recommended but not always required
        $checks += [PSCustomObject]@{
            Check = "Assessment"
            Status = "⚠ Recommended"
            Message = "No assessment found. Run /teachme.assess (recommended)"
        }
        if (-not $Quiet) {
            Write-Alert "No assessment found (recommended but not required)"
            Write-Info "Run /teachme.assess for personalized learning path"
        }
    }
}

# Check roadmap
if ($CheckRoadmap) {
    $roadmapPath = Join-Path $skillPath "roadmap.md"
    if (Test-Path $roadmapPath) {
        $checks += [PSCustomObject]@{
            Check = "Roadmap"
            Status = "✓ Pass"
            Message = "Learning roadmap exists"
        }
        if (-not $Quiet) {
            Write-Success "Roadmap exists"
        }
    } else {
        $allPassed = $false
        $checks += [PSCustomObject]@{
            Check = "Roadmap"
            Status = "✗ Fail"
            Message = "Roadmap not found. Run /teachme.roadmap"
        }
        if (-not $Quiet) {
            Write-Failure "Roadmap not found"
            Write-Info "Run /teachme.roadmap to create learning plan"
        }
    }
}

# Check modules
if ($CheckModules) {
    $modulesPath = Join-Path $skillPath "modules.md"
    if (Test-Path $modulesPath) {
        $checks += [PSCustomObject]@{
            Check = "Modules"
            Status = "✓ Pass"
            Message = "Learning modules exist"
        }
        if (-not $Quiet) {
            Write-Success "Modules exist"
        }
    } else {
        $allPassed = $false
        $checks += [PSCustomObject]@{
            Check = "Modules"
            Status = "✗ Fail"
            Message = "Modules not found. Run /teachme.modules"
        }
        if (-not $Quiet) {
            Write-Failure "Modules not found"
            Write-Info "Run /teachme.modules to create detailed learning modules"
        }
    }
}

# Print summary table
if (-not $Quiet -and $checks.Count -gt 0) {
    Write-Host ""
    Write-Host "Prerequisite Check Summary:" -ForegroundColor Cyan
    Write-Host ""
    $checks | Format-Table -AutoSize
    Write-Host ""
    
    if ($allPassed) {
        Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
        Write-Host "  ✓ All Prerequisites Satisfied!" -ForegroundColor Green
        Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Green
        Write-Host ""
    } else {
        Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Yellow
        Write-Host "  Some Prerequisites Need Attention" -ForegroundColor Yellow
        Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Address the failed checks above before proceeding" -ForegroundColor White
        Write-Host ""
    }
}

# Exit with appropriate code
if ($allPassed) {
    exit 0
} else {
    exit 1
}
