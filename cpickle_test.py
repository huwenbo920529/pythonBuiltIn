# coding:utf-8
import cPickle as pickle

t1 = ('this is a string', 42, [1, 2, 3], None)
p1 = pickle.dumps(t1)
print p1

t2 = pickle.loads(p1)
print t2

p2 = pickle.dumps(t1, True)
print p2

t3 = pickle.loads(p2)
print t3


# 接下来，我们看一些示例，这些示例用到了
# dump()和load() ，它们使用文件和类似文件的对象。这些函数的操作非常类似于我们刚才所看到的
# dumps()和loads() ，区别在于它们还有另一种能力 — dump()
# 函数能一个接着一个地将几个对象转储到同一个文件。随后调用load()
# 来以同样的顺序检索这些对象。
a1 = 'apple'
b1 = {1: 'One', 2: "Two", 3: "Three"}
c1 = ['fee', 'fie', 'foe', 'fum']

f1 = file('temp.pkl', 'wb')
pickle.dump(a1, f1, True)
pickle.dump(b1, f1, True)
pickle.dump(c1, f1, True)
f1.close()

f2 = file('temp.pkl', 'rb')
a2 = pickle.load(f2)
print a2

b2 = pickle.load(f2)
print b2

c2 = pickle.load(f2)
print c2
f2.close()


# 检索所支持的格式
print pickle.format_version
print pickle.compatible_formats


# 多个引用，同一对象
a = [1, 2, 3]
b = a
c = pickle.dumps((a, b))
d, e = pickle.loads(c)
print d
print e
d.append(4)
print d  # [1, 2, 3, 4]
print e  # [1, 2, 3, 4]


# 递归引用
l = [1, 2, 3]
l.append(l)
print l[3]  # [1, 2, 3, [...]]
print l[3][3]  # [1, 2, 3, [...]]
p = pickle.dumps(l)
l2 = pickle.loads(p)
print l2
print l2[3]
print l2[3][3]


# 循环引用
a = [1, 2]
b = [3, 4]
a.append(b)
b.append(a)
print a  # [1, 2, [3, 4, [...]]]
print b  # [3, 4, [1, 2, [...]]]
print a[2]  # [3, 4, [1, 2, [...]]]
print b[2]  # [1, 2, [3, 4, [...]]]
print a[2] is b  # True
print b[2] is a  # True

f = file('temp.pkl', 'w')
pickle.dump((a, b), f)
f.close()
f = file('temp.pkl', 'r')
c, d = pickle.load(f)
f.close()
print c
print d
print c[2] is d
print d[2] is c

# 注意，如果分别 pickle 每个对象，而不是在一个元组中一起 pickle 所有对象，会得到略微不同（但很重要）的结果
f = file('temp.pkl', 'w')
pickle.dump(a, f)
pickle.dump(b, f)
f.close()
f = file('temp.pkl', 'r')
c = pickle.load(f)
d = pickle.load(f)
f.close()
print c
print d
print c[2] is d  # False
print d[2] is c  # False


# 类实例
# 与 pickle 简单对象类型相比，pickle 类实例要多加留意。这主要由于 Python 会 pickle 实例数据（通常是 _dict_ 属性）和类的名称，
# 而不会 pickle 类的代码。当 Python unpickle 类的实例时，它会试图使用在 pickle 该实例时的确切的类名称和模块名称（包括任何包的路径前缀）导入包含该类定义的模块。
# 另外要注意，类定义必须出现在模块的最顶层，这意味着它们不能是嵌套的类（在其它类或函数中定义的类）。
# 当 unpickle 类的实例时，通常不会再调用它们的 _init_() 方法。相反，Python 创建一个通用类实例，
# 并应用已进行过 pickle 的实例属性，同时设置该实例的 _class_ 属性，使其指向原来的类。
# 对 Python 2.2 中引入的新型类进行 unpickle 的机制与原来的略有不同。虽然处理的结果实际上与对旧型类处理的结果相同，
# 但 Python 使用 copy_reg 模块的 _reconstructor() 函数来恢复新型类的实例。
# 如果希望对新型或旧型类的实例修改缺省的 pickle 行为，则可以定义特殊的类的方法 _getstate_() 和 _setstate_() ，
# 在保存和恢复类实例的状态信息期间，Python 会调用这些方法。在以下几节中，我们会看到一些示例利用了这些特殊的方法。
from t2 import Foo
foo = Foo("What is a Foo?")
f = file('temp.pkl', 'w')
pickle.dump(foo, f)
f.close()
f = file('temp.pkl', 'r')
foo2 = pickle.load(f)
f.close()
print foo2.value


from t2 import Foo2

