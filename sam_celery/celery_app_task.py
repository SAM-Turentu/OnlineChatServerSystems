# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/8 13:34'
# file : 'celery_app_task.py'
# Summary : ''


from celery import Celery

broker = 'redis://:shenyancha!!!.@192.168.1.10:6379/0'
backend = 'redis://:shenyancha!!!.@192.168.1.10:6379/1'
app = Celery('celery_task', backend=backend, broker=broker)


@app.task()
def add(x, y):
    z = x + y
    print(z)
    return z
