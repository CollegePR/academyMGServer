from academyMGS.models import *
AcademyClass.objects.all().delete()
Student.objects.all().delete()
Teacher.objects.all().delete()
AttendanceCheck.all().delete()