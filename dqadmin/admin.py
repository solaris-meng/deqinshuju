from django.contrib import admin

from .models import ReportFile

# Register your models here.
class ReportFileAdmin(admin.ModelAdmin):
    list_display = ('user_name','customer_name', 'uploadfile', 'upload_id')
admin.site.register(ReportFile, ReportFileAdmin)
