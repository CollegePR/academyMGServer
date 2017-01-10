from academyMGS.models import *
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def register(request):
    data = {'flag': False}
    id = ""
    password = ""
    academy_class = ""
    name = ""
    try:
        if request.method == "POST":
            id = request.POST.get('id');
            password = request.POST.get('password');
            academy_class = request.POST.get('academy_class');
            name = request.POST.get('name');
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')
        if(Teacher.objects.filter(id=id).count()!=0):
            return HttpResponse(json.dumps(data), content_type='application/json')
        teacher = Teacher(
            id=id,
            password=password,
            acdemy_class=academy_class,
            name=name,
            status=1,
        )
        teacher.save()
        data = {'flag': True}
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
