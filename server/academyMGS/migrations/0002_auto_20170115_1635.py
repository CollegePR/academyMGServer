# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academyMGS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status_of_sign',
            field=models.IntegerField(verbose_name=(1, 2)),
        ),
    ]
