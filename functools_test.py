# coding:utf-8
import functools
from functools import cmp_to_key, partial, total_ordering, wraps


# 1.cmp_to_key
# 将老式的比较函数（comparison function）转换为关键字函数（key function），与接受key function的工具一同使用
# 例如sorted，min，max，heapq.nlargest，itertools.groupby），该函数主要用于将程序转换成Python 3格式的，
# 因为Python 3中不支持比较函数。
# 比较函数是可调用的，接受两个参数，比较这两个参数并根据他们的大小关系返回负值、零或者正值中的一个。
# 关键字函数也是可调用的，接受一个参数，同时返回一个可以用作排序关键字的值。
def compare(ele1, ele2):
    return ele2 - ele1

a = [2, 3, 4]
print sorted(a, key=cmp_to_key(compare))


# 2.partial
# functools.partial(func, *args, **keywords)，函数装饰器，返回一个新的partial对象。
# 调用partial对象和调用被修饰的函数func相同，只不过调用partial对象时传入的参数个数通常要少于调用func时传入的参数个数。
# 当一个函数func可以接收很多参数，而某一次使用只需要更改其中的一部分参数，其他的参数都保持不变时，
# partial对象就可以将这些不变的对象冻结起来，这样调用partial对象时传入未冻结的参数，
# partial对象调用func时连同已经被冻结的参数一同传给func函数，从而可以简化调用过程。
# 如果调用partial对象时提供了更多的参数，那么他们会被添加到args的后面，
# 如果提供了更多的关键字参数，那么它们将扩展或者覆盖已经冻结的关键字参数。
def add(a, b):
    return a + b
add3 = partial(add, 3)
add5 = partial(add, 5)
print add3(4)
print add5(10)


# 3.reduce
# 与Python内置的reduce函数一样，为了向Python3过渡
a = range(1, 5)
print reduce(lambda x, y: x+y, a)
print functools.reduce(lambda x, y: x+y, a)


# 4.total_ordering
# 这是一个类装饰器，给定一个类，这个类定义了一个或者多个比较排序方法，这个类装饰器将会补充其余的比较方法，
# 减少了自己定义所有比较方法时的工作量；
# 被修饰的类必须至少定义 __lt__()， __le__()，__gt__()，__ge__()中的一个，同时，被修饰的类还应该提供 __eq__()方法。
@total_ordering
class Person(object):
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    # 定义相等的比较函数
    def __eq__(self, other):
        return (self.lastname.lower(), self.firstname.lower()) == (other.lastname.lower(), other.firstname.lower())

    # 定义小于的比较函数
    def __lt__(self, other):
        return (self.lastname.lower(), self.firstname.lower()) < (other.lastname.lower(), other.firstname.lower())
print dir(Person)
p1 = Person(lastname='san', firstname='zhang')
p2 = Person(lastname='si', firstname='li')
print p1 == p2
print p1 < p2
print p1 <= p2
print p1 > p2
print p1 >= p2


# 5.update_wrapper
# 更新一个包裹（wrapper）函数，使其看起来更像被包裹（wrapped）的函数。
# 可选的参数指定了被包裹函数的哪些属性直接赋值给包裹函数的对应属性，
# 同时包裹函数的哪些属性要更新而不是直接接受被包裹函数的对应属性，
# 参数assigned的默认值对应于模块级常量WRAPPER_ASSIGNMENTS（
# 默认地将被包裹函数的 __name__， __module__，和 __doc__ 属性赋值给包裹函数），
# 参数updated的默认值对应于模块级常量WRAPPER_UPDATES（默认更新wrapper函数的 __dict__ 属性）。
# 这个函数的主要用途是在一个装饰器中，原函数会被装饰（包裹），装饰器函数会返回一个wrapper函数，
# 如果装饰器返回的这个wrapper函数没有被更新，那么它的一些元数据更多的是反映wrapper函数定义的特征，无法反映wrapped函数的特性。


# 6 wraps
# 这个函数可用作一个装饰器，简化调用update_wrapper的过程，调用这个函数等价于调用
# partial(update_wrapper, wrapped = wrapped, assigned = assigned,updated = updated)。
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decrated function'
        return f(*args, **kwds)
    return wrapper


@my_decorator
def example():
    """DocString"""
    print 'Called example function'

example()
print example.__name__
print example.__doc__
