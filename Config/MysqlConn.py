# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/8 16:01'
# file : 'MysqlConn.py'
# Summary : 'Tortoise 异步ORM'


from tortoise import Tortoise
from Config import Config


def MysqlConn():
    ...
    # engine = create_engine(f"mysql+pymysql://{Config.mysql_config.get('user')}:{Config.mysql_config.get('pwd')}@{Config.mysql_config.get('host')}:"
    #                        f"{Config.mysql_config.get('port')}/{Config.mysql_config.get('db')}", max_overflow=5)
    # return engine


# loop = asyncio.get_event_loop()
#
#
# async def AsyncMysqlConn():
#     conn = await aiomysql.connect(host=Config.mysql_config.host, user=Config.mysql_config.user, password=Config.mysql_config.pwd,
#                                   db=Config.mysql_config.db, port=Config.mysql_config.port, loop=loop)
#     cursor = await conn.cursor()
#     return cursor


async def mysql_init():
    try:

        await Tortoise.init(
            db_url=f'mysql://{Config.mysql_config.user}:{Config.mysql_config.pwd}@{Config.mysql_config.host}:{Config.mysql_config.port}/{Config.mysql_config.db}',
            modules={'models': [
                'Model.Account.AccountModel',
                'Model.Admin.AdminModel',
            ]}
        )
        # await Tortoise.generate_schemas(safe=True)  # safe设置为true时，仅在表不存在时才创建。
    except Exception as e:
        print(e)
