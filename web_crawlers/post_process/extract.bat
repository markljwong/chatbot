@echo off

:: If two user arguments aren't given, then use my directory format
:: Otherwise use user provided input output directories

if "%~2"=="" (
	7z x ./Data/raw/*.rar -o./Data/extracted
	7z x ./Data/raw/*.zip -o./Data/extracted
	7z x ./Data/raw/*.7z -o./Data/extracted
) else (
	7z x %1/*.rar -o%2
	7z x %1/*.zip -o%2
	7z x %1/*.7z -o%2
)