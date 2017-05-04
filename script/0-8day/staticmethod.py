# class Dog(object):
#
#     name = "123"
#     n = 333
#
#     def __init__(self,name):
#         self.name = name
#
#
#
#     #@staticmethod   # 静态方法
#     #@classmethod    #leifangfa  没用
#
#     @property
#     def eat(self):
#         print("%s is eating %s" % (self.name,'dd'))
#
#     @eat.setter
#     def eat(self,food):
#         print("set to foot",food)
#
#     def talk(self):
#         print("%s is talking .." % self.name)
#
# d = Dog('aaa')
#
# d.eat
#
# d.eat = "baozhi"


# class Dog(object):
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod  # 把eat方法变为静态方法
#     def eat(self):
#         print("%s is eating" % self.name)
#
#
# d = Dog("ChenRonghua")
# d.eat()


class Dog(object):

    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat():
        print(" is eating")



d = Dog("ChenRonghua")
d.eat()