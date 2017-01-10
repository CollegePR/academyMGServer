from academyMGS.models import *
import json
from django.http import HttpResponse
import datetime
def attendanceChecking(request):
    data = {'flag': False}
    id = 0
    check = False
    try:
        if request.method == "POST":
            id = request.POST.get('id');
            check = request.POST.get('check');
        else:
            return HttpResponse(json.dumps(data), content_type='application/json')
        attendanceCheck = AttendanceCheck(
            student_id=id,
            date=datetime.date.today(),
            check=check,
        )
        attendanceCheck.save()
        data = {'flag': True}
    except:
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
