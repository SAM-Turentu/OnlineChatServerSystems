# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/10 10:13'
# file : 'RedisSession.py'
# Summary : ''


from Config.RedisConn import select_redis_db


class RedisSession(object):

    def __init__(self, handler):
        self.handler = handler
        # self.redis = select_redis_db()
        # self.redis = await select_redis_db.redis_session_2()

    async def init(self):
        self.redis = await select_redis_db.redis_session_2()

    async def sam_test_asnyc(self):
        try:
            await self.init()
            # client = await self.redis.redis_session_2()
            # await client.set('test_sam_1', '2')
            await self.redis.set('test_sam_1', '2')
            return 123
        except Exception as e:
            print(e)

    async def get_item(self, key):
        ...

    async def set_item(self, key, value):
        ...

    # async def del_item(self, key):
    #     client = await self.redis.redis_session_2()

