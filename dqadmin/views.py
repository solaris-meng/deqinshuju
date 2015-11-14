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
