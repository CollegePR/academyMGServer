# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyMGS', '0004_auto_20170108_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status_of_sign',
            field=models.IntegerField(verbose_name=(1, 2)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.TextField(),
        ),
    ]
