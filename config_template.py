# -*- coding: UTF-8 -*-
'''
基本配置信息
'''

import os

current_path = os.path.dirname(os.path.realpath(__file__))

BASE_CONFIG = {
    # Chrome设置
    "CHROME": {
        # 默认的下载路径
        "DOWNLOAD_PATH": os.path.join(current_path, "download"),
        # 是否弹出下载框，1为弹出，0为不弹
        "IS_SHOW_DOWNLOAD_DIALOG": 0,
        # chrome_driver默认路径，初始启动时，加载到环境变量中
        "DRIVER_PATH": "res"
    },
    # 基本信息
    "SYSTEM_INFO": {
        "URL": "",
        "OUTLET_ACCOUNT": "",
        "MERCHANT_ACCOUNT": "",
        "PASSWORD": ""
    },
    # 关联系统
    "DEPENDENCY_SYSTEM":{
        "BANK": {
            "URL": "",
            "WANGDIAN_ACCOUNT": "",
            "ADMIN_ACCOUNT": "",
            "MASTER_ACCOUNT": "",
            "PASSWORD": ""
        }
    },
    # 报告目录
    "REPORT_FOLDER": os.path.join(current_path,"report"),
    # allure报告目录
    "ALLURE_REPORT_FOLDER": os.path.join(current_path,"allure_report"),
    # 临时文件目录
    "TEMP_FOLDER": os.path.join(current_path,"temp"),
    # 数据库环境
    "DB": {
        "DB_TYPE": "MYSQL",
        "DB_CONN_STR": "localhost,test,test,test", 
    },
    # 执行环境
    "RUN": {
        # driver选择 chrome, firefox, ie, phantomjs
        "RUN_BROWSER": "chrome",
        # 浏览器运行模式headless, gui
        "RUN_BROWSER_MODE": "gui",
        # 执行模式 hub, standalone, parall
        "RUN_MODE": "standalone",
    },
    # 日志管理
    "LOG": {
        "LOG_LEVEL": "info",
        "LOG_FILE_NAME": "anhui_merchant.log",
    },
    # 邮件管理
    "EMAIL": {
        "IS_SEND_EMAIL": 0,
        "SMTP_SERVER": "",
        "SENDER_EMAIL": "",
        "SENDER_PASSWORD": "",
    }
}
