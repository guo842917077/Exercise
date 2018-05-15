"""
数据库管理类
python3 使用pymysql
"""
import pymysql


def createConnect(host, port, user, passwor, database):
    conn = pymysql.connect(host, port, user, passwor, database)
    return conn

def getPyMysql(x):
    return pymysql.Binary(x)