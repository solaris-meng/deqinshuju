from django.contrib import admin

from .models import UploadFile
from .models import TableXincheZhantingXiaoshou
from .models import TableXincheDianxiaoXiaoshou
from .models import TableXincheXiansuoLaiyuan
from .models import TableXincheXiaoshouXiansuo
from .models import TableXincheKulingTongji
from .models import TableXincheShangwuZhengce


# Register your models here.
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('user','uploadfile', 'bu_men', 'upload_id')

class TableXincheZhantingXiaoshouAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','xiaoshou_xiansuo', 'liu_dang_liang','shi_jia_liang','ding_dan_liang','jiao_che_liang')
class TableXincheDianxiaoXiaoshouAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','xiaoshou_xiansuo', 'liu_dang_liang','shi_jia_liang','ding_dan_liang','jiao_che_liang')
class TableXincheXiansuoLaiyuanAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','ziran_daodian', 'dcc','waibu_tuozhan','qita')
class TableXincheXiaoshouXiansuoAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','zhanting_xiaoshou', 'dcc_xiaoshou','er_wang','da_ke_hu')
class TableXincheKulingTongjiAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','kl_0_30', 'kl_30_60','kl_60_90','kl_90_120','kl_120_150')
class TableXincheShangwuZhengceAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','shangwu_zhengce', 'shiji_xiaoliang','wan_cheng_lv')

admin.site.register(UploadFile, UploadFileAdmin)
admin.site.register(TableXincheZhantingXiaoshou, TableXincheZhantingXiaoshouAdmin)
admin.site.register(TableXincheDianxiaoXiaoshou, TableXincheDianxiaoXiaoshouAdmin)
admin.site.register(TableXincheXiansuoLaiyuan, TableXincheXiansuoLaiyuanAdmin)
admin.site.register(TableXincheXiaoshouXiansuo, TableXincheXiaoshouXiansuoAdmin)
admin.site.register(TableXincheKulingTongji, TableXincheKulingTongjiAdmin)
admin.site.register(TableXincheShangwuZhengce, TableXincheShangwuZhengceAdmin)
