# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20151029_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_bu_men',
            field=models.CharField(default=b'tmp', max_length=256),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_name',
            field=models.CharField(default=b'tmp', max_length=256),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_status',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe4\xb8\x8a\xe7\xba\xbf', max_length=256),
        ),
    ]
