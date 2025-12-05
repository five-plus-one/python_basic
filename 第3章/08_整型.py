import sys

age = 18
temp = -15
score = 0

# 当数很大时，可以用下划线进行分组
salary = 300_000
house_price = 3_200_000
graduates = 12_000_000
print(salary, house_price, graduates)

# Python中整数的上限值，取决于执行代码的计算机的内存和处理能力
a = 9 ** 999
# print(a)
b = a + 100
sys.set_int_max_str_digits(0)  # 解除数字转字符串长度限制
print(a)
