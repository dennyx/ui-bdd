# -*- coding: UTF-8 -*-
'''
Selenium 常用方法封装
'''

from enum import Enum
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *
import logging
from selenium.webdriver.support.select import Select
import logging
from utils.os_gui_util import os_upload_file

class FIND_ELEMENT_METHOD(Enum):
    '''
    查找元素方法枚举
    '''
    ID = 'id'
    XPATH = 'xpath'
    CSS = 'css'
    LINK_TEXT = 'link_text'
    NAME = 'name'
    CLASS_NAME = 'class_name'

def walk_through_menu_to_page(context, main_menu, sub_menu, page_bread_crumb_xpath, page_bread_crumb):
    '''
    根据指定的父级菜单及子级菜单，进入到对应页面，并根据面包屑进行校验
    '''
    browser = context.browser
    main_menu_element = browser.find_element_by_link_text(main_menu)
    main_menu_element.click()
    wait_for_element_show(browser, FIND_ELEMENT_METHOD.LINK_TEXT, sub_menu)
    browser.find_element_by_link_text(sub_menu).click()
    wait_for_element_show(browser, FIND_ELEMENT_METHOD.XPATH, page_bread_crumb_xpath)
    assert_that(browser.find_element_by_xpath(page_bread_crumb_xpath).text, equal_to(page_bread_crumb), 'check page bread crumb')
    wait_ajax_finish(browser)
    # 已经进入页面了，所以开始渲染页面基本元素
    context.current_page.render_base_element()

def walk_through_menu_to_page_always_click(context, main_menu, sub_menu, page_bread_crumb_xpath, page_bread_crumb):
    '''
    根据指定的父级菜单及子级菜单，进入到对应页面，并根据面包屑进行校验
    '''
    browser = context.browser
    main_menu_element = browser.find_element_by_link_text(main_menu)
    temp_parent = main_menu_element.find_element_by_xpath("..")
    if temp_parent.get_attribute('class') and temp_parent.get_attribute('class') == "active":
        main_menu_element.click()
    main_menu_element.click()
    if sub_menu != '' and sub_menu != ' ':
        wait_for_element_show(left_side_bar_nav, FIND_ELEMENT_METHOD.LINK_TEXT, sub_menu)
        context.browser.implicitly_wait(3)
        sub_menu_element = left_side_bar_nav.find_element_by_link_text(sub_menu)
        sub_menu_element.click()
    wait_for_element_show(browser, FIND_ELEMENT_METHOD.XPATH, page_bread_crumb_xpath)
    assert_that(browser.find_element_by_xpath(page_bread_crumb_xpath).text, equal_to(page_bread_crumb), 'check page bread crumb')
    wait_ajax_finish(browser)
    # 已经进入页面了，所以开始渲染页面基本元素
    context.current_page.render_base_element()

def get_table_header_info(table):
    '''
    获取table head内容
    '''
    table_head = table.find_element_by_tag_name('thead').find_elements_by_tag_name("th")
    return [x.text for x in table_head]

def get_table_content_info(table):
    '''
    获取table body内容
    '''
    table_body = get_table_body_row_element(table)
    table_content = []
    for body_cell in table_body:
        cell_content = []
        cell_list = body_cell.find_elements_by_tag_name('td')
        cell_content = [x.text for x in cell_list]
        table_content.append(cell_content)
    return table_content  

def get_table_content_info_as_dic_list(table):
    '''
    获取table body内容为dic形式，便于和数据库数据进行对比
    '''
    table_header = get_table_header_info(table)
    table_body = get_table_body_row_element(table)
    table_content = []
    table_content_len = len(table_header)
    for body_cell in table_body:
        cell_content = {}
        cell_list = body_cell.find_elements_by_tag_name('td')
        for i in range(0, table_content_len):
            cell_content[table_header[i]] = cell_list[i].text
        table_content.append(cell_content)
    logging.info("ui table content as %s" % table_content)
    return table_content

def get_specified_row_link_element(table, row_num, link_text):
    '''
    根据表格的行号，链接内容，去获取对应的元素
    '''
    table_body = get_table_body_row_element(table)
    specified_row = table_body[row_num - 1]
    link_element = specified_row.find_element_by_link_text(link_text)
    return link_element

def get_specified_row_specified_column_value(table, row_num, column_num):
    '''
    根据表格的行号，列号，获取指定元素的值
    '''
    table_body = get_table_body_row_element(table)
    specified_row = table_body[row_num - 1]
    value = specified_row.find_elements_by_tag_name('td')[column_num - 1].text
    logging.info("table specified row_num as %s, column_num as %s, value as %s" % (row_num, column_num, value))
    return value

