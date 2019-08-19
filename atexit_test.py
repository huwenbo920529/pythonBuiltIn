# coding:utf-8
import atexit

# 从模块的名字也可以看出来，atexit模块主要的作用就是在程序即将结束之前执行的代码，atexit模块使用register函数用于注册程序退出时的回调函数，然后在回调函数中做一些资源清理的操作
# 注意：
# 1，如果程序是非正常crash，或通过os._exit() 退出，注册的回调函数将不会被调用。
# 2，也可以通过sys.exitfunc来注册回调，但通过它只能注册一个回调，而且还不支持参数。
# 3，建议使用atexit来注册回调函数。

# 不过请特别注意：
# 1，不要在程序中同时使用这两种方式，否则通过atexit注册的回调可能不会被正常调用。
# 通过查阅atexit的源码，原来它内部是通过sys.exitfunc来实现的，它先把注册的回调函数放到一个列表中，当程序退出时，按先进后出的顺序调用注册的回调。如果回调函数在执行过程中抛出了异常，atexit会打印异常的文字信息，并继续执行下一下回调，直到所有的回调都执行完毕，它会重新抛出最后接收到的异常。
# 2，如果使用的python版本是2.6及以后的版本，还可以用装饰器的语法来注册回调函数。
# 3，如果注册顺序是A，B，C，那么最后调用的顺序是相反的，C，B，A

# 该模块主要有如下两个函数
# atexit.register(func, *args, **kargs)
# 注册函数
# atexit.unregister(func)
# 取消注册函数


def atexit_func1():
    print "I'm atexit_func1"


def atexit_func2(name, age):
    print "I'm atexit_func2,{} is {} years old".format(name, age)


print('I am the first output')
atexit.register(atexit_func1)
atexit.register(atexit_func2, 'Katherine', 20)


@atexit.register
def atexit_func3():
    print "I'm atexit_func3"
