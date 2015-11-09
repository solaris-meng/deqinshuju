# encoding:utf-8
import os
import time

from django.db import models

# Create your models here.
def update_filename(instance, filename):
    fpath = 'job/' + time.strftime("%Y/%m/")
    fname = filename
    return os.path.join(fpath, fname)
def gen_job_id():
    job_id = time.strftime('%Y_%m_%d_%H_%M_%S')
    return job_id

# Create your models here.
class Job(models.Model):

    job_name = models.CharField(max_length=256, default='tmp')
    job_id = models.CharField(max_length=256, default=gen_job_id)
    job_file = models.FileField(upload_to=update_filename)
    job_file_name = models.CharField(max_length=256, default='tmp')
    job_status = models.CharField(max_length=256, default='未上线')
    job_bu_men = models.CharField(max_length=256, default='tmp')
    job_is_active = models.BooleanField(default=True)

    job_start = models.DateTimeField()
    job_end = models.DateTimeField()
    last_modified = models.DateTimeField()

    def __unicode__(self):
        return self.job_name


    def get_file_path(self):
        #return os.path.basename(self.job_file.name)
        local_path = self.job_file.path
        idx = local_path.rindex('media')
        return local_path[idx:]
