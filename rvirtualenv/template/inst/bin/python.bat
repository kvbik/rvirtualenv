
@echo off

for /f "tokens=*" %%i in ('%~dp0\getpythondist.py') do set python=%%i
call "%python%" "%~dp0\python.py" %*

