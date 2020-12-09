# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 15:41'
# file : 'AccountRepository.py'
# Summary : ''


from IRepository.IAccountRepository import IAccountRepository
from Model.Account.AccountModel import Account


class AccountRepository(IAccountRepository):

    async def get_user(self, user_id):
        ...

    async def add_new_user(self, phone, password, user_name):
        """注册用户"""
        try:
            await Account.create(user_id=phone, user_name=user_name, status=1)
        except Exception as e:
            print(e)
