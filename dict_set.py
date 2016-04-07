# -*- coding: utf-8 -*-
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d)

a = 'Thomas' in d   # 判断字典中有无此key
print(a)

d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

print(d)

d.pop('Bob')
print(d)

# -----------------------------------------------------------------------
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)

s = set([1, 1, 2, 2, 3, 3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)


