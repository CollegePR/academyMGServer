@echo off
setlocal

set /p flag=디비를 초기화 합니까?(y/n):
if "%flag%" == "n" goto noresetdb

start cmd /c "./[util]db update.bat"
pause
start cmd /c "./[util]class input.bat"
:noresetdb
set /p filename=파일이름을 입력해주십시오. (.xlsx같은 확장자 붙여서):

cd..
python manage.py runscript db_import_from_excel --script-args %filename% --traceback
pause