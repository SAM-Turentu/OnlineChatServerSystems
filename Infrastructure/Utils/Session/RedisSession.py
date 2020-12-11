# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/10 10:13'
# file : 'RedisSession.py'
# Summary : ''
import asyncio

from tornado import gen
from Config.RedisConn import select_redis_db


class RedisSession(object):

    def __init__(self, handler):
        self.redis = select_redis_db.redis_session_2()
        self.handler = handler

    async def sam_test_asnyc(self):
        try:
            test = await self.redis
            test.set('test', 'test123')
            return 123
        except Exception as e:
            print(e)

    async def get_item(self, key):
        ...

    async def set_item(self, key, value):
        ...

    async def del_item(self, key):
        ...


# class sam_test_async():
#
#     def __init__(self):
#         # self.redis = await gen.sleep(1)
#         # self.call = sam_async()
#         self.call = sam_async()
#         # self.client = select_redis_db()
#         # self.redis = self.client.redis_session_2()
#
#     async def sam(self):
#         try:
#             # id = await self.call.test()
#             id = await self.call.test()
#
#             print(id.get('id'))
#             print(id.get('func'))
#             # await self.redis
#         except Exception as e:
#             print(e)
#
#
# async def sam_async_func():
#     try:
#         await gen.sleep(1)
#         print(111)
#         return await gen.sleep(1)
#     except Exception as e:
#         print(e)
#
#
# class sam_async():
#
#     async def test(self):
#         try:
#             id = await sam_async_func()
#             print(id)
#             func = await sam()
#             return {'id': 222, 'func': func}
#         except Exception as e:
#             print(e)
#
#
# async def sam():
#     return 333
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(sam_test_async().sam())
