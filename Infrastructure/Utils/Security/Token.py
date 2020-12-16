# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/10 10:11'
# file : 'Token.py'
# Summary : '产生Token，Token验证'


import base64
import hmac
import time


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
        raise ValueError
        # return False
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
