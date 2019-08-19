# coding:utf-8
from cStringIO import StringIO
import random
import math
import heapq


# heapq 模块提供了堆算法。heapq是一种子节点和父节点排序的树形数据结构。
# 这个模块提供heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]。为了比较不存在的元素被人为是无限大的。heap最小的元素总是[0]
def show_tree(tree, total_width=36, fill=' '):
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width * 1.0) / columns)
        # Python字符串center()方法以字符串宽度(width)为中心。使用指定的填充字符(fillchar)填充完成。默认填充字符(fillchar)是一个空格
        output.write(str(n).center(col_width, fill))
        last_row = row
    print output.getvalue()
    print '-' * total_width
    print
    return

data = random.sample(range(1, 8), 7)
print 'data:', data
show_tree(data)


heap = []
for i in data:
    heapq.heappush(heap, i)
    show_tree(heap)


# 删除并返回堆中最小的元素, 通过heapify() 和heappop()来排序。
heapq.heapify(data)
show_tree(data)
heap = []
while data:
    i = heapq.heappop(data)
    print 'pop %3d' % i
    heap.append(i)
print heap


# 删除现有元素并将其替换为一个新值
data = random.sample(range(1, 8), 7)
print 'data: ', data
heapq.heapify(data)
show_tree(data)
for n in [8, 9, 10]:
    smallest = heapq.heapreplace(data, n)
    print 'replace %2d with %2d:' % (smallest, n)
    show_tree(data)


# heapq.nlargest(n, iterable) 和 heapq.nsmallest(n, iterable)
# 返回列表中的n个最大值和最小值
data = range(1, 6)
print heapq.nlargest(3, data)
print heapq.nsmallest(3, data)

