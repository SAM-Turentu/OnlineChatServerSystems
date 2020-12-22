# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/22 16:10'
# file : 'ResponseComm.py'
# Summary : ''


class ReturnResponse:

    def __init__(self, code=None, message=None, data=None, status=None):
        self.code = code
        self.status = status
        self.data = data
        self.message = message

    @staticmethod
    def success(data: dict = None, message='success'):
        """请求成功，并有资源返回"""
        return {
            'code': 80001,
            'status': True,
            'data': data,
            'message': message,
        }

    @staticmethod
    def no_find(message='no find', data=None):
        """请求成功，没有资源返回"""
        return {
            'code': 80002,
            'status': True,
            'data': data,
            'message': message,
        }

    @staticmethod
    def failure(message='failure', data=None):
        """请求失败，异常"""
        return {
            'code': 80004,
            'status': False,
            'data': data,
            'message': message,
        }

    @staticmethod
    def no_login(message='no login', data=None):
        """没有登录"""
        return {
            'code': 80006,
            'status': True,
            'data': data,
            'message': message,
        }

    @staticmethod
    def invalid_token(message='invalid token'):
        """Token无效（过期，非token等）"""
        return {
            'code': 80007,
            'status': True,
            'data': None,
            'message': message,
        }

    @staticmethod
    def no_token(message='no token'):
        """没有Token"""
        return {
            'code': 80007,
            'status': False,
            'data': None,
            'message': message,
        }
