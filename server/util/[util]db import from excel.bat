@echo off
setlocal

set /p flag=��� �ʱ�ȭ �մϱ�?(y/n):
if "%flag%" == "n" goto noresetdb

start cmd /c "./[util]db update.bat"
pause
start cmd /c "./[util]class input.bat"
:noresetdb
set /p filename=�����̸��� �Է����ֽʽÿ�. (.xlsx���� Ȯ���� �ٿ���):

cd..
python manage.py runscript db_import_from_excel --script-args %filename% --traceback
pause