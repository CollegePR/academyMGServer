from .models import *
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .viewpages import addStudent,login,index,idCheck,register,setStudent,search,accessList,setTeacher,attendanceStatus,attendanceChecking
@csrf_exempt
def addStudentPage(request):
    return addStudent.addStudent(request)
@csrf_exempt
def loginPage(request):
    return login.login(request)
@csrf_exempt
def indexPage(request):
    return index.index(request)
@csrf_exempt
def idCheckPage(request):
    return idCheck.idCheck(request)
@csrf_exempt
def registerPage(request):
    return register.register(request)
@csrf_exempt
def searchPage(request):
    return search.search(request)
@csrf_exempt
def setStudentPage(request):
    return setStudent.setStudent(request)
@csrf_exempt
def setStudentPage(request):
    return setStudent.setStudent(request)
@csrf_exempt
def accessListPage(request):
    return accessList.accessList(request)
@csrf_exempt
def setTeacherPage(request):
    return setTeacher.setTeacher(request)
@csrf_exempt
def attendanceCheckingPage(request):
    return setTeacher.setTeacher(request)
@csrf_exempt
def attendanceStatusPage(request):
    return setTeacher.setTeacher(request)

