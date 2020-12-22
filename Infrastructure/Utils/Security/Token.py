# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/10 10:11'
# file : 'Token.py'
# Summary : '产生Token，Token验证'


import base64
import datetime
import hmac
import time

import jwt


async def generate_token(key, expire_day):
    time_int = time.time()
    expire_str = str(time_int + 60 * 60 * 24 * expire_day)
    sha1_tshexstr = hmac.new(key.encode('utf-8'), expire_str.encode('utf-8'), 'sha1').hexdigest()
    token = expire_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode('utf-8'))
    return b64_token.decode('utf-8')


async def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        # token 无效
        return False
    time_str = token_list[0]
    if float(time_str) < time.time():
        # 超时
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode('utf-8'), time_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # 验证失败
        return False
    return True


class Token(object):

    @staticmethod
    def create_token(user_info=None):
        if user_info is None:
            user_info = {'userId': '123', 'level': 1, 'loginTime': '', 'userName': 'test', 'phone': '13100000000'}
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),  # 7天过期
                'iat': datetime.datetime.utcnow(),  # 发行时间
                'data': user_info,  # user info
            }
            return str(jwt.encode(payload, 'key', algorithm='HS256'), 'utf-8')
        except Exception as e:
            print(e)

    @staticmethod
    def verify_bearer_token(token):
        payload = jwt.decode(token, 'key', algorithms=['HS256'])
        if payload:
            return payload
        return False
