# -*- coding: utf-8 -*-


age = 20
if age >= 18:
    print('your age is ', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is ', age)
    print('adult')
else:
    print('your age is ', age)
    print('teenager')

age = 4
if age >=18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')


# 练习
#
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：


height = 1.75
weight = 80.5

bmi = weight/height**2
print(bmi)
if bmi > 32:
    print('严重肥胖')
elif 32 >= bmi > 28:
    print('肥胖')
elif 28 >= bmi > 25:
    print('过重')
elif 25 >= bmi > 18.5:
    print('正常')
else:
    print('过轻')
