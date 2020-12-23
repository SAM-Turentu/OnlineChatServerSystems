# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 15:42'
# file : 'IAccountRepository.py'
# Summary : ''


class IAccountRepository:

    async def get_user_by_userId(self, user_id):
        ...

    async def get_user_by_phone(self, phone):
        ...

    async def add_new_user(self, user_id, phone, area_code):
        ...
