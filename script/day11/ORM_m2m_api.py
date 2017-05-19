import ORM_m2m
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=ORM_m2m.engine)
session = Session_class()

# b1 = ORM_m2m.Book(name="alex学习Pyhton",pub_date="2017-05-06")
# b2 = ORM_m2m.Book(name="alex学习php",pub_date="2017-05-07")
# b3 = ORM_m2m.Book(name="alex学习hook up girls",pub_date="2017-05-08")
#
# a1 = ORM_m2m.Author(name="alex")
# a2 = ORM_m2m.Author(name="jcak")
# a3 = ORM_m2m.Author(name="rain")
# #
# b1.authors = [a1,a3]
# b3.authors = [a1,a2,a3]
# #
# session.add_all([a1,a2,a3,b1,b2,b3])

# author_obj = session.query(ORM_m2m.Author).filter(ORM_m2m.Author.name=="alex").first()
# print(author_obj.books[1].pub_date)
# book_obj = session.query(ORM_m2m.Book).filter(ORM_m2m.Book.id==2).first()
# print(book_obj.authors)

author_obj = session.query(ORM_m2m.Author).filter(ORM_m2m.Author.name=="rain").first()
session.delete(author_obj)

session.commit()
