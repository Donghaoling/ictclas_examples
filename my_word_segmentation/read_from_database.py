# -*- coding: UTF-8 -*-
__author__ = 'hzdonghaoling'
import MySQLdb
#从数据库中获得评论信息
def get_comments(db):
    cursor = db.cursor()
    sql_string_select = """select * from label_ods_src"""
    try:
        cursor.execute(sql_string_select)
        results = cursor.fetchone() #现在是fetchone()来测试，之后别忘了改成fetchall()
        return results
    except:
        print "Get comment Error"

db = MySQLdb.connect("223.252.211.186", "us_opinionmining", "wWCa5KqKhJnpbQSv", "us_opinion_mining", charset = "utf8") #要读取中文，所以加charset = "urf8"
results = get_comments(db)
print type(results)
s = results[4]
print s
