# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/4 15:24'
# file : 'OnlineChatController.py'
# Summary : ''


from Infrastructure.Core.HttpRequest import WebSocketRequestHandler


class ChatController(WebSocketRequestHandler):

    def open(self, *args: str, **kwargs: str):
        ...

    def on_message(self, message: Union[str, bytes]):
        ...

    def on_close(self):
        ...
