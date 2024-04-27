#交互式输入
#BIM = 体重/（身高 ** 2）
#folat 定义输入数据类型


user_weight = float(input("输入体重（单位是：kg）"))
user_height = float(input("输入身高（单位是：m"))
user_BIM = user_weight / (user_height ) ** 2
print("你的BIM值为：" + str(user_BIM))

print(type(user_weight))