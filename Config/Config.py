# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 13:44'
# file : 'Config.py'
# Summary : ''

config = 'local'  # online，test，local，sam

if config == 'sam':  # ainiruoxia 环境配置
    class mysql_config:
        host = 'localhost'
        port = 3306
        user = 'root'
        pwd = '123456'
        db = 'customer_service_systems'


    class redis_config:
        host = 'localhost'
        port = 6379
        pwd = ''


    class elasticsearch:
        host = '192.168.1.10'
        port = 9200
        user = ''
        pw = ''


    class kafka:
        host = '192.168.1.141'
        port = 9092


    class zookeeper:
        host = '192.168.1.141'
        port = 2181
elif config == 'online':  # 正式环境配置
    class mysql_config:
        host = '192.168.1.10'
        port = 3306
        user = 'root'
        pwd = ''
        db = 'customer_service_systems'


    class redis_config:
        host = '192.168.1.10'
        port = 6379
        pwd = 'shenyancha!!!.'


    class elasticsearch:
        host = '192.168.1.10'
        port = 9200
        user = ''
        pw = ''


    class kafka:
        host = '192.168.1.141'
        port = 9092


    class zookeeper:
        host = '192.168.1.141'
        port = 2181
elif config == 'test':  # 测试环境配置
    class mysql_config:
        host = '192.168.1.10'
        port = 3306
        user = 'root'
        pwd = ''
        db = 'customer_service_systems'


    class redis_config:
        host = '192.168.1.10'
        port = 6379
        pwd = 'shenyancha!!!.'


    class elasticsearch:
        host = '192.168.1.10'
        port = 9200
        user = ''
        pw = ''


    class kafka:
        host = '192.168.1.141'
        port = 9092


    class zookeeper:
        host = '192.168.1.141'
        port = 2181
else:  # company环境配置
    class mysql_config:
        host = '192.168.1.10'
        port = 3306
        user = 'root'
        pwd = ''
        db = 'customer_service_systems'


    class redis_config:
        host = '192.168.1.10'
        port = 6379
        pwd = 'shenyancha!!!.'


    class elasticsearch:
        host = '192.168.1.10'
        port = 9200
        user = ''
        pw = ''


    class kafka:
        host = '192.168.1.141'
        port = 9092


    class zookeeper:
        host = '192.168.1.141'
        port = 2181

settings = {
    'cookie_secret': '@SAM&Chat_Server_Systems_V1.0',  # cookie秘钥
    'login_url': '/login',
}

SESSION_TYPE = 'redis'  # redis, cache
EXPIRE_TIME = 7 * 60 * 60 * 24  # 7天
