#learn python with Bro Code
import math

#字符串
# first_name = "huo"
# food = "bread"
# email = "Byhuohuohahei@123.com"
# print("My name is "+first_name + ",My favourite food is " + food + ",My email is " + email)
# print(f"My name is {first_name},My favourite food is {food},My email is {email}")#用起来更方便


#整型
# age = 22
# quantity = 3
# num_of_students = 30
# print(f"You are {age} years old")
# print(f"You are buying {quantity} items")
# print(f"Your class has {num_of_students} students")

#浮点型
# price = 10.99
# gpa = 3.2
# distance = 5.5
# print(f"The price is ${price}")
# print(f"You gpa is:{gpa}")
# print(f"You ran {distance}km")


#布尔型
# is_stusent = True
# print(f"Are you a student? {is_stusent}")

#查看变量类型,用type()
# name = "HuoHuoHaHei"
# age = 25
# gpa = 3.2
# is_student = True
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

#强制转换类型
# gpa = int(gpa)
# print(gpa)
# print(type(gpa))
# age = float(age)
# print(age)
# print(type(age))


#input的使用,输入函数返回的是一个字符串类型
# name = input("What is you name?: ")
# print(f"Hello {name}!")
# age = input("How old are you?: ")
# print(f"you are {age} years old")
# age = input("How old are you?: ")#like:int(input("ababa"))
# age = int(age) # or直接用int()把input括上
# age = age + 1
# print(f"you are {age} years old")


#exercise
# length = float(input("Enter the length: "))
# weight = float(input("Enter the weight: "))
# area = length * weight
# print(f"The area is:{area}cm²")

#exercise2
# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
# print(f"You've bought {quantity} x {item}/s")
# print(total)

#Madlibs game 随机填写空格内容
# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 =input("Enter a verb ending with 'ing': ")
# adjective3 = input("Enter an adjective (description): ")
# print(f"Tooday I want to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# friends = 4
#friends = friends + 1
#friends =+ 1
# friends = friends / 2
# friends /= 2
#friends = friends ** 2#=>4*4
#friends **= 2
# reminder = friends % 3
# print(friends)
# print(reminder)


#数学常用公式
# x = 3.14
# y = -4
# z = 5
# result = round(x)#取整数
# result = abs(y)#取绝对值
# result = pow(2,3)#取幂函数2的三次方
# result = max(x,y,z)#取最大值
# result = min(x,y,z)#取最小值
# print(result)


#应用Π要在开头写 import math
# print(math.pi)
# print((math.e))
# x = 9.9
#result = math.sqrt(x)#取平方根
#result = math.ceil(x)#向上取整 eg:9.1=>10
# result = math.floor(x)#向下取整 eg:9.9=>9
# print(result)

#exercise计算圆的半径
# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# #print(f"The circumference is:{circumference}")
# print(f"The circumference is:{round(circumference, 2)}cm")#使数值变成定点小数，如这里的两位小数
#计算圆的面积
# radius = float(input('Enter the radius of a circle: '))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {round(area, 2)}")


#勾股定理
# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = math.sqrt(pow(a, 2) + pow(b,2))
# print(f"The xiebian is {c}")


#if的用法
# age = int(input("Enter you age: "))
#
# if age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You must be 18+ to signed up")