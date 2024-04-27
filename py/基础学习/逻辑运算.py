"""
and   or    not
与    或    非


      and

  x > 5 and  x<10
    可以理解为并且： X 大于5并且小于10
    x > 5 and x < 10 and x * 2 == 12
    只有所有结果为 Ture  才会返回 Ture 真
    只要一个结果为False  最后都会返回 False  假

      or
    x >5 or x<10
    可以理解为 或者  X 大于5或者小于10
只要一个结果为Ture  最后都会返回  Tere
只有所有结果为 False  才会返回 False

    not
    不   not  x > 5   x不大于5
    只能对一个对象进行计算 返回相反布尔值

    运算顺序  not 《 and 《 or
"""