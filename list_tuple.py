classmates = ['Machael', 'Bob', 'Tracy']
print(classmates)
len1 = len(classmates)
print(len1)
a1 = classmates[0]
a2 = classmates[2]
a3 = classmates[-1]
a4 = classmates[-3]
print(a1)
print(a2)
print(a3)
print(a4)

classmates.append('Adam')   # 往list中追加元素到末尾
print(classmates)

classmates.insert(1, 'Jack')    # 把元素插入到指定的位置
print(classmates)

classmates.pop()    # 删除list末尾的元素
print(classmates)

classmates.pop(1)  # 删除指定位置的元素
print(classmates)

classmates[1] = 'Sarah'     # 把某个元素替换成别的元素
print(classmates)

L = ['Apple', 123, True]    # 可以有不同类型的数据类型
print(L)

S = ['python', 'java', ['asp', 'php'], 'scheme']    # list 套 list
print(len(S))

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(p[1])
print(s[2][1])

# ----------------------------------------------------------------------------------
#  tuple    tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(classmates[1])

#   tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)

t = ()
print(t)

t = (1,)
print(t)

#   “可变的”tuple

t = ('a', 'b', ['A', 'B'])
print(t)
print(t[2][0])
print(t[2][1])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t[2][0])
print(t[2][1])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])








