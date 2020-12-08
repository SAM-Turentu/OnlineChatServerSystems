# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/8 13:44'
# file : 'result.py'
# Summary : ''


from celery.result import AsyncResult
from sam_celery.celery_app_task import app

# async_r = AsyncResult(id='e6a1d0e9-dc3b-496a-aa0f-8bfd694fcc1e', app=app)
async_r = AsyncResult(id='048aaac9-82db-460e-9db7-19bc42978146', app=app)

if async_r.successful():
    result = async_r.get()
    print(result)
elif async_r.failed():
    print('执行失败')
elif async_r.status == 'PENDING':
    print('任务等待中被执行')
elif async_r.status == 'RETRY':
    print('任务异常后正在重试')
elif async_r.status == 'STARTED':
    print('任务已经开始被执行')
