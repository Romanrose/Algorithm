#列表
[]

classmates = ['Michael', 1, 'Curry']
print(classmates)

# print(len(classmates)) #3



# for i in range(0, 3):
#     print(classmates[i])

# for i in range(-3, 0):
#     print(classmates[i])

# 追加元素到末尾
# classmates.append("Adam")

# print(classmates)

# classmates.insert(0, 'jack')

# print(classmates)

# classmates.pop()

# print(classmates.pop())

print(classmates.pop(1))

p = ['w', 'q', 'e']
q = ['z', 'x', 'c', p]
print(q)


# touple

qw = (1,2)
print(qw)
len(qw)

#只有1个元素的tuple定义时必须加一个逗号,
a = (1,)
print(a)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

print(L[0][0])  # Apple
print(L[1][1])  # Python    

#dict

names = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(names['Michael'])  # 95
names['Bob'] = 80
print(names['Bob'])  # 80

print('Tomas' in names)  # False
print(names)
names.pop('Bob')  # 删除'Bob'键
print(names)  # {'Michael': 95, 'Tracy': 85}


#set

s = {1,7,3}
print(s)  # {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}
s.remove(3)
print(s)  # {1, 2, 4}

#string
str1 = 'Hello, world!'
str1.replace('world', 'Python')
print(str1)  # Hello, world! (原字符串未改变)
str2 = str1.replace('world', 'Python')
print(str2)  # Hello, Python!