# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyMGS', '0005_auto_20170110_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academyclass',
            name='date',
        ),
        migrations.RemoveField(
            model_name='academyclass',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='academyclass',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='student',
            name='status_of_sign',
            field=models.IntegerField(verbose_name=(1, 2)),
        ),
    ]
