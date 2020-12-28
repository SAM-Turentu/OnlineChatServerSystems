# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 13:46'
# file : 'HomeController.py'
# Summary : ''


import logging
import time
import traceback

from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Infrastructure.Utils.RedisImpl import RedisStringImpl
from Infrastructure.Utils.ResponseComm import ReturnResponse
from Model.Account.AccountModel import user_save


# def exception_collection(self):
#     print(123)
#     return 'asdf'


# def catch_exception(func):
#     def wrapper(self, *args, **kwargs):
#         try:
#             u = func(self, *args, **kwargs)
#             return u
#         except:
#             print(234)
#             error = traceback.format_exc()
#             t = time.time()
#             print(f'{t}\n{error}')
#
#     return wrapper


# def catch_exception(origin_func):
#     def wrapper(self, *args, **kwargs):
#         try:
#             u = origin_func(self, *args, **kwargs)
#             return u
#         except Exception:
#             self.revive() #不用顾虑，直接调用原来的类的方法
#             return 'an Exception raised.'
#     return wrapper


# class Test(object):
#     def __init__(self):
#         pass
#
#     def revive(self):
#         print('revive from exception.')
#         # do something to restore
#
#     @catch_exception
#     def read_value(self):
#         print('here I will do something.')
#         raise ValueError
#         # do something.
#
#
# if __name__ == '__main__':
#     te = Test()
#     te.read_value()


class HomeHandler(BaseRequestHandler):

    # @exception_collection
    # @catch_exception
    async def get(self):
        returnResponse = ReturnResponse(self)
        # # returnResponse.ret_success(data={'userId': 'a123456', 'userName': 'sam'})
        # a = 12 / 0
        # return self.write(a)
        try:
            redis = RedisStringImpl()
            await redis.set_item('key', 'value')
            await redis.del_item('man')
            # userId = self.get_query_argument('userId')
            # await self.session.set_item('_USERINFO', 'user_info')
            # await user_save()  # 数据层
            # self.write({'userId': userId, 'userName': 'sam'})
            returnResponse.ret_success(data={'userId': 'a123456', 'userName': 'sam'})
        except Exception as e:
            # 异常日志系统待写
            returnResponse.ret_exception(message='', exception=e)

# 获取客户端Mac地址,BS项目无法获取
# def get_owner_mac():
#     source_ip = '114.85.227.163'
#     mac = None
#     ip_dict = {}
#     for line in os.popen('ipconfig /all'):
#         if line.lstrip().startswith('eee'):
#             mac = line.split(':')[1]
#             mac = mac.replace('-', ':')
#         if line.lstrip().startswith('IPv4'):
#             ip = line.split(':')[1]
#             s = re.compile(r'(\d+).(\d+).(\d+).(\d+)')
#             t = s.search(ip)
#             if t:
#                 ip = t.group()
#             ip_dict[ip] = mac
#     if ip_dict.get(source_ip):
#         return ip_dict[source_ip]
#
#
# def get_dstmac():
#     dstip = '114.85.227.163'
#     mac = None
#     s = 'ping ' + dstip
#     os.system(s)
#     a = os.popen('arp -a')
#     for line in os.popen('arp -a'):
#         if line.lstrip().startswith(dstip):
#             s1 = line.split()
#             mac = s1[1].replace('-', ':')
#             print(str(mac))
#     return mac
