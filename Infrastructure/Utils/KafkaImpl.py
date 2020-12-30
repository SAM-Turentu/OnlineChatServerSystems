# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/30 14:48'
# file : 'KafkaImpl.py'
# Summary : ''

from Config import Config
from kafka import KafkaProducer
from pykafka import KafkaClient


def kafka_conn():
    """将消息存入kafka"""
    producer = KafkaProducer(bootstrap_servers=['192.168.1.141:9092'])
    for i in range(3):
        msg = b'msg %d' % i
        print(msg)
        producer.send('test', msg)
    producer.close()


# kafka_conn()


client = KafkaClient(hosts=f'{Config.kafka.host}: {Config.kafka.port}')
"""获取所有topic"""
for topic in client.topics:
    print(topic)
print(client.brokers)

"""查看broker信息"""
for n in client.brokers:
    host = client.brokers[n].host
    port = client.brokers[n].port
    id = client.brokers[n].id
    print(f'host={host} | port={port} | broker.id={id}')

topic = client.topics['test']
"""消费kafka"""
consumer = topic.get_simple_consumer(consumer_group='test', reset_offset_on_start=True)
for msg in consumer:
    print(msg)
    if msg is not None:
        print('>>>>>>>>>>', msg.offset)
        print('>>>>>>>>>>', msg.value.decode())

"""从zookeeper消费kafka"""
balanced_consumer = topic.get_balanced_consumer(consumer_group='test', auto_commit_enable=True, reset_offset_on_start=True, zookeeper_connect=f'{Config.zookeeper.host}:{Config.zookeeper.port}')
for msg in balanced_consumer:
    if msg is not None:
        print(msg.offset, msg.value.decode())
