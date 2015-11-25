# encoding:utf-8
from django.db import models

import os
import time
from django.utils import timezone 
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
def update_filename(instance, filename):
    fpath = 'dqadmin/' + time.strftime("%Y/%m/%d/")
    fname = instance.user.username + instance.upload_id + filename
    #fname = 'meng' + filename 
    return os.path.join(fpath, fname)

#
# object create:
#   1.uploadfile    -- FileField -- /media/year/month/
#   2.user          -- User      -- FK
#   3.upload_id     -- uuid4
#
#   bu_men\file_type 
#   '新车'         - '初次信息'
#   '二手车'       - '初次信息'
#       
class ReportFile(models.Model):
    uploadfile = models.FileField(upload_to=update_filename)
    user = models.ForeignKey(User,null=True)
    upload_id = models.CharField(max_length=256, default='tmp')
    file_type = models.CharField(max_length=256, default='tmp')

    # the auto updated
    last_modified = models.DateTimeField(null=True)

    # the below info is init later
    user_name = models.CharField(max_length=256, default='tmp')
    customer_name = models.CharField(max_length=256, default='tmp')

    def init_info(self):
        self.user_name = self.user.username
        self.last_modified = timezone.now()
        return 'success'

    def get_abs(self):
        path = '%s/media/%s' % (settings.BASE_DIR, self.uploadfile)
        return path

    def get_file_path(self):
        #return os.path.basename(self.job_file.name)
        local_path = self.uploadfile.path
        idx = local_path.rindex('media')
        return local_path[idx:]

    def get_ico_tl(self):
        tm = self.last_modified
        return tm.strftime("%Y.%m.%d")
    def get_ico_note(self):
        tm = self.last_modified
        rv = '上传时间: %s' % tm.strftime("%Y-%m-%d %H:%M:%S")
        return rv
       

    def __unicode__(self):
        #return self.file_type
        return self.uploadfile.name
