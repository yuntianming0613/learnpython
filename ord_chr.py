a = ord('A')
print(a)

b = chr(65)
print(b)

# 计算str包含多少个字符,可以用len()函数:

a = len('ABC')
b = len('中文')
print(a)
print(b)
print('格式化')
print('%d\n%d' % (a, b))

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

print('%02d-%02d-%2d' % (3, 1, 3))
print('%.2f' % 4.1415)

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%.1f%%' % r)
