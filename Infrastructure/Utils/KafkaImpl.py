# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/30 14:48'
# file : 'KafkaImpl.py'
# Summary : ''
import json

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


class KafkaImpl(object):

    def __init__(self):
        self.client = KafkaClient(hosts=f'{Config.kafka.host}: {Config.kafka.port}')
        self.producer = KafkaProducer(bootstrap_servers=[f'{Config.kafka.host}: {Config.kafka.port}'], retries=3)

    def producer(self, topic, msg):
        """生成消息"""
        msg = bytes(msg)
        self.producer.send(topic, msg)

    def get_brokers(self):
        """获取所有的 broker"""
        broker_list = []
        for n in self.client.brokers:
            broker_list.append(
                {
                    'host': self.client.brokers[n].host,
                    'port': self.client.brokers[n].port,
                    'id': self.client.brokers[n].id,
                }
            )
        return broker_list

    def get_topics(self):
        """获取所有的 topic"""
        topic_list = []
        for topic in self.client.topics:
            topic_list.append(topic)
        return topic_list

    def consumer_direct(self, topic):
        """直接消费 kafka，没有标记已使用"""
        consumer_group = topic
        if topic in self.get_topics():
            topic = self.client.topics[topic]
            consumer = topic.get_simple_consumer(consumer_group=consumer_group, reset_offset_on_start=True)
            message = []
            for msg in consumer:
                if msg is not None:
                    message.append({'offset': msg.offset, 'value': msg.value.decode()})
                    print('>>>>>>>>>>', msg.offset)
                    print('>>>>>>>>>>', msg.value.decode())
            return message

    def consumer_zookeeper(self, topic):
        """从 zookeeper 消费 kafka"""
        consumer_group = topic
        topic = self.client.topics[topic]
        balanced_consumer = topic.get_balanced_consumer(consumer_group=consumer_group, auto_commit_enable=True, reset_offset_on_start=True, zookeeper_connect=f'{Config.zookeeper.host}:{Config.zookeeper.port}')
        message = []
        for msg in balanced_consumer:
            if msg is not None:
                message.append({'offset': msg.offset, 'value': msg.value.decode()})
                print(msg.offset, msg.value.decode())
        return message


# kafka_conn()
#
#
# client = KafkaClient(hosts=f'{Config.kafka.host}: {Config.kafka.port}')
# """获取所有topic"""
# for topic in client.topics:
#     print(topic)
# print(client.brokers)
#
# """查看broker信息"""
# for n in client.brokers:
#     host = client.brokers[n].host
#     port = client.brokers[n].port
#     id = client.brokers[n].id
#     print(f'host={host} | port={port} | broker.id={id}')
#
# topic = client.topics['test']
# """消费kafka"""
# consumer = topic.get_simple_consumer(consumer_group='test', reset_offset_on_start=True)
# for msg in consumer:
#     print(msg)
#     if msg is not None:
#         print('>>>>>>>>>>', msg.offset)
#         print('>>>>>>>>>>', msg.value.decode())
#
# """从zookeeper消费kafka"""
# balanced_consumer = topic.get_balanced_consumer(consumer_group='test', auto_commit_enable=True, reset_offset_on_start=True, zookeeper_connect=f'{Config.zookeeper.host}:{Config.zookeeper.port}')
# for msg in balanced_consumer:
#     if msg is not None:
#         print(msg.offset, msg.value.decode())


class Producer(object):

    def __init__(self, KFKServerList=None, ClientId='Producer', Topic='SAM_Test'):
        if KFKServerList is None or KFKServerList == '':
            KFKServerList = [f'{Config.kafka.host}: {Config.kafka.port}']
        self._kwargs = {
            'boostrap_servers': KFKServerList,
            'retries': 3,
            'key_serializer': lambda m: json.dumps(m).encode('utf-8'),
            'value_serializer': lambda m: json.dumps(m).encode('utf-8'),
        }
        self._topic = Topic
        self._producer = KafkaProducer(**self._kwargs)

    def _callback_SendSuccess(self, record_metadata):
        print('发送成功!')
        print(record_metadata.topic)

    def _callback_SendFailed(self):
        print('发送失败!')
