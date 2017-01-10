from academyMGS.models import *
import json
from django.http import HttpResponse

def classList(request):
    data = {'flag': False, 'data': []}
    try:
        objs = AcademyClass.objects.all()
        for obj in objs:
            data.get("data").insert(0,
                {
                    "id": obj.id,
                    "name": obj.name,
                }
            )
        data["flag"]=True
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')
