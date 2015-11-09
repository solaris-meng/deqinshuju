# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_file', models.FileField(upload_to=job.models.update_filename)),
                ('job_name', models.CharField(default=b'tmp', max_length=64)),
                ('job_status', models.CharField(default=b'\xe6\x9c\xaa\xe4\xb8\x8a\xe7\xba\xbf', max_length=64)),
                ('job_bu_men', models.CharField(default=b'tmp', max_length=64)),
            ],
        ),
    ]
