#!/usr/bin/env python
# -- coding=utf-8 --
"""
左侧菜单栏集合
"""
class LeftMenuPage():
    def __init__(self, context):
        self.context = context

    def homePageMenu(self):
        self.home_page = self.context.browser.find_element_by_xpath("//span[text()='首页']")
        self.transaction_statistics = self.context.browser.find_element_by_xpath("//a[text()='交易额统计']")

    def businessManagementMenu(self):
        self.business_management = self.context.browser.find_element_by_xpath("//span[text()='商户管理']")
        self.basic_information = self.context.browser.find_element_by_xpath("//a[text()='基本信息']")
        self.store_management = self.context.browser.find_element_by_xpath("//a[text()='门店管理']")

    def commodityManagementMenu(self):
        self.commodity_management = self.context.browser.find_element_by_xpath("//span[text()='商品管理']")
        self.commodity_inquire = self.context.browser.find_element_by_xpath("//a[text()='商品查询']")
        self.commodity_release = self.context.browser.find_element_by_xpath("//a[text()='商品发布']")

    def transactionManagementMenu(self):
        self.transaction_management = self.context.browser.find_element_by_xpath("//span[text()='交易管理']")
        self.group_purchase_delivery = self.context.browser.find_element_by_xpath("//a[text()='团购提货']")
        self.order_inquire = self.context.browser.find_element_by_xpath("//a[text()='订单查询']")
        self.pick_up_code = self.context.browser.find_element_by_xpath("//a[text()='提货码管理']")
        self.check_out_counter = self.context.browser.find_element_by_xpath("//a[text()='收银台']")

    def wordOfMouthManagementMenu(self):
        self.word_of_mouth = self.context.browser.find_element_by_xpath("//span[text()='口碑管理']")
        self.commodity_comment = self.context.browser.find_element_by_xpath("//a[text()='商品评价']")
        self.merchant_comment = self.context.browser.find_element_by_xpath("//a[text()='商户评价']")

    def userManagementMenu(self):
        self.user_management = self.context.browser.find_element_by_xpath("//span[text()='用户管理']")
        self.sub_user_management = self.context.browser.find_element_by_xpath("//a[text()='用户管理']") #子菜单

    def funPayMenu(self):
        self.funPay = self.context.browser.find_element_by_xpath("//span[text()='金农信e付']")
        self.funpayOrderList = self.context.browser.find_element_by_xpath("//a[text()='当前交易查询']")
        self.funpayRefundList = self.context.browser.find_element_by_xpath("//a[text()='当前退款查询']")
        self.funpaySettleList = self.context.browser.find_element_by_xpath("//a[text()='当前日账单查询']")
        self.funpayRefund = self.context.browser.find_element_by_xpath("//a[text()='退款申请']")
        self.latelyFunpayOrderList = self.context.browser.find_element_by_xpath("//a[text()='近期交易查询']")
        self.latelyFunpayRefundList = self.context.browser.find_element_by_xpath("//a[text()='近期退款查询']")
        self.latelySettleList = self.context.browser.find_element_by_xpath("//a[text()='近期日账单查询']")