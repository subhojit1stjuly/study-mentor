# Register Teach Me Agents with GitHub Copilot CLI
# This copies teach_me agents to .github/agents/ where Copilot CLI can find them

Write-Host "`n🎓 Registering Teach Me Agents with GitHub Copilot CLI" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

$teachMeRoot = Split-Path -Parent $PSScriptRoot | Split-Path -Parent | Split-Path -Parent
$sourceDir = Join-Path $teachMeRoot ".teach\agents"
$targetDir = Join-Path $teachMeRoot ".github\agents"

Write-Host "`nSource: $sourceDir" -ForegroundColor Gray
Write-Host "Target: $targetDir" -ForegroundColor Gray
Write-Host ""

# Ensure target directory exists
if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    Write-Host "✅ Created .github\agents directory" -ForegroundColor Green
}

# Get all teachme agent files
$agentFiles = Get-ChildItem -Path $sourceDir -Filter "teachme.*.agent.md"

if ($agentFiles.Count -eq 0) {
    Write-Host "❌ No teachme agents found in $sourceDir" -ForegroundColor Red
    exit 1
}

Write-Host "Found $($agentFiles.Count) teach_me agents to register:" -ForegroundColor Cyan
Write-Host ""

$copiedCount = 0
$skippedCount = 0

foreach ($file in $agentFiles) {
    $targetPath = Join-Path $targetDir $file.Name
    
    if (Test-Path $targetPath) {
        # Check if files are different
        $sourceHash = (Get-FileHash $file.FullName -Algorithm MD5).Hash
        $targetHash = (Get-FileHash $targetPath -Algorithm MD5).Hash
        
        if ($sourceHash -eq $targetHash) {
            Write-Host "  ⏭️  $($file.Name) (already up-to-date)" -ForegroundColor Gray
            $skippedCount++
        } else {
            Copy-Item -Path $file.FullName -Destination $targetPath -Force
            Write-Host "  ✅ $($file.Name) (updated)" -ForegroundColor Yellow
            $copiedCount++
        }
    } else {
        Copy-Item -Path $file.FullName -Destination $targetPath
        Write-Host "  ✅ $($file.Name) (registered)" -ForegroundColor Green
        $copiedCount++
    }
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "📊 Summary:" -ForegroundColor Cyan
Write-Host "  New/Updated: $copiedCount" -ForegroundColor Green
Write-Host "  Already registered: $skippedCount" -ForegroundColor Gray
Write-Host "  Total agents: $($agentFiles.Count)" -ForegroundColor White
Write-Host ""

# List all registered agents
Write-Host "🎯 Available teach_me commands:" -ForegroundColor Cyan
Write-Host ""

$registeredAgents = Get-ChildItem -Path $targetDir -Filter "teachme.*.agent.md" | Sort-Object Name

foreach ($agent in $registeredAgents) {
    $commandName = $agent.BaseName -replace '\.agent$', ''
    
    # Extract description from agent file
    $content = Get-Content $agent.FullName -Raw
    if ($content -match '(?m)^description:\s*(.+)$') {
        $description = $matches[1].Trim()
    } else {
        $description = "No description available"
    }
    
    Write-Host "  /$commandName" -ForegroundColor Yellow
    Write-Host "    $description" -ForegroundColor Gray
    Write-Host ""
}

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
Write-Host "✨ Registration complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Next steps:" -ForegroundColor Cyan
Write-Host "  1. Open VS Code in this directory" -ForegroundColor White
Write-Host "  2. Open GitHub Copilot Chat" -ForegroundColor White
Write-Host "  3. Type: /teachme.philosophy" -ForegroundColor Yellow
Write-Host "  4. Start your learning journey! 🎓" -ForegroundColor White
Write-Host ""

# Verify registration
Write-Host "💡 Tip: To verify registration, type '@' in Copilot Chat" -ForegroundColor Cyan
Write-Host "   and you should see 'teachme.*' commands in the autocomplete list." -ForegroundColor Gray
Write-Host ""
