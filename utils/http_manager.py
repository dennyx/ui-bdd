#!/usr/bin/env python
# -- coding=utf-8 --

'''
http请求工具类
'''

import requests
from config import BASE_CONFIG

def make_get_request(sub_url):
    '''
    Get请求
    '''
    url = BASE_CONFIG['BASE_URL'] + sub_url
    print "Preparing to make get request, url as %s" % url
    result = requests.get(url=url)
    format_result = result.content.decode('UTF-8')
    return format_result

def make_post_request(sub_url, data=''):
    '''
    Post请求
    '''
    pass

# Test Code
# print make_get_request('http://www.weather.com.cn/data/sk/101190408.html')