def get_table_body_row_element(table):
    '''
    获取表格tbody中所有的行
    '''
    return table.find_element_by_tag_name('tbody').find_elements_by_tag_name("tr")

def get_table_column_info_by_name(table, column_name):
    '''
    根据表头名称，获取对应列的值
    '''
    table_head = get_table_header_info(table)
    column_index = table_head.index(column_name)
    table_content = get_table_content_info(table)
    return table_content[column_index]

def wait_for_element_show(browser, key_type, key_content, time_period=10):
    '''
    等待元素出现
    browser 指定当前浏览器实例
    key_type 查找元素方法
    key_content 查找元素内容
    time_period 等待时间
    '''
    if key_type == FIND_ELEMENT_METHOD.ID:
        WebDriverWait(browser, time_period).until(lambda browser: browser.find_element_by_id(key_content).is_displayed())
    elif key_type == FIND_ELEMENT_METHOD.XPATH:
        WebDriverWait(browser, time_period).until(lambda browser: browser.find_element_by_xpath(key_content).is_displayed())
    elif key_type == FIND_ELEMENT_METHOD.LINK_TEXT:
        WebDriverWait(browser, time_period).until(lambda browser: browser.find_element_by_link_text(key_content).is_displayed())
    elif key_type == FIND_ELEMENT_METHOD.NAME:
        WebDriverWait(browser, time_period).until(lambda brower: browser.find_element_by_name(key_content).is_displayed())
    elif key_type == FIND_ELEMENT_METHOD.CLASS_NAME:
        WebDriverWait(browser, time_period).until(lambda brower: browser.find_element_by_class_name(key_content).is_displayed())
    else:
        raise Exception('do not support method %s for find element' % key_type)

def change_select_value(select_element, select_type, select_value):
    '''
    修改下拉框的值, 对应API
    select_by_value(value)
    select_by_index(index)
    select_by_visible_text(text)
    '''
    if select_type == 'value':
        Select(select_element).select_by_value(select_value)
    elif select_type == 'text':
        Select(select_element).select_by_visible_text(select_value)

def wait_ajax_finish(browser):
    '''
    检查页面ajax加载是否完成
    '''
    WebDriverWait(browser, 20).until(lambda browser: browser.execute_script("return jQuery.active == 0"))
    WebDriverWait(browser, 20).until(lambda browser: browser.execute_script("return $('.spinner').is(':visible') == false"))

def wait_ajax_finish_specified(browser, loading_span_class):
    """
    检查页面是否加载完成，根据指定的loading标签
    """
    WebDriverWait(browser, 20).until(lambda browser: browser.execute_script("return $('.%s').is(':visible') == false" % loading_span_class))
    WebDriverWait(browser, 20).until(lambda browser: browser.execute_script("return jQuery.active == 0"))

def wait_specified_element_disappear_by_class(browser, class_name):
    """
    等待指定元素消失
    """
    WebDriverWait(browser, 20).until(lambda browser: browser.execute_script("return $('.%s').is(':visible') == false" % class_name))

def phantom_render_jquery(context):
    '''
    因页面jquery文件原因，使用phantom.js直接加载报错，需要重新加载
    此方案不推荐
    '''
    relied_js_files = ["res/jquery/jquery.js", "res/jquery/jquery.md5.js", "res/jquery/layer-3.1.1.js"]
    execute_local_js_files(context.browser, relied_js_files)

def execute_local_js_files(browser, file_list):
    '''
    执行本地的js文件
    '''
    for file_cell in file_list:
        logging.info("current file_cell as %s" % file_cell)
        execute_local_js_file(browser, file_cell)

def execute_local_js_file(browser, file_name):
    '''
    执行本地的js文件
    '''
    js_content = open(file_name, 'r').read()
    browser.execute_script(js_content)

def get_select_selected_value(select_element):
    '''
    获取select_element选中的值
    '''
    return Select(select_element).first_selected_option.text

def upload_and_crop_img_per_os_gui(browser, upload_btn_ui, crop_btn, upload_img, open_btn_img):
    """
    针对使用angularjs封装的上传、裁剪组件，使用此方法进行上传操作
    """
    upload_btn_ui.click()
    os_upload_file(upload_img, open_btn_img)
    crop_btn.click()
    wait_ajax_finish(browser)
    #等待遮罩层消失
    wait_specified_element_disappear_by_class(browser, "stop-editor-back")