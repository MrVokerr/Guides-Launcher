@echo off
SETLOCAL

REM ── Config ─────────────────────────────────────────────────────────────
set "SCRIPT=Guides.py"
set "APP_NAME=Guides"
set "CONFIG=config.json"
set "WORK=pybuild_temp"

REM ── Clean old EXE + temp folder ────────────────────────────────────────
echo Cleaning old artifacts...
if exist "%APP_NAME%.exe" del /f "%APP_NAME%.exe"
if exist "%WORK%" rd /s /q "%WORK%"

REM ── Ensure PyInstaller is installed ────────────────────────────────────
echo Checking for PyInstaller...
pip show pyinstaller >nul 2>&1 || (
  echo Installing PyInstaller...
  pip install pyinstaller
)

REM ── Build one-file EXE into this folder, shove all build files into %WORK% ─
echo Building %APP_NAME%.exe...
pyinstaller ^
  --onefile ^
  --windowed ^
  --name "%APP_NAME%" ^
  --add-data "%~dp0%CONFIG%;." ^
  --distpath "." ^
  --workpath "%WORK%" ^
  --specpath "%WORK%" ^
  "%SCRIPT%"

REM ── Remove the temp folder with spec/build files ───────────────────────
echo Cleaning up temp files...
if exist "%WORK%" rd /s /q "%WORK%"

REM ── Report ─────────────────────────────────────────────────────────────
echo.
if exist "%APP_NAME%.exe" (
  echo ✅ Build succeeded: %APP_NAME%.exe
) else (
  echo ❌ Build failed.
)
pause
ENDLOCAL
