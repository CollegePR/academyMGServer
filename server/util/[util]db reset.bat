@echo off
cd..
echo ��� �����͵��� ���ư��ϴ� �׷��� ��� �Ͻðڽ��ϱ�?
pause
python manage.py shell < ./util/db_reset_shell.py
pause