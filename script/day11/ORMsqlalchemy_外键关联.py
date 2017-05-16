from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:111111@localhost:3306/testdb?charset=utf8",encoding="utf-8")
Base = declarative_base()

class User(Base):
    __tablename__ = 'user_1'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s',password='%s')>" % (self.name,self.password)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer,primary_key=True)
    email_address = Column(String(32),nullable=False)
    user_id = Column(Integer,ForeignKey('user_1.id'))

    user_1 = relationship("User",backref="addresses")  #这个nb，允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

Base.metadata.create_all(engine)

if __name__ == '__main__':
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()

    # obj = Session.query(User).first()
    # for i in obj.addresses:
    #     print(i)
    # addr_obj = Session.query(Address).first()
    # print(addr_obj.user.name)

    obj = Session.query(User).filter(User.name=='rain').all([0])
    print(obj.addresses)

    obj.addresses = [Address(email_address="123123"),
                     Address(email_address="123111")]
    Session.commit()