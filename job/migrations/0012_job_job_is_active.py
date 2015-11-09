# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20151029_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_is_active',
            field=models.BooleanField(default=True),
        ),
    ]
