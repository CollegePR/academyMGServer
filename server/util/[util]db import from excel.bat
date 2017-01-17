@echo off
cd..
echo 모든 데이터들이 날아갑니다 그래도 계속 하시겠습니까?
pause
python manage.py shell < ./util/db_reset_shell.py
pause