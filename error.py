name = "Rahul"
age = int("20")
print("Name:", name) 
print("Age next year:", age + 1) 

student_name = "Anu"
student_age = 21
student_course = "Python"
print(student_name)
print(student_age)
print(student_course) 

price = 99.50 
quantity = int("3") 
total = price * quantity 
price = 99.50 
quantity = int("3") 
total = price * quantity 

x = 10 
y = 20 
total = x + y
print(total) 

first_name = "Arun" 
last_name = "Kumar" 
full_name = first_name + " " + last_name 
print("Full name: ", full_name) 
print("Name length:", len(full_name))

a = 15 
b = 4 
print("Addition:", a + b) 
print("Subtraction:", a - b) 
print("Multiplication:", a * b) 
print("Division:", a / b) 
print("Remainder:", a % b) 

marks = 75
if marks == 75: 
    print("Marks are 75") 

age = 20 
if 18 < age < 25:
    print("Eligible") 

a = 10 
b = 20 
result = 'True' if a > b and a < b else 'False'
print("Result:", result) 

x = 10 
y = 3 
print(x ** y)
print(x*x*x) 

# age = int(input("Enter your age: ")) 
# if age >= 18: 
#     print("Adult") 
# else: 
#     print("Minor") 

# num1 = int(input("Enter first number: ")) 
# num2 = int(input("Enter second number: ")) 
# sum = num1 + num2 
# print("Sum:", sum)     

# temperature = int(input("Enter temperature: "))
# if temperature > 30:
#     print("Hot") 
# else: 
#     print("Normal") 

# radius = int(input("Enter radius: "))
# area = 3.14 * radius * radius 
# print("Area:", area) 

marks = 85 
if marks >= 90: 
    print("A") 
elif marks >= 75: 
    print("B") 
elif marks >= 50: 
    print("C") 
else: 
    print("Fail") 

age = 17 
if age >= 18: 
    print("You can vote") 
else: 
    print("You cannot vote") 

number = 10 
if number % 2 == 0: 
    print("Even") 
else: 
    print("Odd")     

username = "admin" 
password = "1234"  
if username == "admin":     
    if password == "1234":         
        print("Login successful")     
    else:          
        print("Wrong password")  
else:     
    print("Wrong username")

marks = 65
if marks >= 90:  
    grade = "A" 
elif marks >= 75:     
    grade = "B" 
elif marks >= 50:     
    grade = "C" 
else:     
    grade = "F"  
print(grade)  

number = 0 
if number > 0: 
    print("Positive") 
elif number < 0: 
    print("Negative") 
elif number == 0: 
    print("Zero") 

age = 25 
if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Minor")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age >= 18: 
#     print(name + " is eligible to vote") 
# else: 
#     print(name + " is not eligible to vote") 

# price = int(input("Enter product price: "))
# discount = int(input("Enter discount percentage: ")) 
# discount_amount = price * discount / 100 
# final_price = price - discount_amount 
# print("Final price:", final_price) 

# number = int(input("Enter a number: ")) 
# if number % 2 == 0: 
#     print("Even number") 
# elif number % 2 == 1: 
#     print("Odd number") 
# else: 
#     print("Invalid") 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print(a, "is greater") 
# elif b > a: 
#     print(b, "is greater") 
# else: 
#     print("Both numbers are equal") 

# year = int(input("Enter your birth year: ")) 
# age = 2026 - year 
# print("Your age is:", age) 

num = 15 
if num % 3 == 0 and num % 5 == 0: 
    print("Divisible by both") 
elif num % 3 == 0: 
    print("Divisible by 3") 
elif num % 5 == 0: 
    print("Divisible by 5") 
else: 
    print("Not divisible by 3 or 5") 

marks = 82 
attendance = 78 
if marks >= 50 and attendance >= 75: 
    print("Eligible for exam") 
else: 
    print("Not eligible") 

a = 10 
b = 20 
c = 30  
if a > b and a > c :     
    largest = a 
elif b > c and b > a :     
    largest = b 
else:     
    largest = c  
print("Largest:", largest) 

# username = input("Enter username: ")
# age = int(input("Enter age: "))
# marks = int(input("Enter marks: "))
# if username == "student" and age >= 18 and marks >= 50:
#     print("Admission successful")
# elif username == "student" and age >= 18 and marks >= 40:
#     print("Admission pending")
# else:
#     print("Admission rejected")

# 1. Lists — Adding Elements
students = ["Anu", "Rahul", "Meera"]
students.append("Arun")
print(students)

