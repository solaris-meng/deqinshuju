# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20151029_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.CharField(default=job.models.gen_job_id, max_length=256),
        ),
    ]
