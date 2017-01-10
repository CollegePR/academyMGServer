from academyMGS.models import *
import json
from django.http import HttpResponse

def getClassName(request):
    data = {'flag': False, 'data': {}}
    academy_class=0
    try:
        if request.method == 'GET':
            academy_class = request.GET.get('academy_class')
        objs = AcademyClass.objects.filter(id=academy_class)
        data = {'flag': True, 'data': objs.values()[0]}

    except:
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')
