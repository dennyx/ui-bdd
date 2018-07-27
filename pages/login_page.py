# -*- coding: UTF-8 -*-
'''
登录页面，封装各控件
'''

class LoginPage():

    def __init__(self, context):
        self.context = context
        self.username_input_id = 'userName'

    def set_base_element(self):
        self.usernameInput = self.context.browser.find_element_by_id("userName")
        self.passwordInput = self.context.browser.find_element_by_id("password")
        self.loginBtn = self.context.browser.find_element_by_id("btnLogin")

    def set_login_fail(self):
        pass