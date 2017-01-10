from django.contrib import admin
from academyMGS.models import Student, Teacher, AcademyClass, AttendanceCheck
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(AcademyClass)
admin.site.register(AttendanceCheck)