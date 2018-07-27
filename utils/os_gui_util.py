# -*- coding: UTF-8 -*-
'''
操作系统界面常用操作方法
基于pyautogui
'''

import pyautogui
import os
import time

def os_upload_file(upload_file, upload_btn_img, sleep_time=5):
    """
    支持系统本身的上传文件组件
    TODO
        1. 智能等待窗口出现、消失
        2. 上传按钮智能匹配
    """
    time.sleep(sleep_time)
    pyautogui.moveTo(1, 1)
    pyautogui.PAUSE = 1
    secs_between_keys = 0.1
    pyautogui.typewrite(upload_file, interval=secs_between_keys)
    button_x, button_y = pyautogui.locateCenterOnScreen(upload_btn_img)
    pyautogui.click(button_x, button_y)
    time.sleep(sleep_time)