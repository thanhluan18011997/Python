"""
learn all about class

"""

class Year:
    def __get__(self, instance, owner):
        print("da vao det of descriptor")
        return 4

    def __set__(self, instance, value):
        print("da vao set    of descriptor")
        self.value = value


class Person:
    tuoi = Year()

    @property
    def name(self):
        print("name getter")
        return self._name

    @name.setter
    def name(self, valu):
        print("name setter")
        self._name = valu


a = Person()
a.tuoi = 3
print(a.tuoi)
a.name = "luan"
print(a.name)



class Employee:
    """
    manage attribute with __getattr__
    """
    def __init__(self, name):
        print("khoi tao")
        self.__name = name

    def __getattr__(self, item):
        print("getAttr")
        if "_" + self.__class__.__name__ + "__" + item in self.__dict__.keys():
            return self.__name
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        print("setAttr")
        if "_" + self.__class__.__name__ + "__" + key in self.__dict__.keys():
            self.__name = value
            print("co")
        else:
            object.__setattr__(self, key, value)


e = Employee("luan")
print(e.name)
e.name = "long"
print(e.name)
print(e.__dict__.keys())


"""
Practice decorator
"""

def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, item):
            return getattr(self.wrapped, item)

    return Wrapper


class DecoratorClass:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args):
        self.wrapper = self.cls(*args)
        return self

    def __getattr__(self, item):
        return getattr(self.wrapper, item)


@DecoratorClass
class Animal:
    def __init__(self, x, y):
        self.x = "navzvzvme"


l = Animal("depzzzzzzz", "luannnn")
print(l.x)

import time


def giaithuaDecorator(func):
    def wrapper(*args):
        start = time.clock()
        result = func(*args)
        print("function consume time: {}".format(time.clock() - start))
        return result

    return wrapper


class GiaithuaDecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args)
        print("function consume time: {}".format(time.clock() - start))
        return result


@giaithuaDecorator
def functiongt(n):
    s = 1
    for i in range(n):
        s *= i
    return s


functiongt(10)

"""
Build singleton design pattern with decorator

"""
def singleton(aClass):  # On @ decoration
    instance = {}

    def onCall(*args, **kwargs):  # On instance creation
        nonlocal instance  # 3.X and later nonlocal
        if instance == None:
            instance = aClass(*args, **kwargs)  # One scope per class
        return instance

    return onCall


@singleton
class Man:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "hello" + self.name


@singleton
class Woman:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "hello" + self.name


m = Man("Luan");
n = Man("Long");
a = Woman("hoa")
b = Woman("hong")
print(m, n, a, b)


"""

learn Metadata

"""

class MetaClass(type):
    def __new__(meta, classname, supper, attrDict):
        print("gone meta class new with ", classname, supper, attrDict, sep="___")
        print("all attr: ", meta.__dict__.keys())
        return type.__new__(meta, classname, supper, attrDict)

    def __init__(Class, classname, supper, attrDict):
        print("gone meta class Init with ", classname, supper, attrDict, sep="___")
        return type.__init__(Class, classname, supper, attrDict)


class dog(Person,metaclass=MetaClass):
    data=1
    def __init__(self,name):
        self.name=name
print("created Class")
d=dog("lucky")
print("created instance")
def show(x):
    print(x)

class MetaCls(type):
    def __new__(meta,cls,supper,attrDict):
        attrDict["show1"]=show
        return type.__new__(meta,cls,supper,attrDict)
class A(metaclass=MetaCls):
    def __init__(self,name):
        self.name=name
    atrr=1
    def method1(self):
        print("method1")
    def __repr__(self):
        return self.name
a1=A("Luan dzzzzzzzzzz")
a1.show1()
A.show1("okkkkkkk ne")


"""
practice Iterator

"""

class Iterator:
    a = 0
    b = 1
    i = 0
    def __init__(self, count):
        self.count=count

    def __iter__(self):
        while True:
            if (Iterator.i > self.count):
                raise StopIteration
                break
            else:
                result = Iterator.a + Iterator.b
                Iterator.a = Iterator.b
                Iterator.b = result
                Iterator.i += 1
                yield result
                print("luandzzzzzz")


for i in Iterator(5):
    print(i)


