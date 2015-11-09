# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20151029_0512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='first_created',
            new_name='job_end',
        ),
        migrations.AddField(
            model_name='job',
            name='job_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 29, 5, 19, 43, 116539, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
