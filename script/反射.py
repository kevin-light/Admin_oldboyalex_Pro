class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        self.food = food
        print("%s is ratign.." % self.name)

d = Dog("aaa")
choice = input(">>").strip()

if hasattr(d,choice):
    func=getattr(d,choice)
    func("bbb")