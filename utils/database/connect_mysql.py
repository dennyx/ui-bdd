#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    连接数据库
'''
import pymysql as MySQLdb

class Connect_Database():

    def __init__(self):
        self.host = '10.43.2.7'
        self.port = 3306
        self.user = 'root'
        self.password = 'root'
        self.db = 'froad_cbank_dev_anhui'

    def excute_sql(self,sql):
        '''
            执行sql
        '''
        self.conn= MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,db=self.db)
        self.cur = self.conn.cursor()
        if "select" in sql:
            result = self.cur.execute(sql)
            info = self.cur.fetchmany(result)
            return info
        else:
            self.cur.execute(sql)
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    sql = 'select * from f_mgr_role'
    testclass = Connect_Database()
    theresult = testclass.excute_sql(sql)
    for i in theresult:
        print(i)