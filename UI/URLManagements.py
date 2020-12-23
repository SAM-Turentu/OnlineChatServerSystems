# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 13:47'
# file : 'URLManagements.py'
# Summary : ''


from UI.Controllers.AccountController import *
from UI.Controllers.HomeController import *

handlers_urls = [
    # (r'/(\w+)', HomeHandler),  #
    (r'/', HomeHandler),  #
    (r'/register', RegisterHandler),  # 客服系统的注册
    (r'/login', LoginHandler),  # 客服系统的登录
]
