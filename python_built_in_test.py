# coding:utf-8
# 1.abs() 函数返回数字的绝对值。
import math
print abs(-3.9)  # 等价于，math.fabs(-3.9)
print math.fabs(-3.9)

# 2.dict() 函数用于创建一个字典。
# 语法：
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
print dict(a=1, b=2, c=3)  # 传入关键字
print dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # 映射方式构造字典
print dict([('a', 1), ('b', 1), ('c', 1)])  # 可迭代方式构造字典

# 3.help() 函数用于查看函数或模块用途的详细说明。
# print help('math')
a = [1, 2, 3]
# print help(a)
print help(a.append)

# 4.min() 方法返回给定参数的最小值，参数可以为序列。
print min(2+1, 3, 6+1)


# 5.setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在。
class A(object):
    bar = 1
a = A()
setattr(a, 'bar', 5)
print a.bar

# 6.getattr() 函数用于返回一个对象属性值。
print getattr(a, 'bar')
print getattr(a, 'bar2', 999)  # 对象a中不存在属性bar2时返回999

# 7.all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、FALSE 外都算 TRUE。
s = [1, 2, 0, 3]
print all(s)

# 8.dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
print dir(a)

# 9.hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
print hex(35)

# 10.next() 返回迭代器的下一个项目。next(iterator[, default])
# default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。
it = iter(s)
print next(it)

# 11.slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
# class slice(stop)
# class slice(start, stop[, step])
myslice = slice(5)
print myslice
arr = range(10)
if len(arr) > 5:
    print arr[myslice]

# 12.any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
# 元素除了是 0、空、FALSE 外都算 TRUE。
print any(s)

# 13.python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b), 对于浮点数，返回的是（math.floor(a/b), a%b）
print divmod(5.2, 3)

# 14.id() 函数用于获取对象的内存地址。
print id(s)

# 15.sorted() 函数对所有可迭代的对象进行排序操作。
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的sort方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
print sorted(it)

# 16.ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。 生成字符串类似 Python2 版本中 repr() 函数的返回值。
# print ascii('hello') python3的内置函数

# 17.enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
season = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(season))

# 18.Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
# Python2.x 中 input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。
# raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）
# 注意：input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
# 除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
# 注意：python3 里 input() 默认接收到的是 str 类型。
# input() 需要输入 python 表达式
# a = input("input a:")
# print type(a)
# b = input("input b:")  # 需要输入正确的python表达式, 比如："hello"而不是hello
# print type(b)
# # raw_input() 将所有输入作为字符串看待
# a = raw_input("input a:")
# print type(a)
# b = raw_input("input b:")
# print type(b)

# 19.oct() 函数将一个整数转换成8进制字符串。
print oct(21)


# 20.python staticmethod 返回函数的静态方法。该方法不强制要求传递参数.
class C(object):
    @staticmethod
    def f():
        print 'hello'
C.f()  # 静态方法无需实例化
c_object = C()
c_object.f()   # 也可以实例化后调用

# 21.bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
print bin(6)

# 22.eval() 函数用来执行一个字符串表达式，并返回表达式的值。
x = 7
print eval('3*x')

# 23.int() 函数用于将一个字符串或数字转换为整型。
# class int(x, base=10)  x -- 字符串或数字; base -- 进制数，默认十进制。
print int('0xa', 16)

# 24.python open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。

# 25.str() 函数将对象转化为适于人阅读的形式。

# 26.bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。

# 27.exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码, exec 返回值永远为 None。
exec("""for i in range(5):
            print i""")

# 28.isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
print isinstance(c_object, C)
print isinstance(c_object, (int, str, list)) # 是元组中的一个返回 True

# 29.ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，
# 返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
print ord('a')

# 30.sum() 方法对系列进行求和计算。sum(iterable[, start]) start -- 指定相加的参数，如果没有设置这个值，默认为0。
li = [1, 2, 3, 4]
print sum(li)
print sum(li, 2)  # 列表计算总和后再加 2

# 31.bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
print bytearray([1, 2, 3])[0]
print bytearray('runoob', 'utf-8')[0]


# 31.filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。filter(function, iterable)
# function -- 判断函数。 iterable -- 可迭代对象。
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)


# 32.issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。issubclass(class, classinfo)
class A(object):
    pass
class B(A):
    pass
print(issubclass(B, A))

# 33.pow() 方法返回 xy（x的y次方）的值  pow(x, y[, z])
print pow(2, 3)
# math 模块 pow()
# 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z,注意：x,y,z必须为整数
# 注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块pow只含两个参数，且会把参数转换为 float
print pow(2, 3, 3)
print math.pow(2.1, 3.1)

# 34.super() 函数是用于调用父类(超类)的一个方法。
# super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表
class FooParent(object):
    def __init__(self):
        self.parent = "I'am the parent"
        print "Parent"

    def bar(self, message):
        print "{} from Parent".format(message)

class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()  # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        print 'child'

    def bar(self, message):
        super(FooChild, self).bar(message)
        print 'Child bar function'
        print self.parent
fooChild = FooChild()
fooChild.bar('helloWorld!')

# 35.bytes 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。

# 36.float() 函数用于将整数和字符串转换成浮点数。

# 37.iter() 函数用来生成迭代器。iter(object[, sentinel])
# object -- 支持迭代的集合对象。
# sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
# 此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
lst = [1, 2, 3]
for i in iter(lst):
    print(i)

# 38.print() 方法用于打印输出，最常见的一个函数。

# 39.tuple 函数将列表转换为元组。。


# 40.callable() 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
class A(object):
    def method(self):
        pass
print callable(A)  # 类返回true
a = A()
print callable(a)  # 没有实现 __call__,返回false


