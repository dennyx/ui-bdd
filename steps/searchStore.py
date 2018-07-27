#!/usr/bin/env python
# -- coding=utf-8 --
"""
商户管理-->门店管理，门店信息查询
"""
from behave import given, then, when
from hamcrest import assert_that,equal_to
import logging
from pages.leftMenu_page import LeftMenuPage
from pages.StoreManagement.StoreManagementPage import StoreManagementPage
from utils.selenium_util import wait_for_element_show, FIND_ELEMENT_METHOD, wait_ajax_finish, get_table_header_info, get_table_content_info_as_dic_list

@when('Enter store_name as "{store_name}", address as "{address}", store_status as passed and click search button')
def enter_search_message(context, store_name, address):
    context.current_page.store_name.send_keys(store_name) #输入门店名称
    context.current_page.address.send_keys(address) #输入门店地址
    context.current_page.search_button.click() #点击查询按钮
    wait_ajax_finish(context.browser)

@then('data table header should be "{header_str_list:List}"')
def check_store_table_header(context, header_str_list):
    table_header = get_table_header_info(context.current_page.store_table)
    assert_that(table_header, equal_to(header_str_list), 'check for table header')

@then('I should see the specified record')
def check_store_information_in_ui_table(context):
    table_first_row = get_table_content_info_as_dic_list(context.current_page.store_table)
    logging.info("table content as %s" % table_first_row)

@then('All the information same with DB by sql')
def check_store_information_in_db(context):
    sql_str = context.text
    pass