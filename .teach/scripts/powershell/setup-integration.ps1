# Quick Start Setup Script
# Run this to complete the integration setup

Write-Host "`n🎓 Teach Me + CS_AI_Study Integration" -ForegroundColor Cyan
Write-Host "Setting up your learning system for working professionals...`n" -ForegroundColor Gray

# Check both repos exist
$teachMePath = "D:\Projects\ShowCase\agentAi\teach_me"
$studyPath = "D:\Projects\CS_AI_Study"

if (-not (Test-Path $teachMePath)) {
    Write-Host "❌ teach_me not found at: $teachMePath" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $studyPath)) {
    Write-Host "❌ CS_AI_Study not found at: $studyPath" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Found teach_me: $teachMePath" -ForegroundColor Green
Write-Host "✅ Found CS_AI_Study: $studyPath" -ForegroundColor Green
Write-Host ""

# Create workspace file
$workspacePath = "D:\Projects\GooglePrep.code-workspace"
$workspaceContent = @{
    folders = @(
        @{ 
            path = $teachMePath
            name = "🎓 Teach Me (Learning System)"
        }
        @{ 
            path = $studyPath
            name = "💻 CS_AI_Study (Practice)"
        }
    )
    settings = @{
        "files.autoSave" = "afterDelay"
        "terminal.integrated.cwd" = $studyPath
    }
} | ConvertTo-Json -Depth 5

Set-Content -Path $workspacePath -Value $workspaceContent
Write-Host "✅ Created VS Code workspace: $workspacePath" -ForegroundColor Green
Write-Host ""

# Check if reference file exists
$refFile = Join-Path $studyPath "TEACH_ME_REFERENCE.md"
if (Test-Path $refFile) {
    Write-Host "✅ TEACH_ME_REFERENCE.md already in CS_AI_Study" -ForegroundColor Green
} else {
    Write-Host "⚠️  TEACH_ME_REFERENCE.md not found - create it manually" -ForegroundColor Yellow
}
Write-Host ""

# Check skills
$skillsPath = Join-Path $teachMePath "skills"
$skillCount = (Get-ChildItem $skillsPath -Directory).Count
Write-Host "✅ Found $skillCount skills ready to learn" -ForegroundColor Green
Write-Host ""

# Summary
Write-Host "📊 Setup Summary" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "  📍 teach_me location: $teachMePath" -ForegroundColor White
Write-Host "  📍 CS_AI_Study location: $studyPath" -ForegroundColor White
Write-Host "  💼 VS Code workspace: $workspacePath" -ForegroundColor White
Write-Host "  🎯 Skills available: $skillCount" -ForegroundColor White
Write-Host "  ⏰ Study schedule: 31 hrs/week (Mon-Fri: 3h, Weekend: 16h)" -ForegroundColor White
Write-Host ""

# Next steps
Write-Host "🚀 Next Steps" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
Write-Host "1. Open VS Code workspace:" -ForegroundColor Yellow
Write-Host "   code `"$workspacePath`"" -ForegroundColor White
Write-Host ""
Write-Host "2. Create your learning philosophy:" -ForegroundColor Yellow
Write-Host "   cd $teachMePath" -ForegroundColor White
Write-Host "   # In GitHub Copilot Chat: /teachme.philosophy" -ForegroundColor White
Write-Host ""
Write-Host "3. Start with Arrays & Strings (recommended):" -ForegroundColor Yellow
Write-Host "   # In Copilot Chat: /teachme.assess" -ForegroundColor White
Write-Host "   # Choose skill: 003-arrays-and-strings" -ForegroundColor White
Write-Host ""
Write-Host "4. Generate your roadmap:" -ForegroundColor Yellow
Write-Host "   # In Copilot Chat: /teachme.roadmap" -ForegroundColor White
Write-Host ""
Write-Host "5. Start learning tonight! (2-hour session)" -ForegroundColor Yellow
Write-Host "   # In Copilot Chat: /teachme.learn" -ForegroundColor White
Write-Host ""

Write-Host "📚 Reference Guide: $refFile" -ForegroundColor Cyan
Write-Host ""
Write-Host "✨ Integration complete! Ready to start your Google prep journey! 🚀" -ForegroundColor Green
Write-Host ""

# Offer to open workspace
$response = Read-Host "Do you want to open the workspace now? (Y/n)"
if ($response -eq "" -or $response -eq "Y" -or $response -eq "y") {
    Write-Host "`n🚀 Opening VS Code workspace..." -ForegroundColor Cyan
    code "$workspacePath"
} else {
    Write-Host "`n👍 You can open it later with: code `"$workspacePath`"" -ForegroundColor Cyan
}
