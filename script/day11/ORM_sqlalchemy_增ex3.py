from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:111111@localhost:3306/testdb?charset=utf8",encoding="utf-8")
Base = declarative_base()
class User(Base):
    __tablename__ = 'user_1'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s',password='%s')>" % (self.name,self.password)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()

    #增加
    # user_obj = User(name="11",password="22")
    # print(user_obj.name,user_obj.id)
    # Session.add(user_obj)
    # print(user_obj.name, user_obj.id)
    #
    # Session.commit()

    # 查询
    # my_user = Session.query(User).filter_by(name="11").first()
    # # print(my_user.id,my_user.name,my_user.password)
    # print(my_user)

    #修改
    # my_user = Session.query(User).filter_by(name="11").first()
    # my_user.name = "55"
    # my_user.password = "55"
    # Session.commit()
    # print(my_user)

    #删除


    #回滚
    # my_user = Session.query(User).filter_by(name="11").first()
    # my_user.password = "66"
    # fake_user = User(name='rain',password='123456')
    # Session.add(fake_user)
    # print(my_user,fake_user)
    # Session.rollback()
    # Session.commit()
    # print(my_user,fake_user)

    #获取所有数据
    # print(Session.query(User.name,User.id).all())
    #
    #多条件查询
    # objs = Session.query(User).filter(User.id>0).filter(User.id<3).all()
    # print(objs)
    #
    # objs = Session.query(User).filter(User.id.in_(['4','5','6'])).all()
    # print(objs)

    #统计，分组
    # t = Session.query(User).filter(User.name.like("%a%")).all()
    # print(t)
    # t = Session.query(User).filter(User.name.like("%a%")).count()
    # print(t)
    #

    # from sqlalchemy import func
    # print(Session.query(func.count(User.name),User.name).group_by(User.name).all())
#SELECT count(user.name) AS count_1, user.name AS user_name
# FROM user GROUP BY user.name
