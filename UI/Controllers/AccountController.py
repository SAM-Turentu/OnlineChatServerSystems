# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 16:19'
# file : 'AccountController.py'
# Summary : ''


# 用户 一般来源于接口数据
# 客服注册和登录,非用户
import datetime
import logging
import uuid

from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Infrastructure.Utils.Security.Token import Token
from UI.Services.AccountService import AccountService


class RegisterHandler(BaseRequestHandler):
    """注册"""

    async def get(self):
        try:
            phone = self.get_argument('phone')
            password = self.get_argument('password')
            user_name = self.get_argument('user_name')
            loginTime = datetime.datetime.utcnow()
            userId = uuid.uuid4()
            accountService = AccountService()
            await accountService.register_user(phone, password, user_name)
            user_info = {'userId': userId, 'level': 1, 'loginTime': loginTime, 'userName': user_name, 'phone': phone}
            token = Token.create_token(user_info=user_info)  # 创建token
            return self.write(token)
        except Exception as e:
            logging.error(e)

    # async def post(self):
    #     ...
    #
    # async def put(self):
    #     ...
    #
    # async def delete(self):
    #     ...


class LoginHandler(BaseRequestHandler):
    """登录"""

    async def get(self):
        try:
            ...
        except Exception as e:
            logging.error(e)

    async def post(self):
        try:
            ...
        except Exception as e:
            logging.error(e)


class LogoutHandler(BaseRequestHandler):
    """退出登录"""

    async def get(self):
        ...


class ForgetPasswordHandler(BaseRequestHandler):
    """忘记密码"""

    async def get(self):
        ...


class ModifyPasswordHandler(BaseRequestHandler):
    """修改密码"""

    async def get(self):
        ...


class UpdateHeadImageHandler(BaseRequestHandler):
    """上传头像"""

    async def get(self):
        ...


class UpdateUserInfoHandler(BaseRequestHandler):
    """更新账号个人信息"""

    async def get(self):
        ...


# Model Handler
class ModelHandler(BaseRequestHandler):
    """ModelHandler"""

    async def get(self):
        try:
            ...
        except Exception as e:
            print(e)

    async def post(self):
        try:
            ...
        except Exception as e:
            print(e)
