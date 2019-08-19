# coding:utf-8
from socket import *
import weakref


# 创建弱引用
# 你可以通过调用weakref模块的ref(obj[,callback])来创建一个弱引用，obj是你想弱引用的对象，callback是一个可选的函数，
# 当因没有引用导致Python要销毁这个对象时调用。回调函数callback要求单个参数（弱引用的对象）
s = socket(AF_INET, SOCK_STREAM)
ref = weakref.ref(s)
print s
print ref
print ref()  # 调用它来访问被引用的对象, 这里就是s对象

print weakref.getweakrefcount(s)  # 返回弱引用数
print weakref.getweakrefs(s)  # 所给对象的引用列表


# 创建代理对象
# 代理对象是弱引用对象，它们的行为就像它们所引用的对象，这就便于你不必首先调用弱引用来访问背后的对象。
# 通过weakref模块的proxy(obj[,callback])函数来创建代理对象。使用代理对象就如同使用对象本身一样
ref2 = weakref.proxy(s)
print ref2
ref2.close()


# *******************************************************************************************
# 弱引用使用的机会不是很多，一般用来进行 cache 编程。我们可以使用 weakref.ref() 来创建一个弱引用。
import sys
class Class1(object):
    def test(self):
        print "test..."
o = Class1()
print sys.getrefcount(o)
r = weakref.ref(o)
print sys.getrefcount(o)  # 引用计数并没有改变
o2 = r()  # 获取弱引用所指向的对象
print o
print o2
print o is o2  # True
print sys.getrefcount(o)

o = None
o2 = None
print r  # 当对象引用计数为零时，弱引用失效。

