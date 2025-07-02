#尚硅谷python

#变量
# price = 10.5
# weight = 7.5
# money = price * price
# print(f"总共消费{money}元")
# print("总共消费%.2f元"%money)#小数点后保留2位

# year = 2023#python是一行一行解释的所以会出现两个结果
# print(year)
# year = 2024
# print(year)

# money = 10#python里可以进行变量类型修改
# money = '十元'
# print(money)


# price = 10.5
# weight = 7.5
# money = price * price
# money = money - 5
# print("总共消费%.2f元"%money)

#索引
# str = 'Hello World'
#切片 str[起始索引:结束索引+1:步长]
#步长默认为1可省略，起始索引默认为0可省略，结束默认为-1可省略
# print(str[0])
# print(str[0:4])#包头不包尾：前面的位置，后面的位置前一个
# print(str[-1])

# num = '123456789'
#实现逆置,从末尾-1开始数到1的索引为-10（包头不包尾），倒着数步长为负的
# print(num[-1:-10:-1])
# print(num[::-1])#省略版


#看id号
# a = 3
# print(id(a))

#编程题
# total = 10
# a = 2
# b = 4
# c = total - a - b
#
# print('a+c=%d'%(a+b))
# print('c=%d' %c)


#存取钱
# total_price = 100
# save = 10
# total_price = total_price + save
# print('存入%d元，账户余额：%d' %(save, total_price))
# spend = 20
# total_price = total_price - spend
# print('花费%d元，账户余额：%d' %(spend,total_price))
# total_price = total_price - total_price
# print('全部取出，账户余额：%d' %total_price)

# char='a'
# print(ord(char))#查看ASCII码值

#计算BMI
# weight = float(input("请输入你的体重(kg)："))
# height = float(input("请输入你的身高(m)："))
# MBI = weight/(height * height)
# if MBI < 18.5:
#     print("过瘦")
# elif MBI > 23.5:
#     print("过胖")
# else:
#     print("正常")

#年龄判断
# age = (input("请输入年龄："))
# if age.isdigit():   #优化一下判断是否是数字
#     age = int(age)
#     if age >= 0 and age <= 120:
#         print("输入正确")
#     else:
#         print("输入错误")
# else:
#     print("请输入阿拉伯数字")

# py_score = (input("请输入你的python课程成绩："))
# c_score = (input("请输入你的c语言课程成绩："))
# if py_score.isdigit() and c_score.isdigit():
#     py_score = int(py_score)
#     c_score = int(c_score)
#     if(py_score >= 60 or c_score >= 60):
#         print("合格")
#     else:
#         print("不合格")
# else:
#     if not py_score.isdigit() :
#         print("py成绩请输入数字")
#     if not c_score.isdigit() :
#         print("c成绩请输入数字")


#闰年的判断
# year = int(input("输入年份： "))
# if year >= 1582:
#     if year % 4 == 0 and year % 100 != 0:
#         print("普通闰年")
#     elif year % 400 == 0:
#         print("世纪闰年")
#     else:
#         print("不是闰年")
# else:
#     print("年份不得早于1582年！请重新输入")


#while语句
i = 0
while i < 5 :
    print("Hello python!")
    i += 1
