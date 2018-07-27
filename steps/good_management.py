#!/usr/bin/env python
# -- coding=utf-8 --
import sys
sys.path.append('../')
import os
import time
from behave import given, then, when
from hamcrest import *
import logging
from utils.selenium_util import change_select_value, wait_for_element_show,FIND_ELEMENT_METHOD,upload_and_crop_img_per_os_gui,wait_ajax_finish
from utils.datepicker_util import specify_datepicker_as_today

@when('I specify below valid good info to add good')
def enter_add_store_page(context):
    context.browser.execute_script("$('#startTime').removeAttr('readonly')")
    context.browser.execute_script("$('#endTime').removeAttr('readonly')")
    context.browser.execute_script("$('#expireEndTime').removeAttr('readonly')")
    for row in context.table:
        temp_element = context.browser.find_element_by_xpath(row["element_xpath"])
        if row["element_type"] == "select":
            change_select_value(temp_element, "text", row["value"])
        elif row["element_type"] == "date_picker":
            # remove attr
            temp_element.send_keys(row["value"])
        else:
            temp_element.send_keys(row["value"])

@when('upload good photoes, file name as "{file_list:List}"')
def upload_good_photoes(context, file_list):
    upload_file = ""
    for file_cell in file_list:
        file_str = '/image/' + file_cell
        upload_file += file_str + ","
    upload_file = upload_file.rstrip(",")
    open_img_path = os.path.join(os.path.join(os.getcwd(), 'image'), 'docker_open_chrome.png')

    upload_and_crop_img_per_os_gui(context.browser, context.current_page.upload_img_btn, context.browser.find_element_by_xpath(context.current_page.crop_img_btn_xpath), upload_file, open_img_path)

@when('check submit for approval')
def check_submit_for_approval(context):
    wait_ajax_finish(context.browser)
    context.current_page.submit_check_box.click()

@when('click to save good')
def click_to_save_good(context):
    wait_ajax_finish(context.browser)
    context.current_page.save_good_btn.click()

@then('should get good in good list')
def check_good_in_good_list(context):
    wait_ajax_finish(context.browser)
    pass
