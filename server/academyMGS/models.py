from django.db.models import *
from django.db import models
import urllib, os
from urllib.parse import urlparse
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return str(value, 'utf-8')

    def get_prep_value(self, value):
        if value is None:
            return value
        return python_2_unicode_compatible(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class AcademyClass(models.Model):
    class Meta:
        verbose_name = '수강과목'
        verbose_name_plural = '수강과목'

    # Fields
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name

def path_and_rename(instance, filename):
    upload_to = 'static/profile'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(str(instance.pk), ext)

    # return the whole path to the file
    return os.path.join(upload_to, filename)
class Student(models.Model):
    class Meta:
        verbose_name = '학생'
        verbose_name_plural = '학생'

    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=18)
    sex = models.BooleanField(default=True)
    phone_num = models.TextField()
    address = models.TextField()
    school_name = models.TextField()
    grade = models.IntegerField()
    school_class = models.IntegerField()
    date_of_admission = models.DateField(blank=True,null=True)
    date_of_readdmission = models.DateField(blank=True,null=True)
    date_of_exit = models.DateField(blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    #현재 수강상태
    status_of_sign = models.IntegerField(range(1, 3))
    #어떤 반인지 AcademyClass id값임.
    acdemy_class = models.IntegerField(blank=True,null=True)


    #attendanceCheck = AttendanceCheck()
    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Teacher(models.Model):
    class Meta:
        verbose_name = '교사'
        verbose_name_plural = '교사'
    # Fields
    id = models.CharField(primary_key=True, max_length=30)
    password = models.TextField()
    name = models.CharField(max_length=18)
    #어떤 반인지 AcademyClass id값임.
    acdemy_class = models.IntegerField(blank=True,null=True)
    status = models.IntegerField(default=1)
    def __str__(self):  # __unicode__ on Python 2
        return self.name
class AttendanceCheck(models.Model):
    class Meta:
        verbose_name = '출석체크'
        verbose_name_plural = '출석체크'
    #Fields
    student_id = models.IntegerField()
    date = models.DateField(blank=True,null=True)
    check = models.BooleanField()

    def __str__(self):  # __unicode__ on Python 2
      return self.student_id.__str__()
