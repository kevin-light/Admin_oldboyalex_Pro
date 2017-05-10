import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:111111@127.0.0.1/testdb",encoding="utf-8",echo=True)
Base = declarative_base()   #生成ROM基类

class User(Base):
    __tablename__ = 'user'  #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)    #创建表结构

Session_class = sessionmaker(bind=engine)  #创建与数据库的会话session class，注意，这里返回的是一个session的是个class，不是实例
Session = Session_class()   #生成session实例 == cursor
user_obj = User(name="alex",password="alex3741")    #生成你要创建的数据对象
user_obj2 = User(name='jack',password="123")
print(user_obj.name,user_obj.id)
Session.add(user_obj)   #把要创建的数据对象添加到session里
Session.add(user_obj2)  #把要创建的数据对象添加到session里
print(user_obj.name,user_obj.id)  #
Session.commit()    #同意提交，创建数据