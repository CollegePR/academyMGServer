# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import academyMGS.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyClass',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('date', academyMGS.models.ListField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': '수강과목',
                'verbose_name': '수강과목',
            },
        ),
        migrations.CreateModel(
            name='AttendanceCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('date', models.DateField(null=True, blank=True)),
                ('check', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': '출석체크',
                'verbose_name': '출석체크',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('image', models.TextField(blank=True)),
                ('name', models.CharField(max_length=18)),
                ('sex', models.BooleanField(default=True)),
                ('phone_num', models.TextField()),
                ('address', models.TextField()),
                ('school_name', models.TextField()),
                ('grade', models.IntegerField()),
                ('school_class', models.IntegerField()),
                ('date_of_admission', models.DateField(null=True, blank=True)),
                ('date_of_readdmission', models.DateField(null=True, blank=True)),
                ('date_of_exit', models.DateField(null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('status_of_sign', models.IntegerField(verbose_name=(1, 2))),
                ('acdemy_class', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': '학생',
                'verbose_name': '학생',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=18)),
                ('acdemy_class', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': '교사',
                'verbose_name': '교사',
            },
        ),
    ]
