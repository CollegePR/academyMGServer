# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': '수강과목',
                'verbose_name_plural': '수강과목',
            },
        ),
        migrations.CreateModel(
            name='AttendanceCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('student_id', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('check', models.BooleanField()),
            ],
            options={
                'verbose_name': '출석체크',
                'verbose_name_plural': '출석체크',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=18)),
                ('sex', models.BooleanField(default=True)),
                ('phone_num', models.TextField()),
                ('address', models.TextField()),
                ('school_name', models.TextField()),
                ('grade', models.IntegerField()),
                ('school_class', models.IntegerField()),
                ('date_of_admission', models.DateField(blank=True, null=True)),
                ('date_of_readdmission', models.DateField(blank=True, null=True)),
                ('date_of_exit', models.DateField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('status_of_sign', models.IntegerField(verbose_name=(1, 2))),
                ('acdemy_class', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '학생',
                'verbose_name_plural': '학생',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('name', models.CharField(max_length=18)),
                ('acdemy_class', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': '교사',
                'verbose_name_plural': '교사',
            },
        ),
    ]
