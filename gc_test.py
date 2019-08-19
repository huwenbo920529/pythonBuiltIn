# coding:utf-8
import gc
import sys


class CGcLeak(object):
    def __init__(self):
        self._text = '#' * 10

    def __del__(self):
        pass


def make_circle_ref1():
    _gcleak = CGcLeak()
    print "_gcleak ref count0:{}".format(sys.getrefcount(_gcleak))
    del _gcleak
    try:
        print "_gcleak ref coun1:{}".format(sys.getrefcount(_gcleak))
    except UnboundLocalError:
        print "_gcleak is invalid!"


def make_circle_ref2():
    _gcleak = CGcLeak()
    _gcleak._self = _gcleak  # 自己循环引用自己
    print "_gcleak ref count0:{}".format(sys.getrefcount(_gcleak))
    del _gcleak
    try:
        print "_gcleak ref coun1:{}".format(sys.getrefcount(_gcleak))
    except UnboundLocalError:
        print "_gcleak is invalid!"


def test_gcleak1():
    gc.enable()  # 设置垃圾回收器调试标志
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
    print "begin leak test..."
    make_circle_ref1()

    print "begin collect..."
    _unreachable = gc.collect()
    print "unreachable object num:{}".format(_unreachable)
    print "garbage object num:{}".format(len(gc.garbage))
    # gc.garbage是一个list对象，
    # 列表项是垃圾收集器的不可达（即垃圾对象）、但又不能释放（不可回收）的对象，通常gc.garbage中的对象是引用对象还是中的对象。
    # 因Python不知用什么顺序来调用对象的__del__函数导致对象始终存活在gc.garbage中，
    # 造成内存泄漏if __name__ == "__main__": test_gcleak()。如果知道一个安全次序，那么就可以打破引用焕，
    # 再执行del gc.garbage[:]从而清空垃圾对象列表


def test_gcleak2():
    gc.enable()  # 设置垃圾回收器调试标志
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
    print "begin leak test..."
    make_circle_ref2()

    print "begin collect..."
    _unreachable = gc.collect()
    print "unreachable object num:{}".format(_unreachable)
    print "garbage object num:{}".format(len(gc.garbage))


# 多个对象间的循环引用造成内存泄露
class CGcLeakA(object):
    def __init__(self):
        self._text = "$" * 10

    def __del__(self):
        pass


class CGcLeakB(object):
    def __init__(self):
        self._text = '&' * 10

    def __del__(self):
        pass


def make_circle_ref3():
    _a = CGcLeakA()
    _b = CGcLeakB()
    _a.s = _b
    _b.d = _a
    print "ref count0:a={},b={}".format(sys.getrefcount(_a), sys.getrefcount(_b))
    del _a
    del _b
    try:
        print "ref count1:a:{}".format(sys.getrefcount(_a))
    except UnboundLocalError:
        print "_a is in valid!"


def test_gcleak3():
    gc.enable()  # 设置垃圾回收器调试标志
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
    print "begin leak test..."
    make_circle_ref3()

    print "begin collect..."
    _unreachable = gc.collect()
    print "unreachable object num:{}".format(_unreachable)
    print "garbage object num:{}".format(len(gc.garbage))


if __name__ == '__main__':
    # test_gcleak1()
    # test_gcleak2()
    test_gcleak3()