# 2. Lists — Indexing
marks = [78, 85, 92, 67, 88]
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# 3. Lists — Updating Elements
fruits = ["Apple", "Banana", "Orange"]
fruits[2] = "Mango"
print(fruits)

# 4. Lists — Removing Elements
subjects = ["Python", "Java", "HTML", "CSS"]
subjects.remove("Java")
print(subjects)

# 5. Lists — Sorting
numbers = [45, 12, 78, 23, 9]
numbers.sort()
print(numbers)

# 6. Tuples
student = ("Rahul", 21, "Python")
student = list(student)
student[1] = 22
student = tuple(student)
print(student)

# 7. Tuple Unpacking
student = ("Anu", 21, "Data Science")
name, age, course = student
print(name)
print(age)
print(course)

# 8. Sets — Adding Elements
numbers = {10, 20, 30, 40}
numbers.add(50)
print(numbers)

# 9. Sets — Duplicate Values
numbers = [10, 20, 20, 30, 30, 30]
print(len(numbers))

# 10. Dictionaries — Safe Access
student = {
    "name": "Arun",
    "age": 20,
    "course": "Python"
}
print(student.get("marks", "Marks not available"))

student = {    "name": "Arun",    "age": 20,    "course": "Python"}print(student.get("marks", "Marks not available"))


# 11. Dictionary — Updating
student = {
    "name": "Meera",
    "age": 21
}
student["age"] = 22
print(student)

# 12. Dictionary — Adding Data
student = {
    "name": "Rahul",
    "course": "Python"
}
student["age"] = 20
print(student)

# 13. Function Definition
def greet():
    print("Hello, students!")
greet()

# 14. Function Call
def welcome():
    print("Welcome to Python")
welcome()

# 15. Parameters
def greet(name):
    print("Hello", name)
greet("Anu")

# 16. Multiple Parameters
def add(a, b):
    print("Sum:", a + b)
add(10, 20)

# 17. Return Value
def square(number):
    return number * number
result = square(5)
print(result)

# 18. Return vs Print
def add(a, b):
    print("Calculation completed")
    return a + b
result = add(10, 20)
print(result)

# 19. Local Variable
def calculate():
    total = 100
    return total
result = calculate()
print(result)

# 20. Default Arguments
def greet(name, message="Good morning", extra=""):
    print(message, name, extra)
greet("Anu", "Good evening", "Welcome")

# 21. Function Logic
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = is_even(10)
print(result)

# 22. Function with Input
def calculate_area():
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    return area
print(calculate_area())

# 23. Importing a Module
import math

print(math.sqrt(25))

# 24. Using Module Functions
import math

number = 16
print(math.sqrt(number))

# 25. Import Specific Function
from math import sqrt

print(sqrt(49))

# 26. Random Module
import random

number = random.randint(1, 100)
print("Random number:", number)

# 27. Module Alias
import math as m

print(m.pi)

# 28. Date and Time
from datetime import date

today = date.today()
print(today)

# 29. Collection + Function
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
marks = [75, 80, 90, 85]
print("Average:", calculate_average(marks))

# 30. Function + Dictionary
def display_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student.get("course", "Course not available"))
student = {
    "name": "Arun",
    "age": 21
}
display_student(student)

# 31. Function + Set
def count_unique(numbers):
    unique = set(numbers)
    return len(unique)
numbers = [10, 20, 10, 30, 20, 40]
print("Unique numbers:", count_unique(numbers))

# 32. Module + Function
import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
print(calculate_circle_area(5))

# 33. List + Function + Conditional
def find_passed_students(marks):
    passed = []
    for mark in marks:
        if mark >= 40:
            passed.append(mark)
    return passed
marks = [35, 40, 45, 60, 72]
print(find_passed_students(marks))

# 34. Dictionary + Function + Module
import math
def calculate_discount(price, percentage):
    discount = price * percentage / 100
    return price - discount
product = {
    "name": "Laptop",
    "price": "50000",
    "discount": 10
}
final_price = calculate_discount(
    float(product["price"]),
    product["discount"]
)
print("Final price:", math.floor(final_price))

# 35. Final Challenge
import random
def generate_student():
    student = {
        "name": "Rahul",
        "marks": [78, 85, 92, 67]
    }
    average = sum(student["marks"]) / len(student["marks"])
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"
    student["average"] = average
    student["grade"] = grade
    student["id"] = random.randint(1000, 9999)
    return student
result = generate_student()
print("Student:", result["name"])
print("Average:", result["average"])
print("Grade:", result["grade"])
print("ID:", result["id"])