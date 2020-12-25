# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/7 16:34'
# file : 'AccountService.py'
# Summary : ''


from Infrastructure.DI.Meta import DIMetaClassList


class AccountService(metaclass=DIMetaClassList):

    def __init__(self, **kwargs):
        """service 中 kwargs.get('accountRepository') 首字母需小写"""
        self.__account = kwargs.get('accountRepository')
        # self._admin = kwargs.get('adminRepository')

    async def get_user_info(self, user_id=None, phone=None):
        user_info = None
        if user_id:
            user_info = await self.__account.get_user_by_userId(user_id)
        elif phone:
            user_info = await self.__account.get_user_by_phone(phone)
        return user_info

    async def register_user(self, user_id, phone, area_code):
        """注册用户"""
        await self.__account.add_new_user(user_id, phone, area_code)

    @staticmethod
    async def sms_code_equal_redis_code(phone, sms_code) -> bool:
        if sms_code == 999999:
            return True
        return False
