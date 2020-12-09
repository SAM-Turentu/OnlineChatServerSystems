# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/9 10:56'
# file : 'GINOTEST.py'
# Summary : '1.0版本暂不支持 mysql，只支持 postgresql'


import asyncio

from gino import Gino
from Config import Config

db = Gino()


class Account(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(100), nullable=False, index=True, unique=True)
    user_name = db.Column(db.String(50))
    status = db.Column(db.Integer, default=0)


class AccountModel:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.user_name = kwargs.get('user_name')
        self.sex = kwargs.get('sex')


# daisy = await Account.create(user_name='sam')
# await daisy.update(user_name='turentu').apply()

async def main_gino():
    try:
        # db = Gino(bind='mysql+pymysql://root:''@192.168.1.10:3306/customer_service_systems')
        # await db.set_bind(f'mysql+pymysql://{Config.mysql_config.user}:{Config.mysql_config.pwd}@{Config.mysql_config.host}:{Config.mysql_config.port}/{Config.mysql_config.db}')
        await db.set_bind("mysql+pymysql://root:''@192.168.1.10:3306/customer_service_systems")
        await db.gino.create_all()

        # further code gose here
        daisy = await Account.create(user_name='sam')
        await daisy.update(user_name='turentu').apply()

        await db.pop_bind().close()
    except Exception as e:
        # 此方法会抛异常，暂不支持mysql 异步
        print(e)


asyncio.get_event_loop().run_until_complete(main_gino())
