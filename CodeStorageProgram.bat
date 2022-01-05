@ECHO OFF
PUSHD %~DP0

rem ::::::::::::::::::::::::::::::::::::::::::::::::::::::
rem :: 아래 ProgramPath를 해당 프로그램이 있는 경로로 수정 ::
rem ::::::::::::::::::::::::::::::::::::::::::::::::::::::
SET ProgramPath="C:\PythonProject\PyCodeStorage"

cd %ProgramPath%
python main.py

pause
cmd.ext