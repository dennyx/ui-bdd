#!/usr/bin/env python
# -- coding=utf-8 --

"""
执行查询

"""

from .db_base import DB_BASE

import pymysql as MySQLdb

CONNECTION = 1

DB_CONN_STR = 'localhost,test,test,test'

class DB_TOOL(DB_BASE):
    """
    用于查询数据库最大连接数
    """

    def execute_sql(self, sql):
        '''
        执行sql
        '''
        result = self.sql_executor(sql)
        return result

    def check_database(self):
        '''
        检查数据库
        '''
        result = self.execute_sql('select 1 from dual')
        if not result:
            raise Exception('Invalid database connection')

if __name__ == '__main__':
    db_mysql = DB_TOOL(DB_CONN_STR)
    db_mysql.execute_sql('select * from f_transaction_code limit 1')
    db_mysql.close_db()