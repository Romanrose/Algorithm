#generate

g = (x * x for x in range(1, 11))
print(g)  # <generator object <genexpr> at ...>
print(next(g))  # 1
print(next(g))  # 4

for i in g:
    print(i)  # 9, 16, 25, 36, 49, 64, 81, 100