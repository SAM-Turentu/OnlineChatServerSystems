# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/10 11:16'
# file : 'RedisConn.py'
# Summary : ''


import logging
import aioredis
import asyncio
from Config import Config


# 暂未使用
async def AsyncRedisConn(db=0):
    try:
        # conn = await aioredis.create_connection(address=f'redis://{Config.redis_config.host}:{Config.redis_config.port}', db=db, password=Config.redis_config.pwd)
        client = await aioredis.create_redis_pool(address=f'redis://{Config.redis_config.host}:{Config.redis_config.port}', password=Config.redis_config.pwd, db=db)
        return client
    except Exception as e:
        print(e)
        logging.error('A connection error occurred with the Redis! Exception info：%s' % e)


class select_redis_db(object):
    """选择redis db"""

    @staticmethod
    async def redis_login_register_1():
        return await AsyncRedisConn(1)

    @staticmethod
    async def redis_session_2():
        return await AsyncRedisConn(2)

    async def redis_test_3(self):
        return await AsyncRedisConn(3)


class RedisConn(object):

    def __init__(self, db=0):
        self.db = db

    async def AsyncRedisConn(self):
        try:
            client = await aioredis.create_redis_pool(address=f'redis://{Config.redis_config.host}:{Config.redis_config.port}', password=Config.redis_config.pwd, db=self.db)
            return client
        except Exception as e:
            logging.error('A connection error occurred with the Redis! Exception info：%s' % e)

    async def redis_login_register_1(self, db=1):
        self.db = db
        return await self.AsyncRedisConn()

    async def redis_session_2(self, db=2):
        self.db = db
        return await self.AsyncRedisConn()

    async def redis_test_3(self, db=3):
        self.db = db
        return await self.AsyncRedisConn()
