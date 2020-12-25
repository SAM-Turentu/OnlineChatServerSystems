# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 16:19'
# file : 'AccountController.py'
# Summary : ''


# 注册应该单独一个微服务
# 用户 一般来源于接口数据
# 客服注册和登录,非用户


import datetime
import logging
import uuid

from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Infrastructure.Utils.ResponseComm import ReturnResponse
from Infrastructure.Utils.Security.Token import Token
from UI.Services.AccountService import AccountService


class RegisterHandler(BaseRequestHandler):
    """注册"""

    async def get(self):
        returnResponse = ReturnResponse(self)
        try:
            phone = self.get_argument('phone')
            sms_code = self.get_argument('sms_code')
            # 使用手机验证码登录并注册，登录注册合并为一个接口
            loginTime = datetime.datetime.utcnow()
            user_id = uuid.uuid4()

            accountService = AccountService()
            await accountService.register_user(phone, 'password', 'user_name')
            user_info = {'user_id': user_id, 'level': 1, 'loginTime': loginTime, 'userName': 'user_name', 'phone': phone}
            token = Token.create_token(user_info=user_info)  # 创建token
            returnResponse.ret_success(data={'token': token}, message='')
            # return self.write(token)
        except Exception as e:
            returnResponse.ret_exception(exception=e, message='')

    # async def post(self):
    #     ...
    #
    # async def put(self):
    #     ...
    #
    # async def delete(self):
    #     ...


class Register_LoginHandler(BaseRequestHandler):
    """使用手机验证码登录/注册，登录/注册合并为一个接口"""

    async def post(self):
        returnResponse = ReturnResponse(self)
        """使用弹框登录/注册"""
        try:
            phone = self.get_body_argument('phone')
            sms_code = self.get_body_argument('sms_code')
            area_code = self.get_body_argument('area_code', None)  # area_code 验证
            area_code = '86' if area_code is None or area_code == '' else area_code
            loginTime = datetime.datetime.utcnow()

            accountService = AccountService()

            if sms_code:
                """对比短信验证码"""
                ...

            """查询该用户是否已注册"""
            user_info = await accountService.get_user_info(phone=phone)
            if user_info:  # 创建token
                # 更新loginTime
                user_id = user_info.user_id
                user_info = {'user_id': user_id, 'level': 1, 'loginTime': loginTime, 'userName': 'user_name', 'phone': phone}
                token = Token.create_token(user_info=user_info)  # 创建token

            else:  # 添加新用户，并创建token
                user_id = uuid.uuid4()
                # user_id, phone, area_code
                await accountService.register_user(user_id, phone, area_code)

                user_info = {'user_id': user_id, 'level': 1, 'loginTime': loginTime, 'userName': 'user_name', 'phone': phone}
                token = Token.create_token(user_info=user_info)  # 创建token
            returnResponse.ret_success(data={'token': token})
        except Exception as e:
            returnResponse.ret_exception(exception=e, message='服务异常，请稍后重试!')


class LoginHandler(BaseRequestHandler):
    """登录"""

    async def get(self):
        returnResponse = ReturnResponse(self)
        try:
            phone = self.get_argument('phone')
            password = self.get_argument('pw')
            user_name = self.get_argument('user_name')
            loginTime = datetime.datetime.utcnow()
            user_id = uuid.uuid4()

            user_info = {'user_id': user_id, 'level': 1, 'loginTime': loginTime, 'userName': user_name, 'phone': phone}
            token = Token.create_token(user_info=user_info)  # 创建token
            returnResponse.ret_success(data={'token': token}, message='')
        except Exception as e:
            logging.error(e)
            returnResponse.ret_exception(e)

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
