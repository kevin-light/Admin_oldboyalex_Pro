class Dog(object):

    name = "123"
    n = 333

    def __init__(self,name):
        self.name = name



    #@staticmethod   # 静态方法
    #@classmethod    #leifangfa  没用

    @property
    def eat(self):
        print("%s is eating %s" % (self.name,'dd'))

    @eat.setter
    def eat(self,food):
        print("set to foot",food)

    def talk(self):
        print("%s is talking .." % self.name)

d = Dog('aaa')

d.eat

d.eat = "baozhi"