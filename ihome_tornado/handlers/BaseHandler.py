# coding:utf-8

import json

from tornado.web import RequestHandler,StaticFileHandler
from utils.session import Session


class BaseHandler(RequestHandler):
    """自定义基类"""
    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.redis

    def prepare(self):
        print("preparse")
        if self.request.headers.get('Content-Type','').startswith('application/json'):
            print(self.request)
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    def set_default_headers(self):
        """设置默认的json格式"""
        self.set_header('Content-Type','application/json;charset=UTF-8')

    def get_current_user(self):
        """判断是否登录"""
        self.session = Session(self)
        return self.session.data

class StaticFileBaseHandler(StaticFileHandler):
    """docstring for StaticFileBaseHandler"""
    def __init__(self, *args,**kwarges):
        super(StaticFileBaseHandler, self).__init__(*args,**kwarges)
        self.xsrf_token
        
