# -*- coding: utf-8 -*-


names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

Sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    Sum += x
print(Sum)


print(list(range(5)))


Sum = 0
for x in range(101):
    Sum += x
print(Sum)

Sum = 0
n = 99
while n > 0:
    Sum += n
    n -= 2
print(Sum)


# 练习
#
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
#
# # -*- coding: utf-8 -*-
# L = ['Bart', 'Lisa', 'Adam']


L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('Hello,%s!' % i)

n = 0
while n < 3:
    print(n)
    print('Hello,', L[n], '!')
    n += 1


n = 0
while n < len(L):
    print('Hello,,', L[n], '!')
    n += 1
