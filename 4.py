def hu():
    return "Hello, World!"

print(hu())

def nop():
    pass

import math

def move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx, ny

print(move(100, 100, 60, math.pi/6))  # (130.0, 70.0)

def power(x):
    return x * x
print(power(5))  # 25

def enroll(name,age):
    print(f'Name: {name}, Age: {age}')
enroll('Bob', 20)  # Name: Bob, Age: 20

def calc(numbers):
    sum = 0
    for i in numbers:
        sum += i * i
    return sum
print(calc([1, 2, 3]))  # 14

def person(name, age, **kw):
    print(f'Name: {name}, Age: {age}, Other: {kw}')
person('Michael', 30, city='Beijing', job='Engineer')  # Name: Michael, Age: 30, Other: {'city': 'Beijing', 'job': 'Engineer'}
print(person('Bob', 25))  # Name: Bob, Age: 25, Other: {}

list(range(1, 11))
print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[x * x for x in range(1, 11)]

print([x for x in range(1, 11) if x % 2 == 0])