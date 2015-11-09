from django.contrib import admin

from .models import UploadFile
from .models import TableXincheZhantingXiaoshou
from .models import TableXincheDianxiaoXiaoshou
from .models import TableXincheXiaoshouXiansuo


# Register your models here.
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('user','uploadfile', 'bu_men', 'upload_id')

class TableXincheZhantingXiaoshouAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','xiaoshou_xiansuo', 'liu_dang_liang','shi_jia_liang','ding_dan_liang','jiao_che_liang')
class TableXincheDianxiaoXiaoshouAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','xiaoshou_xiansuo', 'liu_dang_liang','shi_jia_liang','ding_dan_liang','jiao_che_liang')
class TableXincheXiaoshouXiansuoAdmin(admin.ModelAdmin):
    list_display = ('date', 'last_modified', 'user','zhanting_xiaoshou', 'dcc_xiaoshou','er_wang','da_ke_hu')

admin.site.register(UploadFile, UploadFileAdmin)
admin.site.register(TableXincheZhantingXiaoshou, TableXincheZhantingXiaoshouAdmin)
admin.site.register(TableXincheDianxiaoXiaoshou, TableXincheDianxiaoXiaoshouAdmin)
admin.site.register(TableXincheXiaoshouXiansuo, TableXincheXiaoshouXiansuoAdmin)
