# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 15:42'
# file : 'IAccountRepository.py'
# Summary : ''


class IAccountRepository:

    async def get_user(self, user_id):
        ...

    async def add_new_user(self, phone, password, user_name):
        ...
