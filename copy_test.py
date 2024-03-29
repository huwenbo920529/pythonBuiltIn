# coding:utf-8
import copy

# 直接赋值：简单地拷贝对象的引用，两个对象的id相同。就是对象的引用（别名），就是给当前内存中的对象增加一个“标签”而已。
# 通过使用内置函数 id() ，可以看出指向内存中同一个对象。
# 直接赋值既不是浅拷贝也不是深拷贝！也就是赋值后两者完全一样，相当于视图（numpy），没有copy到额外的空间中。
a = [1, 2, [3, 4]]
b = a
b[2][0] = 100
b[1] = 22
a[0] = 55
print a
print b


# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。即浅复制只复制对象本身，没有复制该对象所引用的对象。
l1 = [1, 2, [3, 4]]
l2 = copy.copy(l1)
l2[2][0] = 100
print l1   # [1, 2, [100, 4]]
print l2   # [1, 2, [100, 4]]

l2[1] = 99
print l1  # [1, 2, [100, 4]]
print l2  # [1, 99, [100, 4]]


# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。即创建一个新的组合对象，
# 同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。
l3 = [1, 2, [3, 4]]
l4 = copy.copy(l1)
l4[2][0] = 100
print l3   # [1, 2, [3, 4]]
print l4   # [1, 2, [100, 4]]

l4[1] = 99
print l3  # [1, 2, [3, 4]]
print l4  # [1, 99, [100, 4]]


# ********************************************************************************************
# 改变copy的默认行为
# 在定义类的时候，通过定义__copy__和__deepcopy__方法，可以改变copy的默认行为。下面是一个简单的例子:
class CopyObj(object):
    def __init__(self):
        print "CopyObj"

    def __copy__(self):
        print "Hello"
obj = CopyObj()
obj1 = copy.copy(obj)