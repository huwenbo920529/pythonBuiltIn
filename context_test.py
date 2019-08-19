# coding:utf-8
import random
from contextlib import contextmanager
from random import random

import math


class echo(object):
    def __enter__(self):
        print 'enter'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'exit'


with echo() as e:
    print 'this is a test!'


# contextlib是个比with优美的东西，也是提供上下文机制的模块，它是通过Generator装饰器实现的，
# 不再是采用__enter__和__exit__。contextlib中的contextmanager作为装饰器来提供一种针对函数级别的上下文管理机制。
@contextmanager
def make_contest():
    print 'enter'
    try:
        yield {}
    except RuntimeError, err:
        print 'error', err
    finally:
        print 'exit'


with make_contest() as value:
    print value

DEFAULT_EXPIRES = 15
DEFAULT_RETRIES = 5


@contextmanager
def dis_lock(key, client):
    key = 'lock_{}'.format(key)

    def _acquire_lock(key, client):
        for i in xrange(0, DEFAULT_RETRIES):
            get_socored = client.get(key)
            sleep_time = (((i + 1) * random()) + 2 ** i) / 2.5
            print 'sleeping for {}'.format(sleep_time)
        else:
            stored = client.set(key, 1)
            client.expire(key, DEFAULT_EXPIRES)
            return
        raise Exception('Could not acquire lock for {}'.format(key))

    def _release_lock(key, client):
        client.delete(key)

    try:
        _acquire_lock(key, client)
        yield
    finally:
        _release_lock(key, client)


class Solver(object):
    def foo(self):
        pass

a = 1
Solver().foo()


print math.sqrt(4)

