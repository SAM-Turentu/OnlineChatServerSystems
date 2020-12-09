# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/7 16:34'
# file : 'AccountService.py'
# Summary : ''


from Infrastructure.DI.Meta import DIMetaClassList


class AccountService(metaclass=DIMetaClassList):

    def __init__(self, **kwargs):
        """service 中 kwargs.get('accountRepository') 首字母需小写"""
        self._account = kwargs.get('accountRepository')
        # self._admin = kwargs.get('adminRepository')

    async def get_user_info(self):
        ...

    async def register_user(self, phone, password, user_name):
        """注册用户"""
        try:
            await self._account.add_new_user(phone, password, user_name)
        except Exception as e:
            print(e)
