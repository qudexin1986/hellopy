'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class CategoryrecommendItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.category_id = None
		self.count = None
		self.ext = None
		self.recommend_type = None

	def getapiname(self):
		return 'taobao.categoryrecommend.items.get'
