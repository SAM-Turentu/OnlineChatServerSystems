# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 13:46'
# file : 'HomeController.py'
# Summary : ''


import logging
from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Infrastructure.Utils.RedisImpl import RedisStringImpl
from Infrastructure.Utils.ResponseComm import ReturnResponse
from Model.Account.AccountModel import user_save


class HomeHandler(BaseRequestHandler):

    async def get(self):
        returnResponse = ReturnResponse(self)
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
