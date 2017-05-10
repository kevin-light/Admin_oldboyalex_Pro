# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
#
# # 游标设置为字典类型
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# r = cursor.execute("call p1()")
#
# result = cursor.fetchone()
#
# conn.commit()
# cursor.close()
# conn.close()


import pymysql
conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd='111111',db='testdb')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
r = cursor.execute("select * from student")


print(cursor.fetchall())
conn.commit()
cursor.close()
conn.close()