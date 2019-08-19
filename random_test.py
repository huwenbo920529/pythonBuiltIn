# coding:utf-8
import random

# random.random()用于生成一个0到1的随机浮点数: 0 <= n < 1.0
print random.random()

# random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
# 如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a
print random.uniform(10, 20)

# random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
# 下限必须小于上限
print random.randint(10, 20)

# random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。
# 如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
# random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效
print random.randrange(10, 20, 2)

# random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
# 这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
print random.choice(range(10, 20, 2))

# random.shuffle(x[, random])，用于将一个列表中的元素打乱。
p = ["Pthon", "is", "powerful", "simple", "and so on"]
random.shuffle(p)
print p

# random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
print random.sample(p, 3)
print p