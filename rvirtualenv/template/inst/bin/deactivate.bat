
@echo off

"%~dp0\activate.py" "%~dp0\deactivate.bat.template" "%~dp0\_deactivate.bat"
call "%~dp0\_deactivate.bat"

