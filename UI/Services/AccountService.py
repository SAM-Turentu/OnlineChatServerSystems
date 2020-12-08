# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/7 16:34'
# file : 'AccountService.py'
# Summary : ''


from Infrastructure.DI.Meta import DIMetaClassList


class AccountService(metaclass=DIMetaClassList):

    def __init__(self, **kwargs):
        """service 中 kwargs.get('accountRepository') 首字母需小写"""
        self.accountRepository = kwargs.get('accountRepository')
        self.adminRepository = kwargs.get('adminRepository')

    def get_user_info(self):
        ...

    def add_new_user(self):
        ...
