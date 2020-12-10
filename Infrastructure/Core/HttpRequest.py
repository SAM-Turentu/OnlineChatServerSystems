# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 14:40'
# file : 'HttpRequest.py'
# Summary : ''


from typing import Union
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler

from Infrastructure.Utils.Session.SessionFactory import SessionFactory


class BaseRequestHandler(RequestHandler):

    def initialize(self):
        self.session = SessionFactory.get_session_obj(self)  # 异步redis


class WebSocketRequestHandler(WebSocketHandler):

    def initialize(self):
        self.session = SessionFactory.get_session_obj(self)

    def open(self, *args: str, **kwargs: str):
        ...

    def on_message(self, message: Union[str, bytes]):
        ...

    def on_close(self):
        ...

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求
