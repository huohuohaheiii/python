#learn python with Mosh
#变量
# age = 20
# age = 30
# user_name ="Huo"
# is_online = False
# print(age)
# patient_name ="John Smith"
# age = 20
# imforation = "a new patient"
#输入函数
# name = input("what is your name? ")
# print("Hello " + name)
#改变函数类型 int(),float(),bool(),str()
# birth_year = input("Enter you birth year: ")
# age = 2025- int(birth_year)#int()函数即函数转换成int型
# print(age)#错误原因：用整数2020减去一个字符串输入的数字

#输入两个数字，打印两个数字的和
# First = input("first number: ")
# Second = input("second number: ")
# sum = float(First)+ float(Second)
# print("Sum: " +str(sum))

#写法2
# First = float(input("first number: "))
# Second = float(input("second number: "))
# sum = First + Second
# print("Sum: " +str(sum))

#字符串
# course = 'Python for Beginners'
# print(course.upper())
# print(course.lower())
# print(course.find('for'))
# print(course.replace('for','4'))
# print(course.find('Python'))
# print('Python' in course)

#运算
# print(10+3)加
# print(10*3)乘
# print(10/3)除
# print(10//3)商的整数部分
# print(10%3)余数
# print(10**3)密

# x = 10
# x = x + 3#等价于x += 3

# temperature = 25
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20: #(20,30]
#     print("It's a nice day")
# elif temperature > 10: #(10,20]
#     print("It's a it cold")
# else:
#     print("It's cold")
# print("Must Done")

# weight = float(input("Weight: "))#float型才能进行乘除法
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == 'K':
#     converted = weight / 0.45
#     print("Weight in Lbs:" + str(converted) )#字符串不能直接加float型，要强制转换成str
# else:
#     converted = weight * 0.45
#     print("Weight in Kg:" + str(converted))

#while循环
# i = 1
# while i<=10:
#     print(i * '*')#因为是乘法整型可以和字符串型一起使用
#     i += 1

#数组
# names= ["huo","john","ha","hei"]
# names[1] = "jon"#修改元素内容
# print(names[0])
# print(names[0:3])#输出从0开始数的3个元素

#数组“.”的用法
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)#添加一个新元素
# print(numbers)

# numbers.insert(0,-1)#在某个位置插入元素
# print(numbers)

# numbers.remove(3)#删除元素
# print(numbers)

# numbers.clear()#清除列表所有元素，不需要参数
# print(numbers)

#print(3 in numbers)#查找元素是否在列表中，返回一个布尔值
# print(len(numbers))#查询表的长度，len和print一样是内置函数

#for循环,for循环比while循环简便
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:  #其中item是自己取得
#     print(item)

# i = 1
# while i < len(numbers):
#     print(i)
#     i += 1

#range函数
# numbers = range(5)
# print(numbers)#打印结果为：range(0,5)，要用for循环来实现数字的打印
# for number in numbers:
#     print(number)

# numbers = range(5,10)#前面为开始值，后面为结束值但不包括在内，即打印结果:5,6,7,8,9
# for number in numbers:
#     print(number)

# numbers = range(5,10,2)#这里2为步长，即打印结果：5,7,9
# for number in numbers:
#     print(number)

# for number in range(5):#也可以直接for循环打印range
#     print(number)#打印结果：0,1,2,3,4