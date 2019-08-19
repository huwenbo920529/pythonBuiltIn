# coding:utf-8
import pickle
import StringIO


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print self.name + "-" + str(self.age)
a = Person("Jhon", 20)
a.show()
f = open('pick_test.txt', 'w')
pickle.dump(a, f, 0)
f.close()

f = open('pick_test.txt', 'r')
b = pickle.load(f)
f.close()
b.show()


# clear_memo()
# 清空pickler的“备忘”。使用Pickler实例在序列化对象的时候，它会“记住”已经被序列化的对象引用，
# 所以对同一对象多次调用dump(obj)，pickler不会“傻傻”的去多次序列化。
aa = Person('hu', 25)
aa.show()
fle = StringIO.StringIO()
# pick
pick = pickle.Pickler(fle)
pick.dump(aa)
val1 = fle.getvalue()
# print val1
# print len(val1)
pick.clear_memo()
pick.dump(aa)
val2 = fle.getvalue()
# print len(val2)
fle.close()
bb = pickle.loads(val1)
bb.show()
