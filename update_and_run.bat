@echo off
pushd %~dp0
git --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed on this system.
    echo No updates for you. Seriously, just install git.
) else (
    call git pull --rebase --autostash
    if %errorlevel% neq 0 (
        REM incase there is still something wrong
        echo There were errors while updating. Please download the latest version manually.
    )
)

setlocal enabledelayedexpansion

set "requirements_file=requirements.txt"

REM Read each line (library) from requirements.txt and check if it's installed
for /f "delims=" %%i in (%requirements_file%) do (
    set "library_name=%%i"
    pip show !library_name! > nul 2>&1
    if !errorlevel! neq 0 (
        pip install !library_name!
        if !errorlevel! neq 0 (
            echo Pip died.
            echo Check your python installation and make sure it's added to PATH.
        )
    )
)

endlocal

python main.py

pause