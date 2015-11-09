# encoding:utf-8



from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

import json
import traceback
from uuid import uuid4

from .forms import UploadFileForm
from .models import UploadFile
from .models import TableXincheZhantingXiaoshou
from .models import TableXincheDianxiaoXiaoshou
from .models import TableXincheXiaoshouXiansuo
from .config import *
from .filehandler import XincheFileHandler

from job.models import Job


# Create your views here.
def data_in_view(request):
    flog.info("PV, data-in, ")
    #form = UploadFileForm
    ctx = {}
    ctx['job'] = Job.objects.all()
    context = RequestContext(request, ctx)
    template = loader.get_template('data/data_in.html')
    return HttpResponse(template.render(context))

def data_in_handler(request, job_id):
    flog.info("PV, data-in-handler, job_id:%s" % job_id)
    if request.method == 'POST':
        try:
            rv_dic = {}

            # For debug
            #print request.POST
            #print request.FILES
            flog.info('Upload File, User-%s, Job_id:%s File:' % (request.user.username, job_id))
            flog.info(request.FILES)

            # Step 1, get the Job per the job_id
            job = Job.objects.get(job_id=job_id)
            #print 'Job-Bumen: %s' % job.job_bu_men

            # Step 2, save the uploaded file to fs
            #
            # Save the file to Models directly, not use Forms.
            #   1. create model
            #   2. init username, last_modified, bu_men, file_type
            #   3. save file to fs
            new_upload_file = UploadFile(uploadfile = request.FILES['uploadfile'],
                                user=request.user,
                                upload_id=uuid4().hex)
            re = new_upload_file.init_info(job.job_bu_men)
            if re != 'success':
                rv_dic['result'] = 'Err: fail to upload'
                rv = json.dumps(rv_dic)
                return HttpResponse(rv, content_type="application/json")
            new_upload_file.save()

            # Step 3, get the file abs path on FS, then read it out via xlrd
            # Dump the file to 'TableModel'
            fpath = new_upload_file.get_abs()

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
            rv_dic = XincheFileHandler(fpath,
                        user=request.user,
                        job=job)

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
            rv_dic['result'] = 'Err: %s,%s' % (err, request.FILES)
            rv = json.dumps(rv_dic)
            return HttpResponse(rv, content_type="application/json")


def data_in_status_view(request, bu_men):
    flog.info("PV, data-in-status, ")
    #form = UploadFileForm
    ctx = {}

    if bu_men == 'xin_che':
        ctx['TableXincheZhantingXiaoshou'] = TableXincheZhantingXiaoshou.objects.all()
        ctx['TableXincheDianxiaoXiaoshou'] = TableXincheDianxiaoXiaoshou.objects.all()
        ctx['TableXincheXiaoshouXiansuo'] = TableXincheXiaoshouXiansuo.objects.all()
        template = loader.get_template('data/data_in_status.html')
    else:
        return HttpResponse('Error')

    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))
