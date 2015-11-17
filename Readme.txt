
Requirements:
xlrd


用户权限
*普通用户-normal
    -perm-data-add-uploadfile
    -上传excel文件，下载excel文件
    -查看自己的上传进度
*德勤管理员-dqadmin
    -perm-job-can-add-job
    -查看每个用户的上传情况
    -查看数据库
*厂家管理员-coadmin
    -只能查看最简单的上传进度
*超级管理员
    -后台所有权限

数据模型
*Job
-名字-job_name: '9月新车数据采集'
-ID-job_id:
-文件名-job_file_name: '经销商初次信息采集表_新车部门.xlsx'
-文件-job_file: '经销商初次信息采集表_新车部门.xlsx'
-部门-bu_men: '新车'
-状态-status: '未上线'-'上线'-'完成'-'暂停'-'终止'
-开始
-结束
-最后更改
*UploadFile
-文件-uploadfile: '经销商初次信息采集表_新车部门.xlsx'
-用户-User: 上传文件的用户
-上传ID-upload_id: UUID4, 此次上传的唯一标示码
-部门-bu_men: 文件的归属部门
-修改时间-last_modified: 最后修改时间
-上传的用户名-user_name: 方便显示
*JobFinish
-job_id
-

数据表-新车部门
1.xinche_zhanting_xiaoshou
    -username
    -date
    -xiaoshou_xiansuo
    -liu_dang_liang
    -shi_jia_liang
    -ding_dan_liang
    -jiao_che_liang
    --new_created
    --last_modified
2.xinche_dianxiao_xiaoshou
3.xinche_xiansuo_laiyuan
4.xinche_kuling_tongji
5.xinche_hexin_kpi
6.xinche_shangwu_zhengce_wancheng


