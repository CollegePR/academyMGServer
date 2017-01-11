cd ../academyMGS 
RMDIR migrations /S /Q
cd ..
python manage.py makemigrations
python manage.py migrate
pause