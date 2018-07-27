# -*- coding: UTF-8 -*-
"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)

++++++++++++++++++++++++++++++++++++++++++++++++++++
run operation
before_all
for feature in all_features:
    before_feature
    for scenario in feature.scenarios:
        before_scenario
        for step in scenario.steps:
            before_step
                step.run()
            after_step
        after_scenario
    after_feature
after_all

"""

import logging

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from utils.database.db_tool import DB_TOOL
from utils.random_util import gen_current_timestamp_str
from utils.selenium_util import phantom_render_jquery
from steps.common import log_in, change_to_specified_page, log_out

from config import BASE_CONFIG
from utils.common import clean_folders, append_temp_path_to_path

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=BASE_CONFIG['LOG']['LOG_FILE_NAME'],
                    filemode='w')

def before_all(context):
    try:
        # 清除数据
        clean_temp_folder()
        # 修改系统环境变量，增加驱动目录
        append_temp_path_to_path(BASE_CONFIG["CHROME"]["DRIVER_PATH"])
        # 初始化数据库连接，并检查环境
        context.db_mysql = DB_TOOL(BASE_CONFIG["DB"]["DB_CONN_STR"])
        context.db_mysql.check_database()
        # 初始化浏览器
        initialize_browser(context)
        context.browser.get(BASE_CONFIG["SYSTEM_INFO"]["URL"])
        if BASE_CONFIG["RUN"]["RUN_BROWSER"] == 'phantomjs':
            phantom_render_jquery(context)
        context.browser.maximize_window()
        # 初始化数据
        context.data = {}
    except Exception as e:
        logging.exception("Failed to start test")
        clean_env(context)

def after_all(context):
    clean_env(context)

def clean_env(context):
    """
    执行结束后，清理环境信息
    """
    context.db_mysql.close_db()
    context.browser.quit()
    context.browser_spy.quit()

def before_feature(context, feature):
    '''
    feature名字，需要和页面对象的名称一致，用于初始化页面对象
    通过名称，反射调用对应的class
    '''
    change_to_specified_page(context, feature.name)

def before_tag(context, tag):
    '''
    针对所有需要登录的操作
    '''
    if tag == 'NEED_LOGIN':
        try:
            log_in(context)
        except Exception as e:
            context.browser.get_screenshot_as_file('login_fail.png')
            logging.exception("Error occured as %s" % e)
            # logging.exception("browser log as \n %s" %
            #                   context.browser.get_log('browser'))
            # logging.exception("har log as \n %s" %
            #                   context.browser.get_log('har'))
            clean_env(context)
            raise Exception("Failed to login")


def after_tag(context, tag):
    '''
    针对tag执行后的行为
    '''
    if tag == 'NEED_LOGIN':
        try:
            log_out(context)
        except Exception as e:
            context.browser.get_screenshot_as_file('logout_fail.png')
            logging.exception("Error occured as %s" % e)
            # logging.exception("browser log as \n %s" %
            #                   context.browser.get_log('browser'))
            # logging.exception("har log as \n %s" %
            #                   context.browser.get_log('har'))
            clean_env(context)
            raise Exception("Failed to logout")


def before_scenario(context, scenario):
    '''
    在每个scenario开始之前做
    '''
    # 临时选择，这里直接忽略了Login相关的case
    # context.browser.switch_to.default_content()

def after_scenario(context, scenario):
    '''
    在每个scenario开始之后做
    '''
    if scenario.status != 'passed':
        # 检测执行状态，当失败后，执行截图操作
        allure.attach(context.browser.get_screenshot_as_png(), name='screenshot-%s' %
                      gen_current_timestamp_str(),  attachment_type=AttachmentType.PNG)

def clean_temp_folder():
    '''
    清除临时文件夹
    '''
    temp_folders = [
        BASE_CONFIG['REPORT_FOLDER'],
        BASE_CONFIG['ALLURE_REPORT_FOLDER'],
        BASE_CONFIG['TEMP_FOLDER'],
        BASE_CONFIG["CHROME"]["DOWNLOAD_PATH"]
    ]
    clean_folders(temp_folders)

def initialize_browser(context):
    '''
    初始化浏览器
    '''
    # change to use docker
    # use chrome
    context.browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities={'browserName': 'chrome'})
    context.browser_spy = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities={'browserName': 'firefox'})
    # use firefox
    # context.browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities={'browserName': 'firefox'})

    # if BASE_CONFIG["RUN"]["RUN_BROWSER"] == 'chrome':
    #     # 谷歌浏览器
    #     options = webdriver.ChromeOptions()
    #     prefs = {
    #         "profile.default_content_settings.popups": BASE_CONFIG["CHROME"]["IS_SHOW_DOWNLOAD_DIALOG"],
    #         "download.default_directory": BASE_CONFIG["CHROME"]["DOWNLOAD_PATH"]
    #     }
    #     options.add_experimental_option('prefs', prefs)
    #     # set as headless
    #     if BASE_CONFIG["RUN"]["RUN_BROWSER_MODE"] == 'headless':
    #         options.add_argument('headless')
    #         options.add_argument('disable-gpu')
    #         options.add_argument('window-size=1280x960')
    #     context.browser = webdriver.Chrome(chrome_options=options)
    # elif BASE_CONFIG["RUN"]["RUN_BROWSER"] == 'phantomjs':
    #     # 修改phantomJS的UserAgent
    #     desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    #     desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
    #         'AppleWebKit/537.36 (KHTML, like Gecko) ' \
    #         'Chrome/39.0.2171.95 Safari/537.36'
    #     context.browser = webdriver.PhantomJS(
    #         desired_capabilities=desired_capabilities)
        