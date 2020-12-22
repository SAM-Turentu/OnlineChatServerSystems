# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/22 12:58'
# file : 'Swagger.py'
# Summary : 'swagger 初始化'


# pip install -i https://pypi.douban.com/simple tornado-rest-swagger


# import tornado.web
# from Config import Config
# from UI import URLManagements
# from tornado_swagger.setup import setup_swagger
# from Infrastructure.Core.HttpRequest import BaseRequestHandler
#
#
# class Application(tornado.web.Application):
#     handlers = URLManagements.handlers_urls
#
#     def __init__(self):
#         setup_swagger(
#             self.handlers,
#             swagger_url='/swagger/api/doc',
#             description='描述',
#             api_version='1.0',
#             title='聊天系统 api',
#             contact=dict(name="SAM-Turentu", email="SAM-Turentu@outlook.com", url="http://192.168.1.141:8080"),
#         )
#         super(Application, self).__init__(self.handlers, **Config.settings)
#
#
# class SwaggerHandler(BaseRequestHandler):
#
#     async def get(self):
#         """
#         swagger api 太麻烦，已放弃
#         ---
#         tags:
#             - Home
#         summary: Home
#         description: 首页简单描述
#         operationId: getHomeFromSAM
#         parameters:
#             -
#                 name: userId
#                 in: query
#                 description: 用户Id
#                 required: true
#                 schema:
#                     type: string
#         responses:
#             '200':
#                 description: successful operation
#                 content:
#                     application/json:
#                         schema:
#                             type: object
#                             properties:
#                                 userId:
#                                     type: string
#                                 userName:
#                                     type: string
#
#         """
#         userId = self.get_query_argument('userId')
#         self.write({'userId': userId, 'userName': 'sam'})
