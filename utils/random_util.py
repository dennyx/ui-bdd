# -*- coding: UTF-8 -*-

from datetime import datetime

def gen_current_timestamp_str():
    current = datetime.now()
    return current.strftime('%Y%m%d%H%M%S%f')
