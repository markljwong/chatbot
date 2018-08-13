@echo off

:: If two user arguments aren't given, then use my directory format
:: Otherwise use user provided Data directory

if "%~1"=="" (
	7z x .\Data\raw\*.rar -o.\Data\extracted
	7z x .\Data\raw\*.zip -o.\Data\extracted
	7z x .\Data\raw\*.7z -o.\Data\extracted
) else (
	7z x %1\raw\*.rar -o%1\extracted
	7z x %1\raw\*.zip -o%1\extracted
	7z x %1\raw\*.7z -o%1\extracted
)