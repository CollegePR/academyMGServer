from academyMGS.models import *
import json
from django.http import HttpResponse
import datetime

def addStudent(request):
    data = {'flag': False}
    image = ""
    name = ""
    sex = True
    phone_num = ""
    address = ""
    school_name = ""
    grade = 0
    school_class = 0
    status_of_sign = 0
    date_of_admission = ""
    date_of_readdmission = ""
    date_of_exit = ""
    birthday = ""
    academy_class = 0
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            sex = request.POST.get('sex')
            phone_num = request.POST.get('phone_num')
            address = request.POST.get('address')
            school_name = request.POST.get('school_name')
            grade = request.POST.get('grade')
            school_class = request.POST.get('school_class')
            status_of_sign = request.POST.get('status_of_sign')
            date_of_admission = request.POST.get('date_of_admission')
            date_of_readdmission = request.POST.get('date_of_readdmission')
            date_of_exit = request.POST.get('date_of_exit')
            birthday = request.POST.get('birthday')
            academy_class = request.POST.get('academy_class')
            image = request.POST.get('image')

            date_of_admission=date_of_admission.split("-")
            date_of_admission_year=int(date_of_admission[0])
            date_of_admission_month=int(date_of_admission[1])
            date_of_admission_day = int(date_of_admission[2])
            admissionData = datetime.date(date_of_admission_year,date_of_admission_month,date_of_admission_day)

            date_of_readdmission = date_of_readdmission.split("-")
            date_of_readdmission_year = int(date_of_readdmission[0])
            date_of_readdmission_month = int(date_of_readdmission[1])
            date_of_readdmission_day = int(date_of_readdmission[2])
            readdmissionData = datetime.date(date_of_readdmission_year, date_of_readdmission_month, date_of_readdmission_day)

            date_of_exit = date_of_exit.split("-")
            date_of_exit_year = int(date_of_exit[0])
            date_of_exit_month = int(date_of_exit[1])
            date_of_exit_day = int(date_of_exit[2])
            exitData = datetime.date(date_of_exit_year,date_of_exit_month,date_of_exit_day)

            birthday = birthday.split("-")
            birthday_year = int(birthday[0])
            birthday_month = int(birthday[1])
            birthday_day = int(birthday[2])
            birthdayData = datetime.date(birthday_year,birthday_month,birthday_day)




        else:
            return HttpResponse(json.dumps(data), content_type='application/json')

        student = Student(
            name=name,
            sex=sex,
            phone_num=phone_num,
            address=address,
            school_name=school_name,
            school_class=school_class,
            grade=grade,
            status_of_sign=status_of_sign,
            date_of_admission = admissionData,
            date_of_readdmission = readdmissionData,
            date_of_exit = exitData,
            birthday = birthdayData,
            academy_class = academy_class,
            image = image,


        )
        student.save()
        data = {'flag': True}
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
