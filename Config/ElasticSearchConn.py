# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/28 10:24'
# file : 'ElasticSearchConn.py'
# Summary : '日志系统存储'


from Config import Config
from elasticsearch import Elasticsearch


def ElasticsearchConn():
    conn = Elasticsearch(hosts={'host': Config.elasticsearch.host, 'port': Config.elasticsearch.port}, sniff_timeout=15)
    return conn


ElasticsearchConn()
