from academyMGS.models import *
import json
from django.http import HttpResponse


def setTeacher(request):
    data = {'flag': False}
    id = ""
    password = ""
    academy_class = 0
    name = ""
    status = 1
    try:
        if request.method == "POST":
            id = request.POST.get('id')
            password = request.POST.get('password')
            academy_class = request.POST.get('academy_class')
            name = request.POST.get('name')
            status = request.POST.get('status')
            if id is None:
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')

        teacher = Teacher.objects.get(id=id)
        if not password is None:
            teacher.password = password
        if not academy_class is None:
            teacher.academy_class = academy_class
        if not name is None:
            teacher.name = name
        if not status is None:
            teacher.status = status
        teacher.save()
        data = {'flag': True}
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
