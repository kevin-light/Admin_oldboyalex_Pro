from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship

#engine = create_engine("mysql+pymysql://root:111111@127.0.0.1:3306/testdb?charset",echo=True,max_overflow=5)
engine = create_engine("mysql+pymysql://root:111111@127.0.0.1:3306/testdb?charset",max_overflow=5)
Base = declarative_base()

# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer,primary_key=True)
#     name = Column(String(32))
#     extra = Column(String(16))

# Base.metadata.create_all(engine)

# #添加数据
#
# Session_class = sessionmaker(bind=engine)
# Session = Session_class()
#
# user_obj = Users(name="alex",extra="alex3714")
# print('1',user_obj.name,user_obj.extra)
#
# Session.add(user_obj)
# print(user_obj.name,user_obj.extra)
#
# Session.commit()


Session_class = sessionmaker(bind=engine)
Session = Session_class()
session.commit()
