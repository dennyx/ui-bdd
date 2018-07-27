#!/usr/bin/env python
# -- coding=utf-8 --

from behave import given, then, when
from hamcrest import *
import logging
from pages.leftMenu_page import LeftMenuPage
from pages.StoreManagement.BasicInformationPage import BasicInformationPage
from utils.selenium_util import wait_for_element_show, FIND_ELEMENT_METHOD, wait_ajax_finish

@then('check merchant basic information')
def check_information(context):
    """
    校验商户管理-->基本信息的页面数据是否正确
    """
    context.left_page = LeftMenuPage(context)
    context.left_page.businessManagementMenu()
    context.left_page.business_management.click()

    context.current_page = BasicInformationPage(context)
    wait_for_element_show(context.browser, FIND_ELEMENT_METHOD.XPATH, context.current_page.basic_information_xpath)

    context.left_page.basic_information.click()

    wait_ajax_finish(context.browser)