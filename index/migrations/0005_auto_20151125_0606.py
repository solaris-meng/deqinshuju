# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20151116_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='daodian_1',
            field=models.CharField(default=b'0%', max_length=32),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='daodian_2',
            field=models.CharField(default=b'0%', max_length=32),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='daodian_3',
            field=models.CharField(default=b'0%', max_length=32),
        ),
    ]
