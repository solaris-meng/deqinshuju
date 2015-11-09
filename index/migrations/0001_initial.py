# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jituanming', models.CharField(max_length=100)),
                ('dianming', models.CharField(max_length=100)),
                ('chengshiming', models.CharField(max_length=100)),
                ('daqu', models.CharField(max_length=100)),
                ('xiaoqu', models.CharField(max_length=100)),
                ('chengshijibie', models.CharField(max_length=100)),
                ('dizhi', models.CharField(max_length=100)),
                ('dianhua', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
