import re
from django.shortcuts import render
class CheckBrowser(object):
    # Request预处理函数,调用时机在 Django 接收到 request
    # 之后，但仍未解析URL以确定应当运行的 view 之前。Django 向它传入相应的
    # HttpRequest 对象，以便在方法中修改。
	def process_request(self,request):
		# 获取浏览器信息
		agent = (request.META['HTTP_USER_AGENT'])
		print (agent)
		# 用正则来进行筛选,主要匹配MSIE 5~8
		result = re.findall("MSIE [5678]",agent) 
		# print (result)
		if len(result)>0:
			# 如果浏览器是5~8版本，就显示升级页面
			return render(request,"warning.html")