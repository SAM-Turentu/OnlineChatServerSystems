# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/10 10:13'
# file : 'RedisSession.py'
# Summary : ''


import json
import random
import string
import time
from hashlib import sha256
from Config.RedisConn import select_redis_db, RedisConn

create_session_id = lambda: sha256((''.join(random.sample(str(string.ascii_letters + string.digits), random.randint(15, 30))) + str(time.time())).encode('utf-8')).hexdigest()


class RedisSession(object):

    def __init__(self, handler):
        self.redis = RedisConn()
        # self.redis = select_redis_db.redis_session_2()
        self.handler = handler

    # async def sam_test_asnyc(self):
    #     try:
    #         redis = await self.redis.redis_session_2()
    #         # redis = await self.redis
    #         redis.set('test', 'test123')
    #         return 123
    #     except Exception as e:
    #         print(e)

    async def get_item(self, key):
        random_str = self.handler.get_cookie(key, None)
        redis = await self.redis.redis_session_2()
        result = redis.hget(random_str, key) if random_str else None
        if result:
            ret_str = str(result, encoding='utf-8')
            try:
                result = json.loads(ret_str)
            except:
                result = ret_str
        return result

    async def set_item(self, key, value):
        redis = await self.redis.redis_session_2()
        random_str = self.handler.get_cookie(key, None)
        self.random_str = random_str if random_str and redis.exists(random_str) else create_session_id()
        value = json.dumps(value) if type(value) == dict else value
        redis.hset(self.random_str, key, value)
        expires_time = int(time.time() + 7 * 60 * 60 * 24)
        await redis.expire(self.random_str, expires_time)
        self.handler.set_cookie(key, self.random_str, expires_time=expires_time - 1)

    async def del_item(self, key):
        redis = await self.redis.redis_session_2()
        random_str = self.handler.get_cookie(key, None)
        redis.hdel(random_str, key)
        self.handler.clear_cookie(key)
