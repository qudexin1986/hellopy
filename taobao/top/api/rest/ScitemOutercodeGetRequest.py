'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class ScitemOutercodeGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.outer_code = None

	def getapiname(self):
		return 'taobao.scitem.outercode.get'
