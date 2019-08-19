# coding:utf-8
from abc import ABCMeta, abstractmethod, abstractproperty


class Drawable():
    __metaclass__ = ABCMeta

    @abstractproperty
    def size(self):
        pass

    @abstractmethod
    def draw(self, x, y, scale=1.0):
        pass

    def double_draw(self, x, y):
        self.draw(x, y, scale=2.0)


class Circle(Drawable):  # Cicle如果没有override draw函数和size 属性，那么实例化的时候就会报错
    def draw(self, x, y, scale=1.0):
        print (x * scale, y * scale)

    @property
    def size(self):
        return 'Circle size'

c = Circle()
print dir(c)
print isinstance(c, Drawable)
print isinstance(c, Circle)


# 使用抽象类函数的register方法注册具体的class
# 通过注册的类，可以直接实例化，但是无法访问抽象类的所有成员
# 其实就是只是让isinstance、issubclass识别注册的类为抽象类的成员和实例
class Rectangle():
    pass

Drawable.register(Rectangle)
r = Rectangle()
print isinstance(r, Drawable)
print isinstance(r, Rectangle)