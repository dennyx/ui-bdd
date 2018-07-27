#!/usr/bin/env python
# -- coding=utf-8 --

'''
银行端相关支持
'''

import sys
import os
import time
from behave import given, then, when
from hamcrest import *
import logging
from selenium import webdriver
from utils.selenium_util import wait_for_element_show, FIND_ELEMENT_METHOD, wait_ajax_finish_specified
from config import BASE_CONFIG
from pages.BankApprovalPages import BankLoginPage, BankGroupSaleApprovalPage, BankGroupSaleApprovalDetailPage

@given('I do preapprove for sale in bank')
def preapprove_for_sale_good_in_bank(context):
    """
    银行端审核团购商品 - 初审
    """
    # 初始化
    init_bank(context)
    # 登录
    login_bank(context)
    # 进入 待审核团购 页面
    walk_through_menu_to_tab(context.browser_spy, "任务中心", "待审核团购", context.current_spy_page.target_tab_xpath, "待审核团购", context.current_spy_page.iframe_name)
    # 查询
    search_sale_good(context)
    # 查看详情
    # 点击审核
    # 输入审核意见
    # 同意
    logout(context)

@given('I do final approve for sale in bank')
def final_approve_for_sale_good_in_bank(context):
    """
    银行端审核团购商品 - 复核
    """
    # 登录
    # 进入 待审核团购 页面
    # 查询
    # 查看详情
    # 点击审核
    # 输入审核意见
    # 同意

def search_sale_good(context):
    """
    查询待审核团购商品
    """
    context.current_spy_page.render_base_element()
    context.current_spy_page.merchant_name_input.send_keys("商户名称")
    context.current_spy_page.good_name_input.send_keys("商品名称")
    context.current_spy_page.search_button.click()

def init_bank(context):
    context.browser_spy.get(BASE_CONFIG["DEPENDENCY_SYSTEM"]["BANK"]["URL"])
    context.browser_spy.maximize_window()

def login_bank(context, role="FAREN"):
    """
    登录银行端，并进入指定页面
    role - WANGDIAN, FAREN, SHENG
    """
    loginPage = BankLoginPage(context.browser_spy)
    wait_for_element_show(context.browser_spy, FIND_ELEMENT_METHOD.ID, loginPage.username_input_id)
    loginPage.render_base_element()
    loginPage.usernameInput.send_keys(BASE_CONFIG["DEPENDENCY_SYSTEM"]["BANK"]["%s_ACCOUNT" % role])
    loginPage.passwordInput.send_keys(BASE_CONFIG["DEPENDENCY_SYSTEM"]["BANK"]["PASSWORD"])
    wait_ajax_finish_specified(context.browser_spy, "xubox_layer")
    loginPage.loginBtn.click()
    wait_ajax_finish_specified(context.browser_spy, "xubox_layer")
    context.current_spy_page = BankGroupSaleApprovalPage(context.browser_spy)
    wait_for_element_show(context.browser_spy, FIND_ELEMENT_METHOD.XPATH, context.current_spy_page.login_username_xpath)

def logout(context):
    """
    登出银行端
    """
    context.browser_spy.switch_to.default_content()
    context.browser_spy.find_element_by_xpath(context.current_spy_page.logout_xpath).click()

def walk_through_menu_to_tab(browser, main_menu, sub_menu, tab_xpath, tab_name, iframe_name):
    """
    针对打开多个标签页面系统的行为
    """
    if not browser.find_element_by_link_text(sub_menu):
        main_menu_element = browser.find_element_by_link_text(main_menu)
        main_menu_element.click()
        wait_for_element_show(browser, FIND_ELEMENT_METHOD.LINK_TEXT, sub_menu)
    browser.find_element_by_link_text(sub_menu).click()
    wait_ajax_finish_specified(browser, "xubox_layer")
    time.sleep(5)
    wait_for_element_show(browser, FIND_ELEMENT_METHOD.XPATH, tab_xpath)
    assert_that(browser.find_element_by_xpath(tab_xpath).text, equal_to(tab_name), 'check tab name text')
    wait_ajax_finish_specified(browser, "xubox_layer")
    # tab页面架构，存在iframe，需要进行切换
    browser.switch_to_frame(iframe_name)
