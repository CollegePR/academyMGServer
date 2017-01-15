from academyMGS.models import *
import json
from django.http import HttpResponse
import datetime, time


def myStudentAttendance(request):
    data = {'flag': False, 'data': []}
    requestId = ""
    __class = 0
    try:
        print("트라이")
        if request.method == "POST":
            requestId = request.POST.get('requestId')
            objs = Teacher.objects.filter(id=requestId)
            __class = objs.academy_class
            stu = Student.objects.filter(acdemy_class=__class)
            for stu_ in stu:
                __id = stu.id
                attobjs = AttendanceCheck.objects.filter(student_id = __id).filter(date = datetime.date.today())
                data.get("data").insert(0,
                                        {
                                            "id": __id,
                                            "name": stu.name,
                                            "attendance":attobjs.check
                                        }
                                        )


    except:
        print("예외")
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
