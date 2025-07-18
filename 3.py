#循环结构

# for...in循环，依次把list或tuple中的每个元素迭代出来

names = ['Michael', 'Bob', 'Tracy']
for i in names:
    print(i)

num = 0
for x in [1, 2, 3]:
    num += x
print(num)  # 6

sum = 0
for x in range(101):
    sum += x
print(sum)  # 5050

a = 0
n = 100

while n > 0:
    a += n
    n -= 2
print(a)  # 2550

L = ['Bart', 'Lisa', 'Adam']
for i in range(len(L)):
    print('HHELLO ',L[i])  # Bart Lisa Adam

