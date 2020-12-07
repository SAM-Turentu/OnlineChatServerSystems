# -*- coding:utf-8 -*-
# Author : 'SAM'
# CreateTime : '2020/12/3 10:32'
# file : 'Main.py'
# Summary : '在线聊天系统'


import logging
import tornado
import tornado.web
import tornado.ioloop
import tornado.options
from tornado import httpserver
from tornado.options import define, options, parse_command_line
from colorama import init

from Config import Config
from UI import URLManagements

define('port', default=8080, type=int)
# logging.basicConfig(level=logging.INFO)
# options.log_rotate_mode = 'time'  # 轮询模式: time or size
# options.log_rotate_when = 'D'  # 单位: S / M / H / D / W0 - W6
# options.log_rotate_interval = 1  # 间隔: 1天
#
# options.log_file_prefix = os.path.join(os.path.dirname(__file__), 'logs/tornado_main')


def main():
    try:
        init(autoreset=True)  # windows 控制台颜色输出
        parse_command_line()
        logging.info(f'服务已启动，地址：127.0.0.1:{options.port}')
        app = tornado.web.Application(
            handlers=URLManagements.handlers_urls,
            **Config.settings
        )
        http_server = httpserver.HTTPServer(app, xheaders=True)  #
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()

