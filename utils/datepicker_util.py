# -*- coding: UTF-8 -*-
'''
操作日期控件，常用方法封装
'''

from utils.selenium_util import FIND_ELEMENT_METHOD, wait_for_element_show

def specify_datepicker_by_remove_attr(browser, input_name, year, month, day):
    '''
    wdatepicker控件
    删除readonly属性，直接赋值
    '''
    browser.execute_script("$('input[name=%s]').removeAttr('readonly')" % input_name)
    browser.find_element_by_name(input_name).send_keys('%s-%s-%s' % (day, month, year))

def specify_datepicker_by_run_script(browser, year, month, day):
    '''
    wdatepicker控件
    直接调用wdatepicker的js
    '''
    browser.switch_to.default_content()
    datepicker_iframe = browser.find_element_by_xpath("//iframe[contains(@src,'about:blank')]")
    browser.switch_to.frame(datepicker_iframe)
    wait_for_element_show(browser, FIND_ELEMENT_METHOD.XPATH, "//div[@class='WdateDiv']")
    browser.execute_script('day_Click(' + '%s,%s,%s' % (year, month, day) + ')')

def specify_datepicker_as_today(browser):
    '''
    wdatepicker控件
    选择日期为当天
    '''
    browser.switch_to.default_content()
    datepicker_iframe = browser.find_element_by_xpath("//iframe[contains(@src,'about:blank')]")
    browser.switch_to.frame(datepicker_iframe)
    wait_for_element_show(browser, FIND_ELEMENT_METHOD.XPATH, "//div[@class='WdateDiv']")
    browser.find_element_by_id('dpOkInput').click()

def specify_datepicker_by_go_through(browser, year, month, day):
    '''
    wdatepicker控件
    通过遍历元素来选值
    '''
    browser.switch_to.default_content()
    datepicker_iframe = browser.find_element_by_xpath("//iframe[contains(@src,'about:blank')]")
    browser.switch_to.frame(datepicker_iframe)
    wait_for_element_show(browser, FIND_ELEMENT_METHOD.XPATH, "//div[@class='WdateDiv']")
    browser.find_element_by_xpath("//td[@onclick='day_Click(%s,%s,%s);']" % (year, month, day)).click()