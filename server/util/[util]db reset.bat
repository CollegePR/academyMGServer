@echo off
cd..
echo 모든 데이터들이 날아갑니다 그래도 계속 하시겠습니까?
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