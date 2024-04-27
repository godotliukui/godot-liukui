"""
str  字符串   holle  嗨

len（） 函数 求字符串长度
int  整数    123  -123
float  浮点数   123.113   0.123  2.0
bool  布尔类型   True  False
noneType 空值类型   None

 列表 字典 。。。。。。。。。。。
"""
# 字符 空格 符号 都占一个长度  完整的转义符也算一个长度
a = "holle worde!"
print(len(a))

#提取字符 索引 字符 "holle"[4]  实际是第四位字符e  因为 是从0 开始数的
print(a[4])

#布尔值
a1 = True
b2 = False

#空值类型
n = None
#不确定值 用none

# 不确定数据类型 用 type函数

print(type(a))
print(type(a1))
print(type(n))
print(type(1.5))

