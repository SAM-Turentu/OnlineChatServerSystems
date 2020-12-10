# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/10 10:13'
# file : 'SessionFactory.py'
# Summary : ''


from Config import Config
from Infrastructure.Utils.Session.RedisSession import RedisSession


class SessionFactory:

    @staticmethod
    def get_session_obj(handler):
        try:
            obj = None
            if Config.SESSION_TYPE == 'cache':
                ...
            elif Config.SESSION_TYPE == 'redis':
                obj = RedisSession(handler)  # 异步session
            else:
                ...
            return obj
        except Exception as e:
            print(e)
