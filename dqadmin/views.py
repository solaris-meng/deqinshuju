# encoding:utf-8


from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.core import serializers
import json
import traceback

#xml
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 

from job.models import Job

# xinche table
from data.models import *
from .models import ReportFile
from uuid import uuid4
#from data.models import UploadFile

def get_admins():
    admins = []
    admins.append(User.objects.get(username='admin'))
    admins.append(User.objects.get(username='coadmin'))
    admins.append(User.objects.get(username='dqadmin'))
    return admins

# Create your views here.
def job_in_process(request):
    ctx={}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))
    template = loader.get_template('dqadmin/job_in_process.html')
    ctx['job'] = Job.objects.all()
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))

def dq_excel_view(request, username):
    ctx={}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))

    # get all users
    if username == 'all':
        users = User.objects.all()
    else:
        users = User.objects.filter(username=username)
    admin = User.objects.get(username='admin')

    user_result = []
    # for every user, catch all related files
    for user in users:
        if user == admin:
            continue
        files = UploadFile.objects.filter(user=user)
        print files
        if files:
            it = {}
            it['username'] = user.username
            it['jituanming'] = user.profile.jituanming
            it['dianming'] = user.profile.dianming
            #it['jituanming'] = user.UserProfile.jituanming
            #it['dianming'] = user.UserProfile.dianming
            it['file_xinche'] = UploadFile.objects.filter(user=user, bu_men='新车部门')
            it['file_ershouche'] = UploadFile.objects.filter(user=user, bu_men='二手车部门')
            it['file_beijian'] = UploadFile.objects.filter(user=user, bu_men='备件部门')
            it['file_shouhou'] = UploadFile.objects.filter(user=user, bu_men='售后部门')
            it['file_jinrong'] = UploadFile.objects.filter(user=user, bu_men='金融保险部门')
            it['file_qita'] = UploadFile.objects.filter(user=user, bu_men='其他数据')
            user_result.append(it)
    ctx['all'] = user_result
    if user_result:
        ctx['result'] = 'success'
    else:
        ctx['result'] = '没有上传记录'

    if username == 'all':
        ctx['cur_user'] = '全部用户'
        other_user_name = []
    else:
        ctx['cur_user'] = username
        other_user_name = ['全部用户']
    users = User.objects.exclude(username=username)
    for u in users:
        other_user_name.append(u.username)
    ctx['other_user'] = other_user_name

    template = loader.get_template('dqadmin/dq_excel.html')
    ctx['uploadfile'] = UploadFile.objects.all()
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))

def dq_excel_user_view(request):
    ctx={}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))

    # get all users
    #users = User.objects.get(username=username)
    user = request.user
    #admin = User.objects.get(username='admin')

    user_result = []
    # for every user, catch all related files
    files = UploadFile.objects.filter(user=user)
    print files
    if files:
        it = {}
        it['username'] = user.username
        it['jituanming'] = user.profile.jituanming
        it['dianming'] = user.profile.dianming
        #it['jituanming'] = user.UserProfile.jituanming
        #it['dianming'] = user.UserProfile.dianming
        it['file_xinche'] = UploadFile.objects.filter(user=user, bu_men='新车部门')
        it['file_ershouche'] = UploadFile.objects.filter(user=user, bu_men='二手车部门')
        it['file_beijian'] = UploadFile.objects.filter(user=user, bu_men='备件部门')
        it['file_shouhou'] = UploadFile.objects.filter(user=user, bu_men='售后部门')
        it['file_jinrong'] = UploadFile.objects.filter(user=user, bu_men='金融保险部门')
        it['file_qita'] = UploadFile.objects.filter(user=user, bu_men='其他数据')
        user_result.append(it)
    ctx['all'] = user_result

    template = loader.get_template('dqadmin/dq_excel_user.html')
    #ctx['uploadfile'] = UploadFile.objects.all()
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))


def dq_daodian_view(request):
    ctx={}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))

    # get all users
    users = User.objects.all()
    admins = get_admins()

    user_result = []
    for user in users:
        if user in admins:
            continue
        it = {}
        it['username'] = user.username
        it['jituanming'] = user.profile.jituanming
        it['dianming'] = user.profile.dianming
        it['daodian_1'] = user.profile.daodian_1
        it['daodian_2'] = user.profile.daodian_2
        it['daodian_3'] = user.profile.daodian_3
        user_result.append(it)
    ctx['users'] = user_result
    template = loader.get_template('dqadmin/dq_daodian.html')
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))

def dq_daodian_company_view(request):
    ctx={}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))

    # get all users
    users = User.objects.all()
    admins = get_admins()

    user_result = []
    for user in users:
        if user in admins:
            continue
        it = {}
        it['username'] = user.username
        it['jituanming'] = user.profile.jituanming
        it['dianming'] = user.profile.dianming
        it['daodian_1'] = user.profile.daodian_1
        it['daodian_2'] = user.profile.daodian_2
        it['daodian_3'] = user.profile.daodian_3
        it['reports'] = ReportFile.objects.filter(customer_name=user.username)
        user_result.append(it)
    ctx['users'] = user_result
    template = loader.get_template('dqadmin/dq_daodian_company.html')
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))

