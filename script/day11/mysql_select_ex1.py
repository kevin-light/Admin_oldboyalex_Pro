import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='111111',db='testdb')
cursor = conn.cursor()

#effect_row = cursor.execute("select * from student where age > %s",(17,))
effect_row = cursor.execute("insert into student(name,age) values(%s,%s)",["xiaoliu",21])

conn.commit()
cursor.close()
conn.close()

#
if __name__ == '__main__':
    #cursor.encode()
    print(cursor.fetchone())
    print(" - -  - -")
    print(cursor.fetchall())

