from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    #user = models.OneToOneField(User)
    user = models.OneToOneField('auth.User', related_name='profile')

    jituanming = models.CharField(max_length=100)
    dianming = models.CharField(max_length=100)
    chengshiming = models.CharField(max_length=100)
    daqu = models.CharField(max_length=100)
    xiaoqu = models.CharField(max_length=100)
    chengshijibie = models.CharField(max_length=100)
    dizhi = models.CharField(max_length=100)
    dianhua = models.CharField(max_length=100)

    daodian_1 = models.CharField(max_length=32, default='tmp')
    daodian_2 = models.CharField(max_length=32, default='tmp')
    daodian_3 = models.CharField(max_length=32, default='tmp')
