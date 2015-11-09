# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_job_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_id',
            field=models.CharField(default=b'tmp', max_length=256),
        ),
    ]
