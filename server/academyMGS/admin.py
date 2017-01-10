from academyMGS.models import Student, Teacher, AcademyClass, AttendanceCheck
from django.contrib import admin
# Register your models here.
class StudentpageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
admin.site.register(Student,StudentpageAdmin)
admin.site.register(Teacher)
admin.site.register(AcademyClass)
admin.site.register(AttendanceCheck)