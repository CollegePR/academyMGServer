@echo off
cd..
echo ��� �����͵��� ���ư��ϴ� �׷��� ��� �Ͻðڽ��ϱ�?
pause
python manage.py shell < ./scripts/db_reset_shell.py
pause
del db.sqlite3
cd academyMGS 
RMDIR migrations /S /Q
cd ..
python manage.py makemigrations
python manage.py migrate
pause