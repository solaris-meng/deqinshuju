# -*- coding:utf-8 -*-


import xlrd
import traceback
from xlrd import open_workbook
from .models import TableXincheZhantingXiaoshou
from .models import TableXincheDianxiaoXiaoshou
from .models import TableXincheXiaoshouXiansuo
from .config import *

def XincheFileHandler(fpath, user, job):
    try:
        flog.info('Process the file, %s, %s, %s' % (fpath, user, job))
        rv_dic = {}
        item = TableXincheZhantingXiaoshou()
        xls = open_workbook(fpath, 'r')

        #for st in xls.sheets():
        #    print 'Sheet:',st.name
        st_all = xls.sheets()

        # Sheet 1
        #  --TableXincheZhantingXiaoshou
        s1 = st_all[1]
        for row in range(s1.nrows):
            if row == 0:
                # Do some checks
                continue
            # Check if this row is valid
            xiaoshou_xiansuo = s1.cell(row, 1).value
            idate = xlrd.xldate.xldate_as_datetime(s1.cell(row, 0).value, 0)
            #print "find date:",idate
            #r = TableXincheZhantingXiaoshou.objects.get(date=idate)
            #print r
            #continue
            item1 = TableXincheZhantingXiaoshou()
            item1.date = idate
            item1.xiaoshou_xiansuo = s1.cell(row, 1).value
            item1.liu_dang_liang = s1.cell(row, 2).value
            item1.shi_jia_liang = s1.cell(row, 3).value
            item1.ding_dan_liang = s1.cell(row, 4).value
            item1.jiao_che_liang = s1.cell(row, 5).value

            item1.user = user
            item1.job = job
            #print item.date
            item1.save()
                
        # Sheet 2
        #  --TableXincheDianxiaoXiaoshou
        s2 = st_all[2]
        for row in range(s2.nrows):
            if row == 0:
                # Do some checks
                continue
            # Check if this row is valid
            #xiaoshou_xiansuo = s2.cell(row, 1).value
            idate = xlrd.xldate.xldate_as_datetime(s2.cell(row, 0).value, 0)
            #print "find date:",idate
            #r = TableXincheZhantingXiaoshou.objects.get(date=idate)
            #print r
            #continue
            item2 = TableXincheDianxiaoXiaoshou()
            item2.date = xlrd.xldate.xldate_as_datetime(s2.cell(row, 0).value, 0)
            item2.xiaoshou_xiansuo = s2.cell(row, 1).value
            item2.liu_dang_liang = s2.cell(row, 2).value
            item2.shi_jia_liang = s2.cell(row, 3).value
            item2.ding_dan_liang = s2.cell(row, 4).value
            item2.jiao_che_liang = s2.cell(row, 5).value

            item2.user = user
            item2.job = job
            #print item.date
            item2.save()

        # Sheet 4
        #  --TableXincheXiaoshouXiansuo
        s4 = st_all[4]
        for row in range(s4.nrows):
            if row == 0:
                # Do some checks
                continue
            # Check if this row is valid
            #xiaoshou_xiansuo = s4.cell(row, 1).value
            #print "find date:",idate
            #r = TableXincheZhantingXiaoshou.objects.get(date=idate)
            #print r
            #continue
            item4 = TableXincheXiaoshouXiansuo()
            item4.date = xlrd.xldate.xldate_as_datetime(s4.cell(row, 0).value, 0)
            item4.zhanting_xiaoshou = s4.cell(row, 1).value
            item4.dcc_xiaoshou = s4.cell(row, 2).value
            item4.er_wang = s4.cell(row, 3).value
            item4.da_ke_hu = s4.cell(row, 4).value

            item4.user = user
            item4.job = job
            #print item.date
            item4.save()
        return {'result':'success'}
    except Exception, e:
        err = traceback.format_exc()
        return {'result':'error %s' % err}
