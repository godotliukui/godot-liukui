"""
for 变量名 in 可迭代对象 ：
 #对每个变量做一些事情

"""
#实例
tiwen_list = [35.3, 35.6, 35.7, 38.1, 39, 36.2]

for tiwen in tiwen_list:
    if tiwen >= 38:
        print(tiwen)
        print("隔离")
tiwen_zidian = {"1":35.3, "2":35.5, "3":37, "4":38.5, "5":36, "6":39}

#这里有 tiwen_id 和 tiwen1 两个变量 对应字典里的 键：值对
for tiwen_id,tiwen1 in tiwen_zidian.items():
    if tiwen1 >= 38:
        print(tiwen_id)



"""
range （5, 10， 2） 表示 整数数列。 第一个值表示起始值，第二个 表示结束值。 结束值 不在序列范围
 第三个数表示 步长  也就是每次跨几个数字，不指名 默认为1
for i in range(5, 10):
 print(i)
 
会打印5-9 但不会打印10
"""

tatal = 0
for i in range(1, 101):
    tatal = tatal + i
    print(tatal)