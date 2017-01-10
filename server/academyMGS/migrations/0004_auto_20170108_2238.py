# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academyMGS', '0003_auto_20170108_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status_of_sign',
            field=models.IntegerField(verbose_name=(1, 2)),
        ),
    ]
