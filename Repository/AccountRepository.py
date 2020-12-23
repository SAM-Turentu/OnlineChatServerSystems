# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 15:41'
# file : 'AccountRepository.py'
# Summary : ''


from IRepository.IAccountRepository import IAccountRepository
from Model.Account.AccountModel import Account


class AccountRepository(IAccountRepository):

    async def get_user_by_userId(self, user_id):
        return await Account.get(user_id=user_id)

    async def get_user_by_phone(self, phone):
        return await Account.get(phone=phone)

    async def add_new_user(self, user_id, phone, area_code):
        """注册用户"""
        await Account.create(user_id=user_id, phone=phone, area_code=area_code, status=1)