# format --Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 %
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print 'value为：{0.value}'.format(my_value)
print("{:.2f}".format(3.1415926))
# 数字	    格式	输出	描述
# 3.1415926	{:.2f}	3.14	保留小数点后两位
# 3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
# -1	    {:+.2f}	-1.00	带符号保留小数点后两位
# 2.71828	{:.0f}	3	    不带小数
# 5	        {:0>2d}	 05	    数字补零 (填充左边, 宽度为2)
# 5	        {:x<4d}	 5xxx   数字补x (填充右边, 宽度为4)
# 10	    {:x<4d}	10xx	数字补x (填充右边, 宽度为4)
# 1000000	{:,}   1,000,000 以逗号分隔的数字格式
# 0.25	    {:.2%}	25.00%	百分比格式
# 1000000000{:.2e}	1.00e+09 指数记法
# 13	    {:10d}	    13	 右对齐 (默认, 宽度为10)
# 13	    {:<10d}	    13	 左对齐  (宽度为10)
# 13	    {:^10d}	    13	 中间对齐 (宽度为10)
# 11     '{:b}'.format(11)   1011    进制
#         '{:d}'.format(11)   11
#         '{:o}'.format(11)   13
#         '{:x}'.format(11)   b
#         '{:#x}'.format(11)  0xb
#         '{:#X}'.format(11)  0XB

# ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
# b、d、o、x 分别是二进制、十进制、八进制、十六进制。
# 此外我们可以使用大括号 {} 来转义大括号，如下实例：
print ("{} 对应的位置是 {{0}}".format("runoob"))


# 41.len()方法返回对象（字符、列表、元组等）长度或项目个数。

# 42.property() 函数的作用是在新式类中返回属性值。 class property([fget[, fset[, fdel[, doc]]]])
# fget -- 获取属性值的函数
# fset -- 设置属性值的函数
# fdel -- 删除属性值函数
# doc -- 属性描述信息
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value
        print self._x

    def delx(self):
        del self._x
        print 'del self._x'

    x = property(getx, setx, delx, "I'am the 'x' property")
c = C()
print c.x  # 触发 getx
c.x = 1  # 触发 setx
del c.x  # 触发 delx

# 43.type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。

# 44.chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回值是当前整数对应的ascii字符。
print chr(97)

# 45.frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。class frozenset([iterable])
print frozenset(range(10))

# 46.list() 方法用于将元组转换为列表。

# 47.Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
# Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。
# Python2 range() 函数返回的是列表。


# 47.vars() 函数返回对象object的属性和属性值的字典对象
class A(object):
    a = 1
print vars(A)
a = A()
print vars(a)  # {}


# 48.classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
class A(object):
    bar = 1

    def func1(self):
        print 'foo'

    @classmethod
    def func2(cls):
        print 'func2'
        print cls.bar
        cls().func1()  # 注意调用类的方法和获得类的属性的不同之处
A.func2()


# 49.locals() 函数会以字典类型返回当前位置的全部局部变量。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
def hel(arg):
    z = 1
    print locals()
hel(2)

# 50.repr() 函数将对象转化为供解释器读取的形式。
dic = {'runoob': 'runoob.com', 'google': 'google.com'}
print repr(dic)

# 51.zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同.利用 * 号操作符，可以将元组解压为列表。
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 10]
print list(zip(a, b))  # [(1, 4), (2, 5), (3, 6)]
print list(zip(a, c))  # [(1, 7), (2, 8), (3, 9)]
print zip(*zip(a, c))  # 与 zip 相反，*zip 可理解为解压，返回二维矩阵式 [(1, 2, 3), (7, 8, 9)]

# 52.compile() 函数将一个字符串编译为字节代码。
# compile(source, filename, mode[, flags[, dont_inherit]])
# source -- 字符串或者AST（Abstract Syntax Trees）对象。。
# filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
# mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
# flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
# flags和dont_inherit是用来控制编译源码时的标志
st = "for i in range(0,10): print(i)"
c = compile(st, '', 'exec')  # 编译为字节代码对象
exec(c)

# 53.globals() 函数会以字典类型返回当前位置的全部全局变量。
print globals()

# 54.map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表.Python 3.x 返回迭代器。
print map(lambda x: x ** 2, [1, 2, 3, 4])
print map(lambda x, y: x+y, [1, 3, 5, 7], [2, 4, 6, 8])

# 55.reversed 函数返回一个反转的迭代器。
print list(reversed([1, 3, 5]))

# 56.__import__() 函数用于动态加载类和函数。如果一个模块经常变化就可以使用 __import__() 来动态载入。

# 57.complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。

# 58.hasattr() 函数用于判断对象是否包含对应的属性。

# 59.max() 方法返回给定参数的最大值，参数可以为序列。
print max([1, 9, 0, 2, 7])

# 60.round() 方法返回浮点数x的四舍五入值。round( x [, n])
print round(1.2242, 3)

# 61.delattr 函数用于删除属性。delattr(x, 'foobar') 相等于 del x.foobar。


# 62.hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
# hash() 函数可以应用于数字、字符串和对象，不能直接应用于 list、set、dictionary。
# 在 hash() 对对象使用时，所得的结果不仅和对象的内容有关，还和对象的 id()，也就是内存地址有关。
class Test:
    def __init__(self, i):
        self.i = i
for i in range(2):
    t = Test(1)
    print(hash(t), id(t))

# 63.memoryview() 函数返回给定参数的内存查看对象(Momory view)。
# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问
v = memoryview('abcefg')
print v[1]

# 64.set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
x = set('runoob')
y = set('google')
print x, y
print x & y  # 交集
print x | y  # 并集
print x - y  # 差集