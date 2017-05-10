# import pymysql
#
# # 创建连接
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
# # 创建游标
# cursor = conn.cursor()
#
# # 执行SQL，并返回收影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2'")
#
# # 执行SQL，并返回受影响行数
# # effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))
#
# # 执行SQL，并返回受影响行数
# # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
#
#
# # 提交，不然无法保存新建或者修改的数据
# conn.commit()
#
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()



import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='111111',db='testdb')
cursor = conn.cursor()
effect_row = cursor.execute("select * from student")

# effect_row = cursor.execute("update hoses set host='1.1.1.2' where nid > %s",(1,))

# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)",[("1,1,1,11",1),("1.1.1.11",2)])

print(cursor.fetchone())   #取一条数据
print('- - - - - - - - - -')
print(cursor.fetchall())   #获取剩余所有数据

conn.commit()

cursor.close()
conn.close()