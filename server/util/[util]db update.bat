@echo off
cd..
echo ��� �����͵��� ���ư��ϴ� �׷��� ��� �Ͻðڽ��ϱ�?
pause
python manage.py shell < ./util/script/db_reset_shell.py
pause
cd academyMGS 
RMDIR migrations /S /Q
cd ..
python manage.py makemigrations
python manage.py migrate
pause