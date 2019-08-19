# coding:utf-8
import sys
import inspect
import copy_test


def foo(a):
    """
    add 1 to param and return the result
    :param a:
    :return: a + 1
    """
    b = 1 + a
    print b
    return b


class Cat(object):
    """
    class cat
    """
    def __init__(self, name='kitty'):
        self.name = name

    def sayHi(self):
        print self.name, 'say Hi!'

cat = Cat()
print Cat.sayHi  # <unbound method Cat.sayHi>
print cat.sayHi  # <bound method Cat.sayHi of <__main__.Cat object at 0x000000000341D518>>

print dir(cat)  # 获取实例的属性名，以列表形式返回
if hasattr(cat, 'name'):   # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger')
    print getattr(cat, 'name')
    print getattr(cat, 'sayHi')  # 若要调用该函数，可以getattr(cat, 'sayHi')()

# 模块(module)
# __doc__: 文档字符串。如果模块没有文档，这个值是None。
# __name__: 始终是定义时的模块名；即使你使用import .. as 为它取了别名，或是赋值给了另一个变量名。
# __dict__: 包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象。
# __file__: 包含了该模块的文件路径。需要注意的是内建的模块没有这个属性，访问它会抛出异常！
print copy_test.__doc__
print copy_test.__name__
print copy_test.__file__


# 类(class)
# __doc__: 文档字符串。如果类没有文档，这个值是None。
# __name__: 始终是定义时的类名。
# __dict__: 包含了类里可用的属性名-属性的字典；也就是可以使用类名.属性名访问的对象。
# __module__: 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象。
# __bases__: 直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类。
print Cat.__doc__
print Cat.__name__
print Cat.__dict__
print Cat.__module__
print Cat.__bases__


# 实例(instance)
# 实例是指类实例化以后的对象。
# __dict__: 包含了可用的属性名-属性字典。
# __class__: 该实例的类对象。对于类Cat，cat.__class__ == Cat 为 True。
print cat.__class__
print cat.__dict__


# 函数(function)
# 这里特指非内建的函数。注意，在类中使用def定义的是方法，方法与函数虽然有相似的行为，但它们是不同的概念。
# __doc__: 函数的文档；另外也可以用属性名func_doc。
# __name__: 函数定义时的函数名；另外也可以用属性名func_name。
# __module__: 包含该函数定义的模块名；同样注意，是模块名而不是模块对象。
# __dict__: 函数的可用属性；另外也可以用属性名func_dict。
# 不要忘了函数也是对象，可以使用函数.属性名访问属性（赋值时如果属性不存在将新增一个），或使用内置函数has/get/setattr()访问。不过，在函数中保存属性的意义并不大。
# func_defaults: 这个属性保存了函数的参数默认值元组；因为默认值总是靠后的参数才有，所以不使用字典的形式也是可以与参数对应上的。
# func_code: 这个属性指向一个该函数对应的code对象，code对象中定义了其他的一些特殊属性，将在下文中另外介绍。
# func_globals: 这个属性指向当前的全局命名空间而不是定义函数时的全局命名空间，用处不大，并且是只读的。
# func_closure: 这个属性仅当函数是一个闭包时有效，指向一个保存了所引用到的外部函数的变量cell的元组，如果该函数不是一个内部函数，则始终为None。这个属性也是只读的。
print foo.__doc__  # foo.func_doc
print foo.__name__  # foo.func_name
print foo.__module__
print foo.__dict__  # foo.func_dict
print foo.func_defaults
print foo.func_code
print foo.func_globals
print foo.func_closure


# 生成器(generator)
# 生成器是调用一个生成器函数(generator function)返回的对象，多用于集合对象的迭代。
# __iter__: 仅仅是一个可迭代的标记。
# gi_code: 生成器对应的code对象。
# gi_frame: 生成器对应的frame对象。
# gi_running: 生成器函数是否在执行。生成器函数在yield以后、执行yield的下一行代码前处于frozen状态，此时这个属性的值为0。
# next|close|send|throw: 这是几个可调用的方法，并不包含元数据信息，如何使用可以查看生成器的相关文档。
def gen():
    for n in range(5):
        yield n
g = gen()
print g
print g.__iter__()
print g.gi_code
print g.gi_frame
print g.gi_running


# 代码块可以由类源代码、函数源代码或是一个简单的语句代码编译得到。这里我们只考虑它指代一个函数时的情况；2.5节中我们曾提到可以使用函数的func_code属性获取到它。code的属性全部是只读的。
# co_argcount: 普通参数的总数，不包括*参数和**参数。
# co_names: 所有的参数名（包括*参数和**参数）和局部变量名的元组。
# co_varnames: 所有的局部变量名的元组。
# co_filename: 源代码所在的文件名。
# co_flags:  这是一个数值，每一个二进制位都包含了特定信息。较关注的是0b100(0x4)和0b1000(0x8)，如果co_flags & 0b100 != 0，说明使用了*args参数；如果co_flags & 0b1000 != 0，说明使用了**kwargs参数。另外，如果co_flags & 0b100000(0x20) != 0，则说明这是一个生成器函数(generator function)。


# 栈帧(frame)
# 栈帧表示程序运行时函数调用栈中的某一帧。函数没有属性可以获取它，因为它在函数调用时才会产生，而生成器则是由函数调用返回的，所以有属性指向栈帧。想要获得某个函数相关的栈帧，则必须在调用这个函数且这个函数尚未返回时获取。你可以使用sys模块的_getframe()函数、或inspect模块的currentframe()函数获取当前栈帧。这里列出来的属性全部是只读的。
# f_back: 调用栈的前一帧。
# f_code: 栈帧对应的code对象。
# f_locals: 用在当前栈帧时与内建函数locals()相同，但你可以先获取其他帧然后使用这个属性获取那个帧的locals()。
# f_globals: 用在当前栈帧时与内建函数globals()相同，但你可以先获取其他帧
def add(x, y=1):
    f = inspect.currentframe()
    print f.f_locals   #   same as locals()
    print f.f_back   #   <frame object at 0x...>
    return x + y
add(2)


# 追踪(traceback)
# 追踪是在出现异常时用于回溯的对象，与栈帧相反。由于异常时才会构建，而异常未捕获时会一直向外层栈帧抛出，所以需要使用try才能见到这个对象。
# 你可以使用sys模块的exc_info()函数获得它，这个函数返回一个元组，元素分别是异常类型、异常对象、追踪。traceback的属性全部是只读的。
# tb_next: 追踪的下一个追踪对象。
# tb_frame: 当前追踪对应的栈帧。
# tb_lineno: 当前追踪的行号。
x = 1
y = 0
try:
    print x / y
except Exception as e:
    except_info = sys.exc_info()
    print except_info
    tb = except_info[2]
    print tb.tb_frame, tb.tb_lineno


# ****************************************************************************************8
# 使用inspect模块
# inspect模块提供了一系列函数用于帮助使用自省。下面仅列出较常用的一些函数，想获得全部的函数资料可以查看inspect模块的文档。
# 1.检查对象类型
# is{module|class|function|method|builtin}(obj):
# 检查对象是否为模块、类、函数、方法、内建函数或方法。
# isroutine(obj):
# 用于检查对象是否为函数、方法、内建函数或方法等等可调用类型。用这个方法会比多个is*()更方便，不过它的实现仍然是用了多个is*()
im = cat.sayHi
if inspect.isroutine(im):
    im()
print inspect.getmembers(cat)
print inspect.getmodule(copy_test)