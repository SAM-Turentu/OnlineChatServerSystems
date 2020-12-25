# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/24 11:12'
# file : 'RedisImpl.py'
# Summary : ''


import json
import time
from Config import Config
from Config.RedisConn import select_redis_db, RedisConn


class RedisStringImpl(object):

    def __init__(self):
        self.redis = RedisConn(3)

    async def get_item(self, key):
        redis = await self.redis.AsyncRedisConn()
        value = redis.get(key)
        return value.decode()

    async def set_item(self, key, value, expire: bool = False):
        """默认不设置有效期"""
        redis = await self.redis.AsyncRedisConn()
        if expire:
            expires_time = int(time.time() + Config.EXPIRE_TIME)
            await redis.set(key, value, expires_time)
        else:
            await redis.set(key, value)

    async def del_item(self, key):
        redis = await self.redis.AsyncRedisConn()
        await redis.delete(key)


class RedisHashImpl(object):

    def __init__(self):
        self.redis = RedisConn(3)

    async def get_item(self, name, key):
        result = None
        redis = await self.redis.AsyncRedisConn()
        value = redis.hget(name, key)
        try:
            value = value.decode()
            if value:
                result = json.loads(value)
        except:
            result = value
        return result

    async def set_item(self, name, key, value):
        redis = await self.redis.AsyncRedisConn()
        redis.hset(name, key, value)

    async def del_item(self, name, key):
        redis = await self.redis.AsyncRedisConn()
        redis.hdel(name, key)


class RedisListImpl(object):
    """可把异常信息存入redis List，后期ELK，做成日志系统，严重级别将推送到邮箱，短信等"""

    def __init__(self):
        self.redis = RedisConn(4)

    async def get_item(self, key):
        redis = await self.redis.AsyncRedisConn()
        value = redis.lpop(key)
        if redis.llen(key) == 0:
            value = redis.lpop(key + '_1')
        if value:
            return value.decode()
        return False

    async def set_item(self, key, value):
        redis = await self.redis.AsyncRedisConn()
        if redis.llen(key) > 40 * 100000000:  # 40亿
            redis.lpush(key + '_1', value)
        redis.lpush(key, value)

    async def get_len(self, key):
        redis = await self.redis.AsyncRedisConn()
        redis_len = redis.llen(key)
        return redis_len if redis_len else 0

    async def del_key(self, key):
        redis = await self.redis.AsyncRedisConn()
        await redis.delete(key)
