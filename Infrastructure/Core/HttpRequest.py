# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 14:40'
# file : 'HttpRequest.py'
# Summary : ''


import logging
import time
import traceback
from typing import Union
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from Infrastructure.Utils.CommonImpl import catch_exception
from Infrastructure.Utils.Session.SessionFactory import SessionFactory


class BaseRequestHandler(RequestHandler):

    # def data_received(self, chunk):
    #     pass

    def initialize(self):
        self.session = SessionFactory.get_session_obj(self)  # 异步redis

    def prepare(self):
        ...
        # # 中间件默认设置中的2个
        # if 'main/exhibitor/bg/' in self.request.path:  # 参展商登录中间件
        #     middleware = self.middleware_list[2]  # ExhibitorLoginMiddleWare
        # elif 'main/designBiennale2020/admin' in self.request.path:  # 管理员
        #     middleware = self.middleware_list[0]  # AdminLoginMiddleWare
        # else:
        #     configService = ConfigService()
        #     configService.add_page_view_to_redis(HistoryPageViewRedisModel(handler=self, session=self.session, viewSource=3))
        #     middleware = self.middleware_list[1]  # CheckLoginMiddleWare
        # mpath, mclass = middleware.rsplit('.', maxsplit=1)
        # mod = importlib.import_module(mpath)
        # self.account = getattr(mod, mclass).process_request(self, self)

    def on_finish(self):
        ...
        # # 中间件默认设置中的2个
        # if 'main/exhibitor/bg/' in self.request.path:  # 参展商登录中间件
        #     middleware = self.middleware_list[2]  # ExhibitorLoginMiddleWare
        # elif 'main/designBiennale2020/admin  ' in self.request.path:
        #     middleware = self.middleware_list[0]  # AdminLoginMiddleWare
        # else:
        #     middleware = self.middleware_list[1]  # CheckLoginMiddleWare
        # mpath, mclass = middleware.rsplit('.', maxsplit=1)
        # mod = importlib.import_module(mpath)
        # getattr(mod, mclass).process_response(self, self)

    def finish(self, chunk=None):
        print(self)
        catch_exception(self)
        super().finish(chunk)

    def write_error(self, status_code, **kwargs):
        # 此处调用日志收集方法
        catch_exception(self)
        exc_cls, exc_instance, trace = kwargs.get("exc_info")
        error = traceback.format_exc()
        t = time.time()
        # print(f'{t}\n\n\t\t {error}')
        logging.error(error)
        ...
        # if status_code != 200:
        #     self.set_status(status_code)
        #     self.write({"msg": str(exc_instance)})

    # def write_error(self, status_code, **kwargs):
    #     """若发生错误，则发送错误信息给 client"""
    #     return_data = ReturnResponse()
    #     exc_cls, exc_instance, trace = kwargs.get('exc_info')
    #     if status_code != 200:
    #         self.set_status(200)
    #         if 're-login' in str(exc_instance):
    #             return_data.ret_token_invalid()
    #         else:
    #             return_data.ret_exception(message=str(exc_instance))
    #         if 'main/exhibitor/bg/' in self.request.path or 'main/designBiennale2020/admin' in self.request.path:
    #             self.write(return_data.__dict__)
    #         elif '.html' in self.request.path:
    #             self.redirect('/main/login')
    #         else:
    #             return_data.ret_no_login()
    #             self.write(return_data.__dict__)


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
