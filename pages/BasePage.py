# -*- coding: UTF-8 -*-
'''
基本页面对象，所有的页面都应该继承这个
welcome info
logout
left_side_bar
'''

class BasePage():

    def __init__(self, context):
        self.context = context
        self.page_breadcrumb_xpath = "//ul[@class='page-breadcrumb breadcrumb']/li[2]"
        self.user_info_xpath = "//span[@id='welcome_username']"
        self.logout_xpath = "//a[@id='logout']"

    def render_base_element(self):
        '''
        渲染基本元素
        '''
        pass