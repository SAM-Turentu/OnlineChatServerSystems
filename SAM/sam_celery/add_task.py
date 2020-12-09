# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/8 13:35'
# file : 'add_task.py'
# Summary : ''

from SAM.sam_celery.celery_app_task import add

result = add.delay(4, 5)
print(result.id)
