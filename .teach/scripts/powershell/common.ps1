#!/usr/bin/env pwsh
# Common PowerShell functions for Teach Me system

# Find repository root by searching upward for .teach directory
function Find-TeachRoot {
    param([string]$StartDir = (Get-Location).Path)

    # Normalize to absolute path to prevent issues with relative paths
    $resolved = Resolve-Path -LiteralPath $StartDir -ErrorAction SilentlyContinue
    $current = if ($resolved) { $resolved.Path } else { $null }
    if (-not $current) { return $null }

    while ($true) {
        if (Test-Path -LiteralPath (Join-Path $current ".teach") -PathType Container) {
            return $current
        }
        $parent = Split-Path $current -Parent
        if ([string]::IsNullOrEmpty($parent) -or $parent -eq $current) {
            return $null
        }
        $current = $parent
    }
}

# Get repository root, prioritizing .teach directory
function Get-RepoRoot {
    # First, look for .teach directory
    $teachRoot = Find-TeachRoot
    if ($teachRoot) {
        return $teachRoot
    }

    # Fallback to git if no .teach found
    try {
        $result = git rev-parse --show-toplevel 2>$null
        if ($LASTEXITCODE -eq 0) {
            return $result
        }
    } catch {
        # Git command failed
    }

    # Final fallback to script location
    return (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "../../..")).Path
}

# Get the active skill (current working skill)
function Get-ActiveSkill {
    $repoRoot = Get-RepoRoot
    $activeSkillPath = Join-Path $repoRoot ".teach\memory\active-skill.json"
    
    if (Test-Path $activeSkillPath) {
        try {
            $activeSkill = Get-Content $activeSkillPath | ConvertFrom-Json
            return $activeSkill.skill_id
        } catch {
            Write-Warning "Could not read active skill: $_"
            return $null
        }
    }
    
    # Fallback: find most recently modified skill
    $skillsDir = Join-Path $repoRoot "skills"
    if (Test-Path $skillsDir) {
        $latestSkill = Get-ChildItem -Path $skillsDir -Directory | 
            Sort-Object LastWriteTime -Descending | 
            Select-Object -First 1
        
        if ($latestSkill) {
            return $latestSkill.Name
        }
    }
    
    return $null
}

# Set the active skill
function Set-ActiveSkill {
    param(
        [Parameter(Mandatory=$true)]
        [string]$SkillId
    )
    
    $repoRoot = Get-RepoRoot
    $activeSkillPath = Join-Path $repoRoot ".teach\memory\active-skill.json"
    
    # Verify skill exists
    $skillDir = Join-Path $repoRoot "skills\$SkillId"
    if (-not (Test-Path $skillDir)) {
        Write-Error "Skill '$SkillId' does not exist"
        return $false
    }
    
    $activeSkill = @{
        skill_id = $SkillId
        last_updated = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    }
    
    $activeSkill | ConvertTo-Json | Set-Content $activeSkillPath
    Write-Host "Active skill set to: $SkillId" -ForegroundColor Green
    return $true
}

# Get path to skill directory
function Get-SkillPath {
    param(
        [string]$SkillId = $null
    )
    
    $repoRoot = Get-RepoRoot
    
    if (-not $SkillId) {
        $SkillId = Get-ActiveSkill
        if (-not $SkillId) {
            Write-Error "No active skill found. Use -SkillId parameter or set active skill."
            return $null
        }
    }
    
    $skillPath = Join-Path $repoRoot "skills\$SkillId"
    if (-not (Test-Path $skillPath)) {
        Write-Error "Skill directory not found: $skillPath"
        return $null
    }
    
    return $skillPath
}

