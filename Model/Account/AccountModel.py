# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 14:32'
# file : 'AccountModel.py'
# Summary : ''


from tortoise import fields
from tortoise.models import Model


class Account(Model):
    id = fields.IntField(pk=True, autoincrement=True)
    user_id = fields.CharField(100, null=True, index=True, unique=True)
    phone = fields.CharField(50, null=True, index=True, unique=True)
    area_code = fields.CharField(10)  # 电话区号 中国大陆（86）默认
    user_name = fields.CharField(50)
    status = fields.IntField(default=0)

    class Meta:
        table = 'users'

    def __str__(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'phone': self.phone,
            'user_name': self.user_name,
            'status': self.status,
        }


class AccountModel:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.user_name = kwargs.get('user_name')
        self.sex = kwargs.get('sex')


async def user_save():
    await Account.create(user_id='id_123458', user_name='sam-turentu', status=1)
