# import sys
# sys.path.append('F:/Python/Admin_oldboyalex_Pro/script/day11/orm_many_fk.py')

import orm_many_fk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_many_fk.engine)
session = Session_class()
# addr1 = orm_many_fk.Address(street="tiantongyaun",city="changping",state="bj")
# addr2 = orm_many_fk.Address(street="wudaokou",city="haidian",state="bj")
# addr3 = orm_many_fk.Address(street="yanjiao",city="langfang",state="hb")
#
# session.add_all([addr1,addr2,addr3])
# c1 = orm_many_fk.Customer(name="alex",billing_address=addr2,shipping_address=addr2)
# c2 = orm_many_fk.Customer(name="jack",billing_address=addr3,shipping_address=addr3)
#
# session.add_all([c1,c2])

obj = session.query(orm_many_fk.Customer).filter(orm_many_fk.Customer.name=='alex').first()
print(obj.name,obj.billing_address,obj.shipping_address)

session.commit()