# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import os
import time
from job.models import Job


# Create your models here.
def update_filename(instance, filename):
    fpath = 'data/' + time.strftime("%Y/%m/")
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
class UploadFile(models.Model):
    uploadfile = models.FileField(upload_to=update_filename)
    user = models.ForeignKey(User,null=True)
    upload_id = models.CharField(max_length=256, default='tmp')
    bu_men = models.CharField(max_length=256, default='tmp')
    file_type = models.CharField(max_length=256, default='tmp')

    # the auto updated
    last_modified = models.DateTimeField(null=True)

    # the below info is init later
    user_name = models.CharField(max_length=256, default='tmp')

    def init_info(self, bu_men):
        user_name = self.user.username
        self.last_modified = timezone.now()
        print bu_men
        self.bu_men = unicode(bu_men)
        return 'success'

    def get_abs(self):
        path = '%s/media/%s' % (settings.BASE_DIR, self.uploadfile)
        return path

    def __unicode__(self):
        #return self.file_type
        return self.uploadfile.name

class TableXincheZhantingXiaoshou(models.Model):
    date = models.DateTimeField(primary_key=False)
    xiaoshou_xiansuo = models.CharField(max_length=32, default='tmp')
    liu_dang_liang = models.CharField(max_length=32, default='tmp')
    shi_jia_liang = models.CharField(max_length=32, default='tmp')
    ding_dan_liang = models.CharField(max_length=32, default='tmp')
    jiao_che_liang = models.CharField(max_length=32, default='tmp')

    user = models.ForeignKey(User, null=True)
    username = models.CharField(max_length=32, default='test')
    job = models.ForeignKey(Job, null=True)

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        #return self.file_type
        return u'新车展厅销售'

class TableXincheDianxiaoXiaoshou(models.Model):
    date = models.DateTimeField(primary_key=False)
    xiaoshou_xiansuo = models.CharField(max_length=32, default='tmp')
    liu_dang_liang = models.CharField(max_length=32, default='tmp')
    shi_jia_liang = models.CharField(max_length=32, default='tmp')
    ding_dan_liang = models.CharField(max_length=32, default='tmp')
    jiao_che_liang = models.CharField(max_length=32, default='tmp')

    user = models.ForeignKey(User, null=True)
    username = models.CharField(max_length=32, default='test')
    job = models.ForeignKey(Job, null=True)

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        #return self.file_type
        return u'新车电销销售'
class TableXincheXiansuoLaiyuan(models.Model):
    date = models.CharField(max_length=64, default='tmp date')
    ziran_daodian = models.CharField(max_length=32, default='tmp')
    dcc = models.CharField(max_length=32, default='tmp')
    waibu_tuozhan = models.CharField(max_length=32, default='tmp')
    qita = models.CharField(max_length=32, default='tmp')

    user = models.ForeignKey(User, null=True)
    username = models.CharField(max_length=32, default='test')
    job = models.ForeignKey(Job, null=True)

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        #return self.file_type
        return u'线索来源分析'
class TableXincheXiaoshouXiansuo(models.Model):
    date = models.DateTimeField(primary_key=False)
    zhanting_xiaoshou = models.CharField(max_length=32, default='tmp')
    dcc_xiaoshou = models.CharField(max_length=32, default='tmp')
    er_wang = models.CharField(max_length=32, default='tmp')
    da_ke_hu = models.CharField(max_length=32, default='tmp')

    user = models.ForeignKey(User, null=True)
    username = models.CharField(max_length=32, default='test')
    job = models.ForeignKey(Job, null=True)

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        #return self.file_type
        return u'销售线索渠道'
class TableXincheKulingTongji(models.Model):
    date = models.CharField(max_length=64, default='tmp date')
    kl_0_30 = models.CharField(max_length=32, default='tmp')
    kl_30_60 = models.CharField(max_length=32, default='tmp')
    kl_60_90 = models.CharField(max_length=32, default='tmp')
    kl_90_120 = models.CharField(max_length=32, default='tmp')
    kl_120_150 = models.CharField(max_length=32, default='tmp')
    kl_150_180 = models.CharField(max_length=32, default='tmp')
    kl_180_270 = models.CharField(max_length=32, default='tmp')
    kl_270_360 = models.CharField(max_length=32, default='tmp')
    kl_360_0 = models.CharField(max_length=32, default='tmp')

    user = models.ForeignKey(User, null=True)
    username = models.CharField(max_length=32, default='test')
    job = models.ForeignKey(Job, null=True)

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        #return self.file_type
        return u'库龄统计'
class TableXincheShangwuZhengce(models.Model):
    date = models.CharField(max_length=64, default='tmp date')
    shangwu_zhengce = models.CharField(max_length=32, default='tmp')
    shiji_xiaoliang = models.CharField(max_length=32, default='tmp')
    wan_cheng_lv = models.CharField(max_length=32, default='tmp')

    user = models.ForeignKey(User, null=True)
    username = models.CharField(max_length=32, default='test')
    job = models.ForeignKey(Job, null=True)

    new_created = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)

    def __unicode__(self):
        #return self.file_type
        return u'销售线索渠道'
