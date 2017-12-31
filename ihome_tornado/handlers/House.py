#coding:utf-8

import logging
import json
import constants
import math

from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.commons import required_login


# class AreaInfoHandler(BaseHandler):
# 	"""提供城区的信息"""
# 	def get(self):
# 		try:
# 			# 从redis中查找area_info
# 			ret = self.redis.get('area_info')
# 		except Exception as e:
# 			# 将错误信息存入日志中
# 			logging.error(e)
# 			ret = None
# 		if ret:
# 			logging.info("hit redis: area_info")
# 			# 拼出返回的信息
# 			resp = '{"ercode":"0","errmsg":"OK","data":%s}'% ret
# 			return self.write(resp)

# 		sql = "select ai_area_id,ai_name from ih_area_info;"
# 		try:
# 			ret = self.db.query(sql)
# 		except Exception as e