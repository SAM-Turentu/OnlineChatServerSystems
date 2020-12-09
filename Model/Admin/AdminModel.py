# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 17:00'
# file : 'AdminModel.py'
# Summary : ''

from tortoise import fields
from tortoise.models import Model


class Admin(Model):
    id = fields.IntField(pk=True, autoincrement=True)

    class Meta:
        table = 'admin'


class AdminModel:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
