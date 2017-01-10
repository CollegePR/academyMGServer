from academyMGS.models import *
import json
from django.http import HttpResponse
import datetime
from ..forms import ImageUploadForm

def setStudent(request):
    data = {'flag': False}
    id = 0
    name = ""
    sex = True
    image = ""
    phone_num = ""
    address = ""
    school_name = ""
    grade = 0
    school_class = 0
    status_of_sign = 1
    date_of_admission = ""
    date_of_readdmission = ""
    date_of_exit = ""
    birthday = ""
    academy_class = 0

    try:
        if request.method == "POST":
            id = request.POST.get('id')
            image = ImageUploadForm(request.POST, request.FILES)
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
            if id is None:
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')
        student = Student.objects.get(id=id)
        if not image is None:
            student.image = image.cleaned_data['image'],
        if not name is None:
            student.name = name
        if not sex is None:
            student.sex = sex
        if not phone_num is None:
            student.phone_num = phone_num
        if not address is None:
            student.address = address
        if not school_name is None:
            student.school_name = school_name
        if not grade is None:
            student.grade = grade
        if not school_class is None:
            student.school_class = school_class
        if not status_of_sign is None:
            student.status_of_sign = status_of_sign
        if not date_of_admission is None:
            date_of_admission = date_of_admission.split("-")
            date_of_admission_year = int(date_of_admission[0])
            date_of_admission_month = int(date_of_admission[1])
            date_of_admission_day = int(date_of_admission[2])
            admissionData = datetime.date(date_of_admission_year, date_of_admission_month, date_of_admission_day)
            student.date_of_admission = admissionData
        if not date_of_readdmission is None:
            date_of_readdmission = date_of_readdmission.split("-")
            date_of_readdmission_year = int(date_of_readdmission[0])
            date_of_readdmission_month = int(date_of_readdmission[1])
            date_of_readdmission_day = int(date_of_readdmission[2])
            readdmissionData = datetime.date(date_of_readdmission_year, date_of_readdmission_month,
                                             date_of_readdmission_day)
            student.date_of_readdmission = readdmissionData
        if not date_of_exit is None:
            date_of_exit = date_of_exit.split("-")
            date_of_exit_year = int(date_of_exit[0])
            date_of_exit_month = int(date_of_exit[1])
            date_of_exit_day = int(date_of_exit[2])
            exitData = datetime.date(date_of_exit_year, date_of_exit_month, date_of_exit_day)
            student.date_of_exit = exitData
        if not birthday is None:
            birthday = birthday.split("-")
            birthday_year = int(birthday[0])
            birthday_month = int(birthday[1])
            birthday_day = int(birthday[2])
            birthdayData = datetime.date(birthday_year, birthday_month, birthday_day)
            student.birthday = birthdayData

        student.save()
        data = {'flag': True}

    except:
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
