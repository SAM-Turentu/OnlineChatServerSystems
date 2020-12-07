# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/7 16:32'
# file : 'Mapper.py'
# Summary : ''


from Infrastructure.DI.Meta import DIMapper, DIMapperList


def Mapper():
    """一个 service 只能绑定一个 repository"""
    DIMapper.inject('cls', 'arg')


def MapperList():
    """
    默认使用该方法，一个 service 可绑定多个 repository
    Notice: service 中 kwargs.get('accountRepository') 获取需小写
    :return:
    """
    DIMapperList.inject('cls', 'args1', 'args2')
