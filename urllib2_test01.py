#!/usr/bin/env python
#coding:utf-8

import urllib2
import urllib

# response = urllib2.urlopen('http://www.baidu.com');
# html = response.read();
# print html;

# req = urllib2.Request('http://www.baidu.com');
# response = urllib2.urlopen(req);
# the_page = response.read();
# print the_page

url = 'http://www.someserver.com/register.cgi';

values = {
	name:"lhy",
	location:"SDU",
	language:"Python"
};
data = urllib.urlencode(values); #编码工作

req = urllib2.Request(url,data); #发送请求同时传data表单

response = urllib2.urlopen(req); #接受反馈信息

the_page = response.read();  #读取反馈内容

