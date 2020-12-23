# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/22 16:10'
# file : 'ResponseComm.py'
# Summary : ''


class ReturnResponse:

    def __init__(self, handler, code=80001, message='', data: dict = None, status=True):
        self.handler = handler
        self.code = code
        self.status = status
        self.data = data
        self.message = message

    def __del__(self):
        print('释放对象时调用该方法!')
        return self.handler.write({
            'code': self.code,
            'status': self.status,
            'message': self.message,
            'data': self.data,
        })

    def ret_success(self, data: dict = None, message='success'):
        """80001：请求成功，有资源   80002：请求成功，没有资源"""
        code = 80001 if data is not None and data != '' else 80002
        self.code = code
        self.status = True
        self.data = data
        self.message = message

    def ret_no_find(self, message='no find'):
        """请求成功，没有资源返回"""
        self.code = 80002
        self.status = True
        self.message = message
        self.data = None

    def ret_failure(self, message='failure', data: dict = None):
        """请求失败"""
        self.code = 80004
        self.status = False
        self.message = message
        self.data = data

    def ret_exception(self, message=''):
        """请求异常"""
        self.code = 80004
        self.status = False
        self.message = message
        self.data = None

    def ret_no_login(self, message='no login', data: dict = None):
        """没有登录"""
        self.code = 80006
        self.status = True
        self.message = message
        self.data = data

    def ret_invalid_token(self, message='invalid token'):
        """Token无效（过期，非token等）"""
        self.code = 80007
        self.status = True
        self.message = message
        self.data = None

    def ret_no_token(self, message='no token'):
        """没有Token"""
        self.code = 80007
        self.status = False
        self.message = message
        self.data = None

    @staticmethod
    def ret_not_token(self, message=''):
        ...
