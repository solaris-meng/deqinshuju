# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.CharField(default=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe7\x9a\x84\xe5\x94\xaf\xe4\xb8\x80\xe7\xa0\x81', max_length=256),
        ),
    ]
