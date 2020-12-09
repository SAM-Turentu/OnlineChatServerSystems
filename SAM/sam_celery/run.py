# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/8 13:36'
# file : 'run.py'
# Summary : ''

from SAM.sam_celery.celery_app_task import app

if __name__ == '__main__':
    app.worker_main(argv=['worker'])
