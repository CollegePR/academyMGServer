# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyMGS', '0002_auto_20161227_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='academyclass',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='academyclass',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='status_of_sign',
            field=models.IntegerField(verbose_name=(1, 2)),
        ),
    ]
