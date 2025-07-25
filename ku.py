import sys

with open("out.txt", "w") as f:
    sys.stdout = f
    print("将这一行写入out.txt")

sys.stdout = sys.__stdout__  # 恢复标准输出
print("这行会输出到控制台")
