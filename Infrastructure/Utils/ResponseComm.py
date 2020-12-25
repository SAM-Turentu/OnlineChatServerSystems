# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/22 16:10'
# file : 'ResponseComm.py'
# Summary : ''
import logging


class ReturnResponse:

    def __init__(self, handler, code=80001, message='', data: dict = None, status=True, exception=None):
        self.handler = handler
        self.code = code
        self.status = status
        self.data = data
        self.message = message
        self.exception = exception

    # def __del__(self):
    #     if self.code == 80005:
    #         logging.error(self.exception)  # 异常日志系统待写
    #     return self.handler.write({
    #         'code': self.code,
    #         'status': self.status,
    #         'message': self.message,
    #         'data': self.data,
    #     })

    def class_del(self):
        if self.code == 80005:
            logging.error(self.exception)  # 异常日志系统待写
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
        self.class_del()

    def ret_no_find(self, message='no find'):
        """请求成功，没有资源返回"""
        self.code = 80002
        self.status = True
        self.message = message
        self.data = None
        self.class_del()

    def ret_failure(self, message='failure', data: dict = None):
        """请求失败"""
        self.code = 80004
        self.status = False
        self.message = message
        self.data = data
        self.class_del()

    def ret_exception(self, message='', exception=None):
        """请求异常"""
        self.code = 80005
        self.status = False
        self.message = message
        self.data = None
        self.exception = exception
        self.class_del()

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
        self.class_del()

    def ret_no_token(self, message='no token'):
        """没有Token"""
        self.code = 80007
        self.status = False
        self.message = message
        self.data = None
        self.class_del()

    @staticmethod
    def ret_not_token(self, message=''):
        ...
