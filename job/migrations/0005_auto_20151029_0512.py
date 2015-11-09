# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20151029_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='first_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='last_modified',
            field=models.DateTimeField(),
        ),
    ]
