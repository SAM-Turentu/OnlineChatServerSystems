# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 17:00'
# file : 'AdminModel.py'
# Summary : ''

from tortoise import fields
from tortoise.models import Model


class Admin(Model):
    id = fields.IntField(pk=True, autoincrement=True)
    user_id = fields.CharField(100, null=True, index=True, unique=True)
    level_id = fields.IntField(default=0, index=True)  # 1:super-admin，2：company-super-admin，3:company-admin,4:section-admin,5:employee
    level = fields.CharField(255, index=True)
    customer_service = fields.CharField(255, index=True)  # 客服

    class Meta:
        table = 'admins'


class AdminModel:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
