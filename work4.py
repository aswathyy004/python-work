# a = str(input("Enter a traffic color:"))
# if a== "red":
#     print("Stop")
# elif a=="yellow":
#     print("Slow down")
# elif a=="green":
#     print("Go")  
# else:
#     print("Invalid")     

# num= int(input("enter a whole no.:"))
# if num%2==0 :
#     print(f"the no. {num} is even")
# else:
#     print(f"The no. {num} is odd")

# n= int(input("enter a no.:"))
# if n>0:
#     print(f"{n} is positive")
# elif n<0:
#     print(f"{n} is negative")
# else:
#     print("The no. is zero")        

# age= int(input("enter age.:"))
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Ineligible to vote")    

# n = int(input("Enter the temperature:"))
# if n<20:
#     print("cold")
# elif 20 <= n <= 30:
#     print("Warm")
# else:
#     print("hot")    

# year = int(input("Enter a year: "))
# if year % 4 == 0: # any year divisible by 4 is a leap year
#     print("Leap year")
# elif year % 100 == 0: # years divisible by 100 are not leap years
#     print("Not a leap year")
# elif year % 400 == 0: # Century years divisible by 400 are leap years (e.g., 1600, 2000).
#     print("Leap year")
# else:
#     print("Not a leap year")

# mark = int(input("Enter your marks:")) 
# if 90<=mark<=100:
#     print("A")
# elif 80<=mark<90:
#     print("B")
# elif 70<=mark<80:
#     print("C")
# elif 60<=mark<70:
#     print("D")
# elif 0<=mark<60:
#     print("F")
# else:
#     print("Invalid mark entry!!!")

# n = int(input("Enter a number: "))
# if n > 0:
#     if n % 2 == 0:
#         print("Positive and even")
#     else:
#         print("Not positive or not even")
# else:
#     print("Not positive or not even")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("Largest:", a)
# elif b >= a and b >= c:
#     print("Largest:", b)
# else:
#     print("Largest:", c)

# amount = float(input("Enter purchase amount: "))
# if amount > 5000:
#     discount = amount * 20 / 100
# elif 2000 <= amount < 5000:
#     discount = amount * 10 / 100
# else:
#     discount = 0
# final_bill = amount - discount
# print("Discount:", discount)
# print("Final bill:", final_bill)

# day = int(input("Enter a day number: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid day number")

# for n in range(1,11):
#     print (n)

# n = int(input("Enter a number:"))
# for i in range (1,11):
#     print(i,"x",n,"=",i * n )

# n = int(input("Enter n: "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print("Sum:", total)

# n = int(input("How many numbers? "))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     a, b = b, a + b

# for i in range(1, 3):
#     print("*" * i)
# for i in range(1, 3):
#     print("*" * i)
# OR
# for i in range(4):
#   if i % 2 == 0:
#     print("*")
#   else:
#     print("**")

# text = input("Enter a string: ")
# reverse = ""
# for char in text:
#     reverse = char + reverse
# print(reverse)

# for num in range(1, 51):
#     if num % 2 == 0:
#         print(num)

# n = int(input("Enter n: "))
# while n >= 1:
#     print(n)
#     n = n - 1

# n = int(input("Enter a number: "))
# factorial = 1
# while n > 1:
#     factorial = factorial * n
#     n = n - 1
# print("Factorial:", factorial)

# n = int(input("Enter a number: "))
# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10

# n = int(input("Enter a number: "))
# count = 0
# if n == 0:
#     count = 1
# else:
#     while n != 0:
#         count = count + 1
#         n = n // 10
# print("Number of digits:", count)

# while True:
#     text = input("Enter something (or exit): ")
#     if text == "exit":
#         break
#     print("You entered:", text)

# numbers = [10, 20, 30, 40, 50]
# target = int(input("Enter number to find: "))
# for n in numbers:
#     if n == target:
#         print("Number found")
#         break
# else:
#     print("Number not found")

# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         pass
#     print(i)

# day = int(input("Enter day number (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid day")

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")
# match op:
#     case "+":
#         print(a + b)
#     case "-":
#         print(a - b)
#     case "*":
#         print(a * b)
#     case "/":
#         if b != 0:
#             print(a / b)
#         else:
#             print("Cannot divide by zero")
#     case _:
#         print("Invalid operator")

# marks = int(input("Enter marks (0-100): "))
# match marks:
#     case x if 90 <= x <= 100:
#         print("Grade A")
#     case x if 80 <= x < 90:
#         print("Grade B")
#     case x if 70 <= x < 80:
#         print("Grade C")
#     case x if 60 <= x < 70:
#         print("Grade D")
#     case x if 0 <= x < 60:
#         print("Grade F")
#     case _:
#         print("Invalid marks")

# status = int(input("Enter HTTP status code: "))
# match status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case x if 500 <= x <= 599:
#         print("Server Error")
#     case x if 400 <= x <= 499:
#         print("Client Error")
#     case _:
#         print("Other status code")

# row = int(input("Enter row (1-8): "))
# col = int(input("Enter column (1-8): "))
# if row < 1 or row > 8 or col < 1 or col > 8:
#     print("Invalid position")
# else:
#     match (row % 2, col % 2):
#         case (1, 1) | (0, 0):
#             print("Black")
#         case (1, 0) | (0, 1):
#             print("White")

# cmd = input("Enter command (add or quit): ").split()
# match cmd:
#     case ["add", a, b]:
#         print(float(a) + float(b))
#     case ["quit"]:
#         print("Exiting")
#     case _:
#         print("Invalid command")

# filename = input("Enter filename: ")
# parts = filename.split(".")

# match parts:
#     case [name, "jpg"] | [name, "png"]:
#         print("Image file")
#     case [name, "py"]:
#         print("Python file")
#     case _:
#         print("Unknown file type")

# import math
# shape = input("Enter shape (circle or rect): ")
# if shape == "circle":
#     radius = float(input("Enter radius: "))
#     data = ("circle", radius)
# elif shape == "rect":
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))
#     data = ("rect", length, width)
# else:
#     data = ("invalid",)
# match data:
#     case ("circle", r):
#         print("Area:", math.pi * r * r)
#     case ("rect", l, w):
#         print("Area:", l * w)
#     case _:
#         print("Invalid shape")