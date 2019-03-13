# question: 怎样从一个集合中获得最大或最小的N个元素列表？

'''
heapq模块中的两个函数：nlargest()  nsmallest() 完美解决这个问题
'''

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # 得到最大的三个数
print(heapq.nsmallest(3, nums))  # 得到最小的三个数


'''
当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很
合适的。如果你仅仅想查找唯一的最小或最大（N=1）的元素的话，那么使用 min() 和
max() 函数会更快些。类似的，如果 N 的大小和集合大小接近的时候，通常先排序这个
集合然后再使用切片操作会更快点（sorted(items)[:N] 或者是 sorted(items)[-N:]
）。需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势（如果
N 快接近集合大小了，那么使用排序操作会更好些）。
'''

# 两个函数都能够接受一个参数   根据参数来进行选择元素
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 这里根据price的值来比较
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


