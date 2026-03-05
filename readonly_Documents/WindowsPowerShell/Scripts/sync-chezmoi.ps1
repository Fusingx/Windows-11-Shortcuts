# --- sync-chezmoi.ps1 ---
$chezmoiSource = chezmoi source-path

if (-not (Test-Path $chezmoiSource)) {
    Write-Error "Chezmoi source directory not found."
    exit
}

Set-Location $chezmoiSource
Write-Host "Syncing from: $chezmoiSource" -ForegroundColor Cyan

# Check if we have a remote set up
$hasRemote = git remote
if (-not $hasRemote) {
    Write-Host "Warning: No git remote found. Use 'git remote add origin <URL>' first." -ForegroundColor Yellow
}

# Add, Commit, and Push
git add .
$status = git status --porcelain
if ($status) {
    $date = Get-Date -Format "yyyy-MM-dd HH:mm"
    git commit -m "Auto-sync: $date"
    
    if ($hasRemote) {
        Write-Host "Pushing to GitHub..." -ForegroundColor Magenta
        git push origin main # or 'master'
    }
} else {
    Write-Host "No changes to sync." -ForegroundColor Green
}