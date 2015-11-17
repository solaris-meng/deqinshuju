# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20151028_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='daodian_1',
            field=models.CharField(default=b'tmp', max_length=32),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='daodian_2',
            field=models.CharField(default=b'tmp', max_length=32),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='daodian_3',
            field=models.CharField(default=b'tmp', max_length=32),
        ),
    ]
