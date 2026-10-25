$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not (Get-Command doxygen -ErrorAction SilentlyContinue)) {
    Write-Error "doxygen is not installed or not on PATH. Install from https://www.doxygen.nl/download.html"
}

doxygen Doxyfile
Write-Host "Documentation generated: $root\docs\doxygen\html\index.html"
