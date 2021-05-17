from collections import namedtuple
def nameTuple():
    Color=namedtuple("color",["red","green","blue"])
    color=Color(red=255,green=10,blue=25)
    print(color.red,Color.__name__)

nameTuple()

from abc import ABC,abstractmethod
class Abstraction(ABC):
    @abstractmethod
    def abstract(self):
        pass
class  ConcreteAbstraction(Abstraction):
    def abstract(self):
        print("override abstract method")
ab=ConcreteAbstraction()
ab.abstract()