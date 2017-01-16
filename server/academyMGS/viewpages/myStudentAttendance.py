from academyMGS.models import *
import json
from django.http import HttpResponse
import datetime, time


def myStudentAttendance(request):
    data = {'flag': False, 'data': []}
    requestId = ""
    __class = 0
    check = False

    try:
        print("트라이")
        if request.method == "POST":
            print("포스트")
            requestId = request.POST.get('requestId')
            print("클라에서requestId받아오고")
            objs = Teacher.objects.get(id=requestId)
            print("그아이디의선생님가져오고")

            __class = objs.acdemy_class
            print("그선생님의반가져오고")
            print(__class)
            stu = Student.objects.filter(acdemy_class=__class)
            print("받은 반의 학생 가져옵니다.")
            print(stu)

            for stu_ in stu:
                print ("================================")
                print(stu_.name)
                print(stu_.id)
                print("위는 현재 포문 학생의 정보입니다===")
                try:
                    getId = AttendanceCheck.objects.get(student_id=stu_.id,date=datetime.date.today())
                    check_attendance = getId.check
                    print(check_attendance)
                    print("위 학생의 오늘 출석정보를 불러왔습니다")
                except:
                    print("학생의 오늘 출석정보가 존재하지않습니다. 출석정보를 입력합니다.")
                    attendanceCheck = AttendanceCheck(
                        student_id=stu_.id,
                        date=datetime.date.today(),
                        check=check,
                    )
                    attendanceCheck.save()
                    print("출석정보를 갱신했습니다")
                    getId = AttendanceCheck.objects.get(student_id=stu_.id, date=datetime.date.today())
                    check_attendance = getId.check
                    print(check_attendance)
                    print("현재 학생의 오늘 출석정보를 다시 불러왔습니다")
                data.get("data").insert(0, {
                    "id": stu_.id,
                    "name": stu_.name,
                    "check" : check_attendance,
                })
                data["flag"] = True
                print("data입력완료")


    except:
        print("예외")
        return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse(json.dumps(data), content_type='application/json')
