# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20151029_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='first_created',
            field=models.DateField(default=datetime.datetime(2015, 10, 29, 5, 4, 35, 123331, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='last_modified',
            field=models.DateField(default=datetime.datetime(2015, 10, 29, 5, 4, 57, 186555, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
