# coding:utf-8
from collections import namedtuple, deque, Counter, OrderedDict, defaultdict


# namedtuple()
# namedtuple主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。
websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]
Website = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
    website = Website._make(website)
    print website
    print website.name


# deque
# deque其实是 double-ended queue 的缩写，翻译过来就是双端队列，
# 它最大的好处就是实现了从队列 头部快速增加和取出对象: .popleft(), .appendleft()
fancy_loading = deque('>--------------')
n = 1
while n < 16:
    print '{}'.format(''.join(fancy_loading))
    fancy_loading.rotate(1)
    n = n + 1

d1 = deque()
d1.appendleft('first')
d1.appendleft('second')
d1.appendleft('third')
d1.append('four')
print d1
d1.pop()
print d1
d1.popleft()
print d1

d = deque(xrange(10))
print 'Normal:', d
d = deque(xrange(10))
d.rotate(2)
print 'Right roration:', d
d = deque(xrange(10))
d.rotate(-2)
print 'Left roration:', d


# Counter计数器是一个非常常用的功能需求
s = '''A Counter is a dict subclass for counting hashable objects.
It is an unordered collection where elements are stored as dictionary keys
and their counts are stored as dictionary values.
Counts are allowed to be any integer value including zero or negative counts.
The Counter class is similar to bags or multisets in other languages.'''.lower()
c = Counter(s)
print c
print c.most_common(5)  # 获取出现频率最高的5个字符


# OrderedDict
# 在Python中，dict这个数据结构由于hash的特性，是无序的，这在有的时候会给我们带来一些麻烦，
# 幸运的是，collections模块为我们提供了OrderedDict
items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)
regular_dict = dict(items)
ordered_dict = OrderedDict(items)
print 'Regular dict:'
for k, v in regular_dict.items():
    print k, v
print 'Ordered dict:'
for k, v in ordered_dict.items():
    print k, v


# defaultdict
# 我们都知道，在使用Python原生的数据结构dict的时候，如果用 d[key] 这样的方式访问，
    # 当指定的key不存在时，是会抛出KeyError异常的。
# 但是，如果使用defaultdict，只要你传入一个默认的工厂方法，那么请求一个不存在的key时，
    # 便会调用这个工厂方法使用其结果来作为这个key的默认值。
members = [
    # gender, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]
result = defaultdict(list)
for gender, name in members:
    result[gender].append(name)
print result
for k, v in result.items():
    print k, v


# collections中ChainMap的使用
# ChainMap可以合并多个dict，而且效率很高