#L = [1,2,3,4,5]
#a,v = L

'''
问题:
如果可迭代对象的元素个数大于变量个数，会抛出一个ValueError: too many values to unpack (expected 2)
如何从这个可迭代对象中解压N个元素出来？
'''

'''
解决:python中的星号表达式可以用来解决这个问题
解压不确定个数或任意个数元素的可迭代对象
'''
# 除去第一个和最后一个求平均
def drop_first_last(grades):
    first,*middle,last = grades
    return sum(middle)/len(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name,email,*phonenumbers = record # phonenumbers变量永远是列表类型  不管解压数量是多少
print(phonenumbers)


# 也可以放在开头部分
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)



# 切分字符串
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

# 解压元素并丢弃  丢弃名称用_或ign
record = ('ACME', 50, 123.45, (12, 18, 2012))
name,*_,(*_,year) = record

