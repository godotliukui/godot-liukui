"""
空字典用{}花括号表示  变量名 = {}
contacts = {"小米”：“12312313”
            "大米“：”123123123"

            }
花括号里面数据是成对的用引号表示对应： 键（key）：值（value）   键值对之间用逗号分隔

获取某个键的值
contacts["小米"] 里面放入键
键的类型不可变 list 列表是可变类型的 不能作为键
example_list = ["键盘", "键帽"]

------------
列表用方括号  元组用圆括号
------------------
元组
元组不可变 所以 不能 删除 或添加
example_tuple = ("键盘", "键帽")

contacts = {("小米", 10): "12312313123",
            ("小米", 12): "34635345345",
            ("小米", 19): "676756756745"}

xiaomi_unm = contacts[("小米“,10)]
把整个元组作为键

字典是可变的 所以可以删除和添加 键值对
添加键值对
contacts["大米"] = "1236989768"

删除键值对
del contacts["大米"]

查询存在多少键值对
len(contacts)

查询键是否存
"大米" in contacts  #返回bool值 告诉你 是否存在

------------------
字典的三个方法
zidian.keys（）  #返回所有键
zidian.values（）  #返回所有值
zidian.items （）   #返回所有键值对

"""

#创建字典

zidian = {"liumeil":"20160913",
          "zhouqian":"19910419"}

#字典添加 键对值
zidian["liukui"] = "19910910"

bianiang = input("输入名字")

if bianiang in zidian:
    print("你要查询的" + bianiang + "日期如下")
    print(zidian[bianiang])
else:
    print("还没来得及做好")
    print("总共只有" + str(len(zidian)) + "个")