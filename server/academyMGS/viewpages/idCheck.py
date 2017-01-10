from academyMGS.models import *
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def idCheck(request):
    data = {'flag': False}
    requestId = ""
    try:
        if request.method == 'GET':
            requestId = request.GET.get('id')
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')
        data = {'flag': (Teacher.objects.filter(id=requestId).exists()) and (True) or (False)}
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
