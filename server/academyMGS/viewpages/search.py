from academyMGS.models import *
from django.forms.models import model_to_dict
import json
from django.http import HttpResponse


def search(request):
    searchQuery = ""
    data = {'flag': False, 'count': 0, 'data': []}

    if request.method == 'GET':
        searchQuery = str(request.GET.get('search_query'))

    queries = searchQuery.split(" ")
    objs = []
    for query in queries:
        students = {}
        check = False
        checkFlag = "1"
        if query.__contains__("수강"):
            checkFlag = "1"
            check = True
        elif query.__contains__("미납"):
            checkFlag = "2"
            check = True
        elif query.__contains__("퇴"):
            checkFlag = "3"
            check = True
        if check:
            students = Student.objects.filter(
                Q(status_of_sign=checkFlag)
            )
            temps = []
            for obj in objs:
                for student in students.values():
                    if not student == obj:
                        temps.insert(0, student)
                        objs[0]['date_of_admission'] = str(objs[0]['date_of_admission'])
                        objs[0]['date_of_readmission'] = str(objs[0]['date_of_readmission'])
                        objs[0]['date_of_exit'] = str(objs[0]['date_of_exit'])
                        objs[0]['birthday'] = str(objs[0]['birthday'])
            if temps.__len__() > 0:
                for temp in temps:
                    objs.insert(0, temp)
            if objs.__len__() is 0:
                for student in students.values():
                    objs.insert(0, student)
                    objs[0]['date_of_admission'] = str(objs[0]['date_of_admission'])
                    objs[0]['date_of_readdmission'] = str(objs[0]['date_of_readdmission'])
                    objs[0]['date_of_exit'] = str(objs[0]['date_of_exit'])
                    objs[0]['birthday'] = str(objs[0]['birthday'])
        if query.__contains__("-") | query.isdigit():
            date = query.split("-")
            i = 0
            for number in date:
                date[i] = str(number)
                i += 1
                if i == date.__len__():
                    break
            if date.__len__() == 2:
                students = Student.objects.filter(
                    (Q(birthday__year=date[0]) & Q(birthday__month=date[1])) |
                    (Q(date_of_admission__year=date[0]) & Q(date_of_admission__month=date[1])) |
                    (Q(date_of_readdmission__year=date[0]) & Q(date_of_readdmission__month=date[1])) |
                    (Q(date_of_exit__year=date[0]) & Q(date_of_exit__month=date[1]))
                )
            elif date.__len__() == 1:
                students = Student.objects.filter(
                    Q(birthday__year=date[0]) |
                    Q(date_of_admission__year=date[0]) |
                    Q(date_of_readdmission__year=date[0]) |
                    Q(date_of_exit__year=date[0])
                )
            elif date.__len__() == 3:
                students = Student.objects.filter(
                    (Q(birthday__year=date[0]) & Q(birthday__month=date[1]) & Q(birthday__day=date[2])) |
                    (Q(date_of_admission__year=date[0]) & Q(date_of_admission__month=date[1]) & Q(
                        date_of_admission__day=date[2])) |
                    (Q(date_of_readdmission__year=date[0]) & Q(date_of_readdmission__month=date[1]) & Q(
                        date_of_readdmission__day=date[2])) |
                    (Q(date_of_exit__year=date[0]) & Q(date_of_exit__month=date[1]) & Q(date_of_exit__day=date[2]))
                )

            temps = []
            for obj in objs:
                for student in students.values():
                    if not student == obj:
                        temps.insert(0, student)
                        objs[0]['date_of_admission'] = str(objs[0]['date_of_admission'])
                        objs[0]['date_of_readmission'] = str(objs[0]['date_of_readmission'])
                        objs[0]['date_of_exit'] = str(objs[0]['date_of_exit'])
                        objs[0]['birthday'] = str(objs[0]['birthday'])
            if temps.__len__() > 0:
                for temp in temps:
                    objs.insert(0, temp)
            if objs.__len__() is 0:
                for student in students.values():
                    objs.insert(0, student)
                    objs[0]['date_of_admission'] = str(objs[0]['date_of_admission'])
                    objs[0]['date_of_readdmission'] = str(objs[0]['date_of_readdmission'])
                    objs[0]['date_of_exit'] = str(objs[0]['date_of_exit'])
                    objs[0]['birthday'] = str(objs[0]['birthday'])
        if searchQuery.__contains__("academy_class="):
            searchQuery = searchQuery.split("=")[1]
            students = Student.objects.filter(acdemy_class = int(searchQuery))

        else:
            students = Student.objects.filter(
                Q(id__contains=query) |
                Q(name__contains=query) |
                Q(address__contains=query) |
                Q(school_class__contains=query) |
                Q(school_name__contains=query) |
                Q(grade__contains=query) |
                Q(acdemy_class__contains=query) |
                Q(phone_num__contains=query)
            )

        temps = []
        for obj in objs:
            for student in students.values():
                if not student == obj:
                    temps.insert(0, student)
                    objs[0]['date_of_admission'] = str(objs[0]['date_of_admission'])
                    objs[0]['date_of_readmission'] = str(objs[0]['date_of_readmission'])
                    objs[0]['date_of_exit'] = str(objs[0]['date_of_exit'])
                    objs[0]['birthday'] = str(objs[0]['birthday'])
        if temps.__len__() > 0:
            for temp in temps:
                objs.insert(0, temp)
        if objs.__len__() is 0:
            for student in students.values():
                objs.insert(0, student)
                objs[0]['date_of_admission'] = str(objs[0]['date_of_admission'])
                objs[0]['date_of_readdmission'] = str(objs[0]['date_of_readdmission'])
                objs[0]['date_of_exit'] = str(objs[0]['date_of_exit'])
                objs[0]['birthday'] = str(objs[0]['birthday'])

    data["flag"] = True
    data["count"] = objs.__len__()
    data["data"] = objs

    return HttpResponse(json.dumps(data), content_type='application/json')
