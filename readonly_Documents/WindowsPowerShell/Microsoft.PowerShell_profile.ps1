Clear-Host
#$ENV:STARSHIP_LOG = "error"
Invoke-Expression (&starship init powershell)
#Set-PSReadLineOption -PredictionSource History