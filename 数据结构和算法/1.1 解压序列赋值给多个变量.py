# problem: 现在有一个包含N个元素的元组或者序列，怎么样将里面的值解压同时赋给N个变量？

'''
解决方案： 任何的序列（可迭代对象）可以通过一个简单的赋值语句解压赋值给多个变量
前提：变量的数量必须和序列元素数量一致
'''

p = ('whc', 22)
name, age = p
print('姓名:', name, '年龄:', age)

list = ['abc', 15, 16.1, (2019, 3, 12)]
n, shares, price, date = list
print(n, shares, price, date)
n, shares, price, (year, month, day) = list
print(n, shares, price, year, month, day)

'''
这种解压赋值可以用在任何可迭代对象上，不仅列表和元组
包括字符串，文件对象，迭代器和生成器
'''

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

'''
如果只想要解压一部分，丢弃其他值。可以使用任意变量去占位，到时丢掉这些变量即可。
注意：必须保证选用的占位变量在其他地方没有被使用
'''
data = ['gogo',1314,(2019,3,12)]
_,_,now = data
print(now)