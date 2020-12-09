# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/8 11:01'
# file : 'sam_celery_test.py'
# Summary : '芹菜收割机'

from celery import Celery

broker = 'redis://192.168.1.10:6379/0'
backend = 'redis://192.168.1.10:6379/1'
app = Celery('celery_task', backend=backend, broker=broker)


@app.task()
def main(x, y):
    z = x + y
    print(z)
    return z


result = main.delay(4, 5)
print(result.id)


if __name__ == '__main__':
    # main()
    ...
