'''
Created by auto_sdk on 2014-02-12 16:59:11
'''
from top.api.base import RestApi
class AlipayMicropayOrderConfirmpayurlGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.alipay_order_no = None
		self.amount = None
		self.auth_token = None
		self.memo = None
		self.receive_user_id = None
		self.transfer_out_order_no = None

	def getapiname(self):
		return 'alipay.micropay.order.confirmpayurl.get'
