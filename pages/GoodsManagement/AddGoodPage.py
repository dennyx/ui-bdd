#!/usr/bin/env python
# -- coding=utf-8 --
"""
商户管理-->门店管理页面--> 新增门店页面
"""

from pages.BasePage import BasePage

class AddGoodPage(BasePage):

    def render_base_element(self):
        self.upload_img_btn = self.context.browser.find_element_by_xpath("//input[@id='uploader2']")
        self.crop_img_btn_xpath = "//div[@class='foot-confirm']/button"
        self.submit_check_box = self.context.browser.find_element_by_xpath("//input[@id='isSubmit']")
        self.save_good_btn = self.context.browser.find_element_by_xpath("//button[@id='saveProductId']")
