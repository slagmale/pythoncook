# problem: 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？


'''
保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码
在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行：
'''
from collections import deque


def search(lines, pattern, history=5):
    # 新建固定大小的队列，当新的元素加入并队列已满，最老的元素被自动移除。
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines  # 带yield的函数是生成器，在程序中返回值，之后程序不往下运行
        previous_lines.append(line)



'''
写查询元素的代码时，通常使用包含yield表达式的生成器函数
将搜索过程和使用搜索结果代码解耦
'''

#  队列案例
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # 输出deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)  # 输出deque([2, 3, 4], maxlen=3)
# 如果不设定队列大小  得到无限大小的队列，可以在队列两端执行添加和弹出元素的操作
q2 = deque()
q2.append(5)
q2.append(6)
q2.append(7)
print(q2)
q2.appendleft(4)  # 在最左边添加一个元素
print(q2)
q2.pop()  # 删除最后一个元素
print(q2)
q2.popleft()  # 在最左边删除一个元素
print(q2)

# 在队列两端插入或删除元素复杂度为O(1)   而在列表开头插入或删除元素复杂度为O(n)


# yiled生成式函数案例
def foo(num):
    print("starting...")
    while num < 10:
        num = num + 1
        res = yield num
        print('res:', res)


a = foo(0)
# 第一种
print(a.__next__())  # yield 返回num=1  这时函数停止运行  并没有给res赋值
print(a.__next__())  # 输出res=None 接着while循环返回num=2

# 第二种
print(a.__next__())
print(a.send(5))  # 将值5赋值给了res 然后执行next 输出res=5后接着while循环 返回num
