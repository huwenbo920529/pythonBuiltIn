# coding:utf-8
import gc
from sys import getrefcount


# 返回所有被垃圾回收器（collector）管理的对象。这个函数非常基础！只要python解释器运行起来，就有大量的对象被collector管理，因此，该函数的调用比较耗时！
print len(gc.get_objects())

# 我们可以使用sys包中的getrefcount()，来查看某个对象的引用计数。
# 需要注意的是，当使用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用。
# 因此，getrefcount()所得到的结果，会比期望的多1。
a = [1, 2, 3]
print(getrefcount(a))   # 2
b = a
print(getrefcount(b))  # 3

# 返回obj对象直接指向的对象
print gc.get_referents(b)

# 返回所有直接指向obj的对象
print gc.get_referrers(b)


# 对象引用对象
# Python的一个容器对象(container)，比如表、词典等，可以包含多个对象。
# 实际上，容器对象中包含的并不是元素对象本身，是指向各个元素对象的引用。
# 我们也可以自定义一个对象，并引用其它对象:
class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

b = [1, 2, 3]
a = from_obj(b)
print id(b)
print id(a.to_obj)

a = [1, 2, 3]
print(getrefcount(a))
b = [a, a]
print(getrefcount(a))


# *****************************************************************************
# 容器对象的引用可能构成很复杂的拓扑结构。我们可以用objgraph包来绘制其引用关系
x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

import objgraph
objgraph.show_refs([z], filename='ref_top.dot')


x = [1, 2, 3]
y = x
print(getrefcount(y))

del x
print(getrefcount(y))


# 垃圾回收时，Python不能进行其它的任务。频繁的垃圾回收将大大降低Python的工作效率。如果内存中的对象不多，就没有必要总启动垃圾回收。
# 所以，Python只会在特定条件下，自动启动垃圾回收。
# 当Python运行时，会记录其中分配对象(object allocation)和取消分配对象(object deallocation)的次数。当两者的差值高于某个阈值时，垃圾回收才会启动。
# 我们可以通过gc模块的get_threshold()方法，查看该阈值:
print gc.get_threshold()  # 返回(700, 10, 10)，后面的两个10是与分代回收相关的阈值，后面可以看到。700即是垃圾回收启动的阈值。可以通过gc中的set_threshold()方法重新设置。

print gc.get_count()  # 返回没代中当前的对象数

# 我们也可以手动启动垃圾回收，即使用gc.collect()。
gc.collect()
