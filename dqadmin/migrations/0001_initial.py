# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import dqadmin.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uploadfile', models.FileField(upload_to=dqadmin.models.update_filename)),
                ('upload_id', models.CharField(default=b'tmp', max_length=256)),
                ('file_type', models.CharField(default=b'tmp', max_length=256)),
                ('last_modified', models.DateTimeField(null=True)),
                ('user_name', models.CharField(default=b'tmp', max_length=256)),
                ('customer_name', models.CharField(default=b'tmp', max_length=256)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
