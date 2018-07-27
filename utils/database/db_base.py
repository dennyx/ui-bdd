#!/usr/bin/env python
# -- coding=utf-8 --

"""
检查数据库连接数的基类

"""

from abc import ABCMeta, abstractmethod

import pymysql as MySQLdb

class DB_BASE(object):
    """
    检查数据库连接的基类
    """
    __metaclass__ = ABCMeta

    def __init__(self, conn_str):
        """
        初始化
        """
        self.conn = None
        self.cursor = None
        self.connect_db(conn_str)
        self.html_table_info = {}
    
    def connect_db(self, conn_str):
        """
        连接数据库
        """
        conn_info_list = conn_str.split(",")
        self.conn = MySQLdb.connect(conn_info_list[0],conn_info_list[1],conn_info_list[2],conn_info_list[3],charset="utf8")
        # 指定返回数据为字典
        self.cursor = self.conn.cursor(cursor=MySQLdb.cursors.DictCursor)

    def sql_executor(self, sql):
        """
        执行SQL
        """
        self.cursor.execute(sql)  #使用cursor提供的方法来执行查询语句   
        data = self.cursor.fetchall()         #使用fetchall方法返回所有查询结果
        return data

    def close_db(self):
        """
        关闭游标和连接
        """
        self.cursor.close()            
        self.conn.close() 
