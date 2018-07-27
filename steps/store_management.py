#!/usr/bin/env python
# -- coding=utf-8 --
import sys
sys.path.append('../')
import os
import time
from behave import given, then, when
from hamcrest import *
import logging
from utils.selenium_util import wait_for_element_show, FIND_ELEMENT_METHOD, wait_ajax_finish,upload_and_crop_img_per_os_gui

@given('click add store button')
def enter_add_store_page(context):
    # 点击新增按钮，进入新增门店页面
    context.current_page.add_button.click() #点击门店管理页面中的新增按钮
    wait_ajax_finish(context.browser)

@when('fill in the following store information as "{store_message}"')
def enter_store_message(context, store_message):
    store_message_list = store_message.split('|') #将用例数据转换成数组

    i = 0
    for input_box in context.current_page.input_list: #循环将用户数据填充到页面输入框中
        if i < len(store_message_list):
            input_box.send_keys(store_message_list[i])
            i = i + 1
        else:
            break

@when('select the area message as "{area_message}"')
def select_area_message(context, area_message):

    area_message_list = area_message.split('|') #将用例数据转换成数组

    context.current_page.select_province.find_element_by_xpath("//option[text()='%s']" % area_message_list[0]).click()
    wait_ajax_finish(context.browser)

    context.current_page.select_city.find_element_by_xpath("//option[text()='%s']" % area_message_list[1]).click()
    wait_ajax_finish(context.browser)

    context.current_page.select_area.find_element_by_xpath("//option[text()='%s']" % area_message_list[2]).click()
    wait_ajax_finish(context.browser)

    context.current_page.location_button.click() #点击地区定位
    wait_ajax_finish(context.browser)

@when('select the category message as "{category_message}"')
def select_category_message(context, category_message):
    # 选择所属分类
    context.current_page.category_button.click() #点击打开所属分类详情页面
    wait_ajax_finish(context.browser)

    category_message_list = category_message.split('|') #将用例数据转换成数组

    category_count = 1
    for category in category_message_list:
        if category_count <= len(category_message_list):
            context.browser.find_element_by_xpath("//div/a[text()='%s']" % category).click()
            category_count = category_count + 1
        else:
            break
    context.current_page.category_confirm_button.click()

@when('enter the store description as "{store_description}"')
def enter_store_description(context, store_description):
    store_description_list = store_description.split('|') #将用例数据转换成数组

    i = 0
    for description_box in context.current_page.textarea_list: #循环将用户数据填充到页面输入框中
        if i < len(store_description_list):
            description_box.send_keys(store_description_list[i])
            i = i + 1
        else:
            break

@when('enter the discount message as "{discount_message}"')
def enter_discount_message(context, discount_message):
    #优惠详情
    discount_message_list = discount_message.split('|')
    context.current_page.discount_information.send_keys(discount_message_list[0])

    if discount_message_list[1] == 'N':
        context.current_page.discount_check_box.click()
    else:
        pass

@when('upload store logo, file name as "{file_name}"')
def upload_store_logo(context, file_name):
    # upload_file = os.path.join(os.path.join(os.getcwd(), 'image'), file_name)
    upload_file = '/image/' + file_name
    open_img_path = os.path.join(os.path.join(os.getcwd(), 'image'), 'docker_open_chrome.png')

    upload_and_crop_img_per_os_gui(context.browser, context.current_page.logo_upload_button, context.browser.find_element_by_xpath(context.current_page.save_logo_btn_xpath), upload_file, open_img_path)

@when('upload store photoes, file list as "{file_list:List}"')
def upload_store_photoes(context, file_list):
    wait_for_element_show(context.browser, FIND_ELEMENT_METHOD.XPATH, context.current_page.image_upload_button_xpath)
    upload_file = ""
    for file_cell in file_list:
        # file_str = os.path.join(os.path.join(os.getcwd(), 'image'), file_cell)
        file_str = '/image/' + file_cell
        upload_file += file_str + ","
    upload_file = upload_file.rstrip(",")
    open_img_path = os.path.join(os.path.join(os.getcwd(), 'image'), 'docker_open_chrome.png')

    upload_and_crop_img_per_os_gui(context.browser, context.current_page.image_upload_button, context.browser.find_element_by_xpath(context.current_page.save_img_btn_xpath), upload_file, open_img_path)

@when('save outlet')
def save_store(context):
    wait_for_element_show(context.browser, FIND_ELEMENT_METHOD.XPATH, context.current_page.save_outlet_button_xpath)
    context.current_page.save_outlet_button.click()

@then('should get store in management page name as "{store_name}"')
def check_store_in_management_page(context, store_name):
    pass