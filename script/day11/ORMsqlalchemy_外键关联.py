from sqlalchemy import create_engine,Column,Integer,String,DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:111111@localhost:3306/testdb?charset=utf8",encoding="utf-8")
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_data = Column(DATE,nullable=False)

    def __repr__(self):
        return "<User(name='%s',id='%s')>" % (self.name,self.id)


class StudentRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True)
    day = Column(String(32),nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))

    student = relationship("Student",backref="my_study_record")  #这个nb，允许你在user表里通过backref字段反向查出所有它在student表里的关联项

    def __repr__(self):
        return "<%s day19 = %s  status=%s>" % (self.student.name,self.day,self.status)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    Session_class = sessionmaker(bind=engine)
    session = Session_class()

    # s1 = Student(name="alex",register_data="2017-01-01")
    # s2 = Student(name="jack",register_data="2017-02-01")
    # s3 = Student(name="rain",register_data="2017-03-01")
    # s4 = Student(name="eric",register_data="2017-04-01")
    #
    # study_obj1=StudentRecord(day19=1,status="YES",stu_id=1)
    # study_obj2=StudentRecord(day19=2,status="no",stu_id=1)
    # study_obj3=StudentRecord(day19=3,status="YES",stu_id=1)
    # study_obj4=StudentRecord(day19=4,status="YES",stu_id=2)
    #
    # session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])

    stu_obj = session.query(Student).filter(Student.name=="alex").first()
    print(stu_obj.my_study_record)


    session.commit()







#
#     # obj = Session.query(User).first()
#     # for i in obj.addresses:
#     #     print(i)
#     # addr_obj = Session.query(Address).first()
#     # print(addr_obj.user.name)
#
#     obj = Session.query(User).filter(User.name=='rain').all([0])
#     print(obj.addresses)
#
#     obj.addresses = [Address(email_address="123123"),
#                      Address(email_address="123111")]
#     Session.commit()