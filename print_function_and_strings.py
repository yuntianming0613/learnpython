print('This is an example of print function')
print('中文测试')
print("We're going to the store")
print('We\'re going to the store')
print('He said "Hi."')
print('Hi '+'there')
print('Hi '+'5')
print('Hi '+str(8))
print(int('8')+5)
print('Hi', 'hello')
print('100 + 200 =', 100 + 200)
name = input()
print('hello', name)
name = input('Please enter your name: ')
print('hello', name)
print('\\\n\\')
print('''
line1
    line2
line3
            line4
''')
age = int(input('please enter you age: '))
if age >= 18:
    print('adult')
else:
    print('teenager')

print('''
n = 123
f = 456.789
s1 = \'Hello, world\'
s2 = \'Hello, \\\'Adam\\\'\'
s3 = r\'Hello, "Bart"\'
s4 = r\'\'\'Hello,
Lisa!\'\'\'
''')