def dq_daodian_handler(request, username):
    rv_dict = {}
    rv_dict['result'] = '保存失败'

    if request.method == 'POST':
        print request.POST
        try:
            user = User.objects.get(username=username)
            user.profile.daodian_1 = request.POST['daodian_1_value']
            user.profile.daodian_2 = request.POST['daodian_2_value']
            user.profile.daodian_3 = request.POST['daodian_3_value']
            #print user.profile.daodian_1,user.profile.daodian_2,user.profile.daodian_3
            user.profile.save()
            rv_dict['result'] = '保存成功'
        except Exception, e:
            err = traceback.format_exc()
            rv_dict['result'] = '%s' % err

        rv = json.dumps(rv_dict)
        return HttpResponse(rv, content_type="application/json")

    rv_dict['result'] = '不允许的操作'
    rv = json.dumps(rv_dict)
    return HttpResponse(rv, content_type="application/json")

# init view
def db_view(request, table_name):
    ctx={}
    if table_name == 'xinche_dianxiao_xiaoshou':
        ctx['type'] = 'xinche_dianxiao_xiaoshou'
        ctx['tabletl'] = ['日期','用户','新增销售线索','留档量','试乘试驾量','订单量','交车量']
        #ctx['db'] = TableXincheDianxiaoXiaoshou.objects.all()

        # get user name list
        users = User.objects.all()
        users_list = []
        for user in users:
            user_name = user.username
            users_list.append(user_name)
        ctx['users'] = users_list

        context = RequestContext(request, ctx)
        template = loader.get_template('dqadmin/db_view.html')
        return HttpResponse(template.render(context))
    else:
        return HttpResponse('failed to load data.')

# handler query request
def db_get_table(request):
    if request.method == 'POST':
        try:
            rv_dic = {}
            #print request.POST

            # Get conditions
            rq_user = request.POST['username']
            rq_table = request.POST['tablename']

            # Init
            # Bumen - xinche
            # -- S1
            FIELD_zhanting_xiaoshou = ['date','username','xiaoshou_xiansuo','liu_dang_liang','shi_jia_liang','ding_dan_liang','jiao_che_liang']
            TITLE_zhanting_xiaoshou = ['日期','用户名','销售线索','留档量','试驾量','订单量','交车量']
            # -- S2
            FIELD_dianxiao_xiaoshou = ['date','username','xiaoshou_xiansuo','liu_dang_liang','shi_jia_liang','ding_dan_liang','jiao_che_liang']
            TITLE_dianxiao_xiaoshou = ['日期','用户名','销售线索','留档量','试驾量','订单量','交车量']
            # -- S3
            FIELD_xiansuo_laiyuan = ['date','username','ziran_daodian','dcc','waibu_tuozhan','qita']
            TITLE_xiansuo_laiyuan = ['日期','用户名','自然到店','DCC','外部拓展','其他']
            # -- S4
            FIELD_xiaoshou_xiansuo = ['date','username','zhanting_xiaoshou','dcc_xiaoshou','er_wang','da_ke_hu']
            TITLE_xiaoshou_xiansuo = ['日期','用户名','展厅销售','DCC销售','二网','大客户']
            # -- S5
            FIELD_kuling_tongji = ['date','username','kl_0_30','kl_30_60','kl_60_90','kl_90_120','kl_120_150','kl_150_180','kl_180_270','kl_270_360','kl_360_0']
            TITLE_kuling_tongji = ['日期','用户名','小于30天','30-60天','60-90天','90-120天','120-150天','150-180天','180-270天','270-360天','大于360天']
            # -- S7
            FIELD_shangwu_zhengce = ['date','username','shangwu_zhengce','shiji_xiaoliang','wan_cheng_lv']
            TITLE_shangwu_zhengce = ['日期','用户名','商务政策（新车销量）','实际销量','完成率']

            if rq_table == 'zhanting_xiaoshou':
                print 'Rq table',rq_table
                data = serializers.serialize("xml", TableXincheZhantingXiaoshou.objects.all())
                field_array = FIELD_zhanting_xiaoshou
                title_array = TITLE_zhanting_xiaoshou
                print data
            elif rq_table == 'dianxiao_xiaoshou':
                print 'Rq table',rq_table
                data = serializers.serialize("xml", TableXincheDianxiaoXiaoshou.objects.all())
                field_array = FIELD_dianxiao_xiaoshou
                title_array = TITLE_dianxiao_xiaoshou
                print data
            elif rq_table == 'xiaoshou_xiansuo':
                print 'Rq table',rq_table
                data = serializers.serialize("xml", TableXincheXiaoshouXiansuo.objects.all())
                field_array = FIELD_xiaoshou_xiansuo
                title_array = TITLE_xiaoshou_xiansuo
                print data
            elif rq_table == 'xiansuo_laiyuan':
                print 'Rq table',rq_table
                data = serializers.serialize("xml", TableXincheXiansuoLaiyuan.objects.all())
                field_array = FIELD_xiansuo_laiyuan
                title_array = TITLE_xiansuo_laiyuan
                print data
            elif rq_table == 'kuling_tongji':
                print 'Rq table',rq_table
                data = serializers.serialize("xml", TableXincheKulingTongji.objects.all())
                field_array = FIELD_kuling_tongji
                title_array = TITLE_kuling_tongji
                print data
            elif rq_table == 'shangwu_zhengce':
                print 'Rq table',rq_table
                data = serializers.serialize("xml", TableXincheShangwuZhengce.objects.all())
                field_array = FIELD_shangwu_zhengce
                title_array = TITLE_shangwu_zhengce
                print data
            else:
                return HttpResponse('DB Error')

            # Append meta
            #meta = ET.Element("meta")


            # XML
            root = ET.fromstring(data)
            meta_str = ''
            meta_str += r'<meta>'

            for it in field_array:
                meta_str += r'<tbfield>'
                meta_str += it
                meta_str += r'</tbfield>'
            for tl in title_array:
                meta_str += r'<tbtitle>'
                meta_str += tl
                meta_str += r'</tbtitle>'

            meta_str += r'</meta>'
            meta_tree = ET.fromstring(meta_str)
            root.append(meta_tree)

            #return HttpResponse('<h1>Hello World</h1>')
            #return HttpResponse('Hello Worl')
            #print ET.tostring(root)
            new_tree = ET.tostring(root)
            return HttpResponse(new_tree, content_type="application/xml")
            #return HttpResponse(rv, content_type="application/json")
        except Exception, e:
            err = traceback.format_exc()
            rv_dic['result'] = 'Err: %s,%s' % (err, request.FILES)
            rv = json.dumps(rv_dic)
            return HttpResponse(rv, content_type="application/json")
