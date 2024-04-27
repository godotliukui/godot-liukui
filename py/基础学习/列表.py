"""
item1 = "键盘"
itme2 = "键帽“
itme3 =  "显示器“
itme4 = "音响“
itme5 = "手表“
itme6 = "电竞椅"
itme7 = "kindle"
itme8 = "相机“
itme9 = "平板"
itme10 = "硬盘"
这样 定义很不方便且繁琐
"""
# 列表的使用方法
# 空的列表用方括号表示  变量名 = []
#把要放入的数据填入方括号内， 用 逗号 分开

shopping_list = ["键盘", "键帽"]

#想继续加入列表 就用方法 append（） 加入

shopping_list.append("音响") #append添加元素
shopping_list.append("显示器")
shopping_list.remove("键盘")  #remove删除元素
shopping_list[1] = "硬盘"  #更换列表内第二个元素，从0开始计数

print(shopping_list)    #打印列表
print(len(shopping_list)) #查看中共有几个元素
print(shopping_list[1]) # 用索引列表打印需要位置的元素

num = [1, 13, -7, 11, 20]

min_num = min(num)
sorted_num = sorted(num)

print(max(num)) #  直接---打印列表最大值
print(min_num)  # 赋值-----打印列表最小值
print(sorted_num)  # 打印排序好的列表 从小到大

#  据说从大到小 num.sort(reverse=True)   列表名.sort(reverse=True)

"""
方法：
对象.方法名.(....)
shopping_list.append("显示器")

函数：

函数名（对象）

len（shoping_list）

列表是 可变的  ： list 。。。
即 里面的内容是可变的

王列表里面添加元素 列表就会发生变化， 不需要对 shopping_list 重新赋值
shopping_list.append("显示器")  正确添加方法
shopping_list = shopping_lise.append("显示器“）  是错误的
------------------------------
列表删除方法

shopping_list = ["键盘", "键帽"]

shopping_list.remove("键盘")  就会在愿列表上生效  也不需要从新赋值，但是该元素必须存在于列表
不确定可以随时打印列表
print("shopping_list")

列表可以放不同类型的数据， 还可以用len（） 求长度 会返回列表元素的数量
print("shopping_list[]) 方括号内填数字  索引
索引并赋值
 shopping_list[1] = "电竞椅"   会覆盖原本位置的元素
 
 
num = [1, 13, -7, 11, 20]
max_num = max(num)
min_num = min(num)
sorted_num = sorted(num)

print(max_num) # 打印列表最大值
print(min_num)  # 打印列表最小值
print(sorted_num)  # 打印排序好的列表
 ---------------——————————————————————————————-

不可变的 ： 字符串str  整数 int   浮点数 float  布尔类型 boll 。。。。。

例如: # supper（）是将 hello 转换为大写字母，但是 S的值并不会改变
s = "hello"
print（s.upper()）
# s = s.supper()    要把新的字符串赋值给变量s  这样才会把s全部别为大写
print(s)

"""



