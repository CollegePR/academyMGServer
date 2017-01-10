from academyMGS.models import *
import json
from django.http import HttpResponse

def accessList(request):
    data = {'flag': False, 'data': []}
    requestId = ""
    try:

        objs = Teacher.objects.filter(status=1)
        for obj in objs:
            data.get("data").insert(0,
                {
                    "name": obj.name,
                    "id": obj.id,
                    "academy_class": obj.acdemy_class,
                }
            )
        data["flag"]=True
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')
