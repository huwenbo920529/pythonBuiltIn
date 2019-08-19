# coding:utf-8
import traceback
import sys
import cgitb


def func(a, b):
    return a / b


def test1():
    try:
        func(1, 0)
    except Exception as e:
        print "print_exception()"
        exc_type, exc_value, exc_tb = sys.exc_info()
        print 'the exc type is:', exc_type
        print 'the exc value is:', exc_value
        print 'the exc tb is:', exc_tb
        # traceback.print_exception(exc_type, exc_value, exc_tb)
        for filename, linenum, funcname, source in traceback.extract_tb(exc_tb):
            print "{}:{}-->{} in {}()".format(filename, linenum, source, funcname)


def test2():
    cgitb.enable(format('html'))
    func(1, 0)


if __name__ == '__main__':
    # test1()
    test2()