# Check if git is available
function Test-HasGit {
    try {
        $null = git --version 2>$null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

# Check if philosophy exists
function Test-HasPhilosophy {
    $repoRoot = Get-RepoRoot
    $philosophyPath = Join-Path $repoRoot ".teach\memory\philosophy.md"
    return Test-Path $philosophyPath
}

# Get skill progress
function Get-SkillProgress {
    param(
        [string]$SkillId = $null
    )
    
    $skillPath = Get-SkillPath -SkillId $SkillId
    if (-not $skillPath) { return $null }
    
    $progressPath = Join-Path $skillPath "progress.json"
    if (-not (Test-Path $progressPath)) {
        Write-Warning "Progress file not found: $progressPath"
        return $null
    }
    
    try {
        return Get-Content $progressPath | ConvertFrom-Json
    } catch {
        Write-Error "Could not read progress file: $_"
        return $null
    }
}

# Update skill progress
function Update-SkillProgress {
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$Updates,
        [string]$SkillId = $null
    )
    
    $skillPath = Get-SkillPath -SkillId $SkillId
    if (-not $skillPath) { return $false }
    
    $progressPath = Join-Path $skillPath "progress.json"
    
    try {
        $progress = @{}
        if (Test-Path $progressPath) {
            $progress = Get-Content $progressPath | ConvertFrom-Json -AsHashtable
        }
        
        # Merge updates
        foreach ($key in $Updates.Keys) {
            $progress[$key] = $Updates[$key]
        }
        
        $progress['last_updated'] = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
        
        $progress | ConvertTo-Json -Depth 10 | Set-Content $progressPath
        return $true
    } catch {
        Write-Error "Could not update progress: $_"
        return $false
    }
}

# List all skills
function Get-AllSkills {
    $repoRoot = Get-RepoRoot
    $skillsDir = Join-Path $repoRoot "skills"
    
    if (-not (Test-Path $skillsDir)) {
        return @()
    }
    
    return Get-ChildItem -Path $skillsDir -Directory | ForEach-Object {
        $skillName = $_.Name
        $progressPath = Join-Path $_.FullName "progress.json"
        
        $status = "not-started"
        $completionPercent = 0
        
        if (Test-Path $progressPath) {
            try {
                $progress = Get-Content $progressPath | ConvertFrom-Json
                $status = $progress.skill_status
                
                if ($progress.total_modules -and $progress.modules) {
                    $completed = ($progress.modules | Where-Object { $_.status -eq "completed" }).Count
                    $completionPercent = [math]::Round(($completed / $progress.total_modules) * 100)
                }
            } catch {
                # Could not read progress
            }
        }
        
        [PSCustomObject]@{
            SkillId = $skillName
            Status = $status
            Completion = "$completionPercent%"
            Path = $_.FullName
        }
    }
}

# Generate next skill ID
function Get-NextSkillId {
    param(
        [Parameter(Mandatory=$true)]
        [string]$SkillName
    )
    
    $repoRoot = Get-RepoRoot
    $skillsDir = Join-Path $repoRoot "skills"
    
    # Find highest existing ID number
    $highestId = 0
    if (Test-Path $skillsDir) {
        Get-ChildItem -Path $skillsDir -Directory | ForEach-Object {
            if ($_.Name -match '^(\d{3})-') {
                $id = [int]$matches[1]
                if ($id -gt $highestId) {
                    $highestId = $id
                }
            }
        }
    }
    
    $nextId = $highestId + 1
    $idPadded = $nextId.ToString("000")
    
    # Slugify skill name
    $slug = $SkillName.ToLower() -replace '[^a-z0-9]+', '-' -replace '^-|-$', ''
    
    return "$idPadded-$slug"
}

# Check if a file exists in skill directory
function Test-SkillFile {
    param(
        [Parameter(Mandatory=$true)]
        [string]$FileName,
        [string]$SkillId = $null
    )
    
    $skillPath = Get-SkillPath -SkillId $SkillId
    if (-not $skillPath) { return $false }
    
    $filePath = Join-Path $skillPath $FileName
    return Test-Path $filePath
}

# Get domain from skill definition
function Get-SkillDomain {
    param(
        [string]$SkillId = $null
    )
    
    $skillPath = Get-SkillPath -SkillId $SkillId
    if (-not $skillPath) { return $null }
    
    $definitionPath = Join-Path $skillPath "skill-definition.md"
    if (-not (Test-Path $definitionPath)) {
        return $null
    }
    
    try {
        $content = Get-Content $definitionPath -Raw
        if ($content -match '(?m)^Domain:\s*(.+)$') {
            return $matches[1].Trim()
        }
    } catch {
        # Could not parse domain
    }
    
    return $null
}

# Pretty print header
function Write-TeachHeader {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Title
    )
    
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host "  $Title" -ForegroundColor Cyan
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""
}

# Pretty print success message
function Write-Success {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Message
    )
    
    Write-Host "✓ $Message" -ForegroundColor Green
}

# Pretty print error message
function Write-Failure {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Message
    )
    
    Write-Host "✗ $Message" -ForegroundColor Red
}

# Pretty print warning message
function Write-Alert {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Message
    )
    
    Write-Host "⚠ $Message" -ForegroundColor Yellow
}

# Pretty print info message
function Write-Info {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Message
    )
    
    Write-Host "ℹ $Message" -ForegroundColor Blue
}

# Export functions
Export-ModuleMember -Function *
