# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 16:19'
# file : 'AccountController.py'
# Summary : ''


from Infrastructure.Core.HttpRequest import BaseRequestHandler


class RegisterHandler(BaseRequestHandler):
    """注册"""

    async def get(self):
        ...

    async def post(self):
        ...


class LoginHandler(BaseRequestHandler):
    """登录"""

    async def get(self):
        ...

    async def post(self):
        ...


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
