#选择结构
age = 20
if age < 60:
    print("不及格")
else:
    print("及格")

#input

bir = input("请输入你的生日：")
birth = int(bir)
if birth > 2000:
    print("00后")
elif birth < 2000:
    print("00前")


#模式匹配

score = "A"

match score:
    case "A":
        print("优秀")
    case "B":
        print("良好")
    case "C":
        print("及格")
    case _:
        print("不及格")

age = 2

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')