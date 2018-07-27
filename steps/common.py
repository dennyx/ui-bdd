# -*- coding: UTF-8 -*-

import time
from behave import given, when, then
from hamcrest import *
from pages.login_page import LoginPage
from pages.BasePage import BasePage
from utils.selenium_util import wait_for_element_show,FIND_ELEMENT_METHOD, walk_through_menu_to_page, wait_ajax_finish, phantom_render_jquery
from config import BASE_CONFIG
import logging
from pages.export import *

def log_in(context):
    loginPage = LoginPage(context)
    wait_for_element_show(context.browser, FIND_ELEMENT_METHOD.ID, loginPage.username_input_id)
    loginPage.set_base_element()
    loginPage.usernameInput.send_keys(BASE_CONFIG["SYSTEM_INFO"]["MERCHANT_ACCOUNT"])
    loginPage.passwordInput.send_keys(BASE_CONFIG["SYSTEM_INFO"]["PASSWORD"])
    loginPage.loginBtn.click()
    wait_ajax_finish(context.browser)
    context.current_page = BasePage(context)
    wait_for_element_show(context.browser, FIND_ELEMENT_METHOD.XPATH, context.current_page.user_info_xpath)

def log_out(context):
    wait_ajax_finish(context.browser)
    context.browser.find_element_by_xpath(context.current_page.logout_xpath).click()

@given('sleep for {time_period:Number} seconds')
def sleep(context, time_period):
    time.sleep(time_period)

@given('driver sleep for {time_period:Number} seconds')
def browser_sleep(context, time_period):
    context.browser.implicitly_wait(time_period)

@given('click menu "{main_menu}" and "{sub_menu}" and bread_crumb as "{bread_crumb}"')
def go_through_menu(context, main_menu, sub_menu, bread_crumb):
    basePage = BasePage(context)
    walk_through_menu_to_page(context, main_menu, sub_menu, basePage.page_breadcrumb_xpath, bread_crumb)

@when('I wait for page loading')
def wait_for_page_loading(context):
    wait_ajax_finish(context.browser)

@then('total info should be "{total_num}" with param "{param_name}"')
def check_total_data_number(context, total_num, param_name):
    if not context.current_page.is_rendered_base_element:
        context.current_page.render_base_element()
    context.current_page.render_page_element()
    if param_name != '' and param_name != ' ' and context.data.has_key(param_name):
        total_num = total_num.replace(param_name, str(context.data[param_name]))
    assert_that(context.current_page.total_number_div.text.split(",")[0], equal_to(total_num), "check total number info")

@given('I switch to page "{page_name}"')
def change_page(context, page_name):
    change_to_specified_page(context, page_name)
    context.current_page.render_base_element()
    
def change_to_specified_page(context, page_name):
    '''
    根据页面对象名称，来切换当前活跃的页面实例
    '''
    logging.info("Preparing to switch current page instance to %s" % page_name)
    clazz = globals()[page_name]
    context.current_page = clazz(context)
    logging.info("Successfully switched current page instance to %s" % page_name)