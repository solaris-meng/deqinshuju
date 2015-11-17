"""deqinshuju URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# for manage upload file
from django.conf import settings
from django.conf.urls.static import static

# for views
from index.views import index_view
from index.views import register_view,register_handler_view
from index.views import login_view,logout_view,login_handler_view

# for data
import data.views

# for dqadmin
import dqadmin.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # index
    url(r'^$', index_view, name='index'),
    url(r'^register$', register_view, name='register'),
    url(r'^register_handler$', register_handler_view, name='register_handler'),
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^login_handler$', login_handler_view, name='login_handler'),

    # data
    #url(r'^data_in$', data.views.data_in_view, name='data_in'),
    url(r'^data_in/(?P<bu_men>[\w\W]+)$', data.views.data_in_view, name='data_in_view'),
    url(r'^data_in_handler/(?P<job_id>[\w\W]+)$', data.views.data_in_handler, name='data_in_handler'),
    url(r'^data_in_status/(?P<bu_men>[\w\W]+)$', data.views.data_in_status_view, name='data_in_status'),

    # dqadmin
    url(r'^dqadmin/excel$', dqadmin.views.dq_excel_view, name='dq_excel'),
    url(r'^dqadmin/excel_user$', dqadmin.views.dq_excel_user_view, name='dq_excel_user'),
    url(r'^dqadmin/daodian$', dqadmin.views.dq_daodian_view, name='dq_daodian'),
    url(r'^dqadmin/daodian_company$', dqadmin.views.dq_daodian_company_view, name='dq_daodian_company'),
    url(r'^dqadmin/daodian_handler/(?P<username>[\w\W]+)$', dqadmin.views.dq_daodian_handler, name='dq_daodian_handler'),
    url(r'^dqadmin/job_in_process$', dqadmin.views.job_in_process, name='job_in_process'),
    url(r'^dqadmin/database/compare$', dqadmin.views.db_compare_view, name='db_compare_view'),
    url(r'^dqadmin/database/table$', dqadmin.views.db_get_table, name='db_get_table'),
    url(r'^dqadmin/database/(?P<table_name>[\w\W]+)$', dqadmin.views.db_view, name='db_view'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