'''
    ctx={}
    if table_name == 'xinche_dianxiao_xiaoshou':
        ctx['type'] = 'xinche_dianxiao_xiaoshou'
        ctx['tabletl'] = ['日期','用户','新增销售线索','留档量','试乘试驾量','订单量','交车量']
        ctx['db'] = TableXincheDianxiaoXiaoshou.objects.all()
        context = RequestContext(request, ctx)
        template = loader.get_template('dqadmin/db_view.html')
        return HttpResponse(template.render(context))
    else:
        return HttpResponse('failed to load data.')
'''

def db_compare_view(request):
    ctx={}
    if not request.user.is_authenticated():
        ctx['result'] = 'not authenticated'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/user_invalid.html')
        return HttpResponse(template.render(context))
    #ctx['db'] = TableXincheDianxiaoXiaoshou.objects.all()
    context = RequestContext(request, ctx)
    template = loader.get_template('dqadmin/db_compare_view.html')
    return HttpResponse(template.render(context))

def dq_report_in_view(request, customername):
    if request.method == 'POST':
        try:
            rv_dic = {}

            # For debug
            print request.POST
            print request.FILES
            #flog.info('Upload File, User-%s, Job_id:%s File:' % (request.user.username, job_id))
            #flog.info('Get file 1')
            #flog.info(request.FILES)

            #print 'Job-Bumen: %s' % job.job_bu_men

            # Step 2, save the uploaded file to fs
            #
            # Save the file to Models directly, not use Forms.
            #   1. create model
            #   2. init username, last_modified, bu_men, file_type
            #   3. save file to fs
            new_report_file = ReportFile(uploadfile = request.FILES['uploadfile'],
                                user=request.user,
                                customer_name=customername,
                                upload_id=uuid4().hex,
                                )
            re = new_report_file.init_info()
            if re != 'success':
                rv_dic['result'] = 'Err: fail to upload'
                rv = json.dumps(rv_dic)
                return HttpResponse(rv, content_type="application/json")
            new_report_file.save()

            # Step 3, get the file abs path on FS, then read it out via xlrd
            # Dump the file to 'TableModel'
            #fpath = new_report_file.get_abs()

            # Step 4, parse the file
            # Note: the 1:1 relation
            #   Job - xls file - form
            # For now, we cover the tables below:
            #   N1-TableXincheZhantingXiaoshou
            #   N2-TableXincheDiaoxiaoXiaoshou
            #   N3-To do
            #   N4-TableXincheXiaoshouXiansuo
            #   N5-To do
            #   N6-To do
            #   N7-To do
            # if Bu_men is xin_che
            rv_dic = {'result':'上传成功'}

            #xml = request.FILES['uploadfile']
            #print xml
            #print rv['result']
            #with open('/tmp/tmp.txt', 'wb+') as destination:
            #    for chunk in fd.chunks():
            #        destination.write(chunk)

            rv = json.dumps(rv_dic)
            return HttpResponse(rv, content_type="application/json")
        except Exception, e:
            err = traceback.format_exc()
            print err
            rv_dic['result'] = 'Err: %s,%s' % (err, request.FILES)
