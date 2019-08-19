# coding:utf-8
from itertools import chain, combinations, count, cycle, dropwhile, groupby, ifilter, ifilterfalse, imap

# itertools模块包含创建有效迭代器的函数，可以用各种方式对数据进行循环操作，此模块中的所有函数返回的迭代器都可以与for循环语句
# 以及其他包含迭代器（如生成器和生成器表达式）的函数联合使用。


# 1.chain(iter1, iter2, ..., iterN)：
# 给出一组迭代器(iter1, iter2, ..., iterN)，此函数创建一个新迭代器来将所有的迭代器链接起来，
# 返回的迭代器从iter1开始生成项，直到iter1被用完，然后从iter2生成项，这一过程会持续到iterN中所有的项都被用完。
test = chain('AB', 'CDE', 'F')
print test  # <itertools.chain object at 0x0000000002BBEA20>
print list(test)
for item in test:
    print item


# 2.chain.from_iterable(iterables):
# 一个备用链构造函数，其中的iterables是一个迭代变量，生成迭代序列，此操作的结果与以下生成器代码片段生成的结果相同：
def f(iterables):
    for y in iterables:
        yield y


test = f('ABCDEF')
print test.next()

test = chain.from_iterable('ABCDEF')
print test.next()

# combinations(iterable, r):
# 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序:
test = combinations([1, 2, 3, 4], 2)
print test  # <itertools.combinations object at 0x000000000336A228>
print list(test)  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
for e in test:
    print e

# count([n]):
# 创建一个迭代器，生成从n开始的连续整数，如果忽略n，则从0开始计算（注意：此迭代器不支持长整数），
# 如果超出了sys.maxint，计数器将溢出并继续从-sys.maxint-1开始计算。
count1 = count()
print count1.next()
print count1.next()
count2 = count(100)
print count2.next()

# cycle(iterable):
# 创建一个迭代器，对iterable中的元素反复执行循环操作，内部会生成iterable中的元素的一个副本，此副本用于返回循环中的重复项。
cycle1 = cycle([1, 2, 3])
for i in range(10):
    print cycle1.next()


# dropwhile(predicate, iterable):
# 创建一个迭代器，只要函数predicate(item)为True，就丢弃iterable中的项，如果predicate返回False，就会生成iterable中的项和所有后续项。
def predicate(x):
    return x > 10


dropwhile1 = dropwhile(predicate, [12, 11, 9, 20])
print list(dropwhile1)  # [9 ,20]

# groupby(iterable [,key]):
# 创建一个迭代器，对iterable生成的连续项进行分组，在分组过程中会查找重复项。
# 如果iterable在多次连续迭代中生成了同一项，则会定义一个组，如果将此函数应用一个分类列表，那么分组将定义该列表中的所有唯一项，
# key（如果已提供）是一个函数，应用于每一项，如果此函数存在返回值，该值将用于后续项而不是该项本身进行比较，
# 此函数返回的迭代器生成元素(key, group)，其中key是分组的键值，group是迭代器，生成组成该组的所有项。
from operator import itemgetter  # itemgetter用来去dict中的key，省去了使用lambda函数

d1 = {'name': 'zhangsan', 'age': 20, 'country': 'China'}
d2 = {'name': 'wangwu', 'age': 19, 'country': 'USA'}
d3 = {'name': 'lisi', 'age': 22, 'country': 'JP'}
d4 = {'name': 'zhaoliu', 'age': 22, 'country': 'USA'}
d5 = {'name': 'pengqi', 'age': 22, 'country': 'USA'}
d6 = {'name': 'lijiu', 'age': 22, 'country': 'China'}
lst = [d1, d2, d3, d4, d5, d6]
# 通过country进行分组：
# lst.sort(key=itemgetter('country'))  # 需要先排序，然后才能groupby。lst排序后自身被改变
# lstg = groupby(lst, itemgetter('country'))
lstg = groupby(lst, key=lambda x: x['country'])  # 等同于使用itemgetter()
for key, group in lstg:
    # print key, list(group)
    for g in group:  # group是一个迭代器，包含了所有的分组列表
        print key, g

# ifilter(predicate, iterable):
# 创建一个迭代器，仅生成iterable中predicate(item)为True的项，如果predicate为None，将返回iterable中所有计算为True的项。
for i in ifilter(lambda x: x % 2, range(10)):
    print i

# ifilterfalse(predicate, iterable):
# 创建一个迭代器，仅生成iterable中predicate(item)为False的项，如果predicate为None，则返回iterable中所有计算为False的项。
for i in ifilterfalse(lambda x: x % 2, range(10)):
    print i


# imap(function, iter1, iter2, iter3, ..., iterN)
# 创建一个迭代器，生成项function(i1, i2, ..., iN)，其中i1，i2...iN分别来自迭代器iter1，iter2 ... iterN，
# 如果function为None，则返回(i1, i2, ..., iN)形式的元组，只要提供的一个迭代器不再生成值，迭代就会停止。
d = imap(pow, (2, 3, 10), (5, 2, 3))
for i in d:
    print i
d = imap(None, (2,3,10), (5,2))
for i in d:
    print i


# islice(iterable, [start, ] stop [, step]):
# 创建一个迭代器，生成项的方式类似于切片返回值： iterable[start : stop : step]，将跳过前start个项，
# 迭代在stop所指定的位置停止，step指定用于跳过项的步幅。与切片不同，负值不会用于任何start，stop和step，
# 如果省略了start，迭代将从0开始，如果省略了step，步幅将采用1.
