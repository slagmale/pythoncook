# problem: 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？


'''
保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码
在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行：
'''
from collections import deque






# yiled生成式函数
def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)


