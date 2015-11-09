# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20151029_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_file_name',
            field=models.CharField(default=b'tmp', max_length=256),
        ),
    ]
