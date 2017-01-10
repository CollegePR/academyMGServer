from academyMGS.models import *
import json
from django.http import HttpResponse
import datetime, time
def attendanceStatus(request):
    data = {'flag': False,'data':[]}
    id = 0
    try:
        if request.method == "POST":
            id = request.POST.get('id');
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')
        objs=AttendanceCheck.objects.filter(student_id=id)
        temps=[]
        for obj in objs.values():
            temps.insert(0, obj)
            temps[0]['date'] = str(temps[0]['date'])
            del temps[0]['id']
            del temps[0]['student_id']
        data = {'flag': True,'data':temps}
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
