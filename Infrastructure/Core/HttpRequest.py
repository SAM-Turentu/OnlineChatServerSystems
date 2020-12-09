# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 14:40'
# file : 'HttpRequest.py'
# Summary : ''


from typing import Union
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler


class BaseRequestHandler(RequestHandler):

    def initialize(self):
        ...


class WebSocketRequestHandler(WebSocketHandler):

    def initialize(self):
        ...

    def open(self, *args: str, **kwargs: str):
        ...

    def on_message(self, message: Union[str, bytes]):
        ...

    def on_close(self):
        ...

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求
