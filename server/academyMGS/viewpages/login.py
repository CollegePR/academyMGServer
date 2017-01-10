from academyMGS.models import *
import json
from django.http import HttpResponse
from django.contrib.auth.models import User


def login(request):
    data = {'flag': False,'data' : {}}
    id = ""
    password = ""
    try:
        if request.method == "POST":
            id = request.POST.get('id');
            password = request.POST.get('password');
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')
        obj = Teacher.objects.get(id=id)
        if obj.password == password and obj.status == 2:
            data = {'flag': True,'data':{'academy_class':obj.acdemy_class,'name':obj.name,}}
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')
