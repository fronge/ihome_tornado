# coding:utf-8

import os
import torndb
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import config
import redis
import torndb

from handlers import Passport
from urls import urls
from tornado.options import options,define
from tornado.web import RequestHandler


define('port',default=8888,type=int,help='run server on the given port')


class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        self.db = torndb.Connection(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)
def main():
    options.log_file_prefix = config.log_path
    options.logging = config.log_level
    tornado.options.parse_command_line()
    app = Application(
        urls,
        **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
