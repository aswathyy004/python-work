# File handling
 
# 1. Create a Text File
file = open("sample.txt", "w")
file.close()
print("File created successfully")

# 2. Write Your Name and Age into a File
file = open("student.txt", "w")
file.write("Name: Rahul\n")
file.write("Age: 21")
file.close()
print("Data written successfully")

# 3. Read Data from a File
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# 4. Append New Content into an Existing File
file = open("student.txt", "a")
file.write("\nCourse: Python")
file.close()
print("Data appended successfully")

# 5. Count the Number of Characters in a File
file = open("student.txt", "r")
data = file.read()
print("Number of Characters:", len(data))
file.close()

# 6. Count the Number of Words in a File
file = open("student.txt", "r")
data = file.read()
words = data.split()
print("Number of Words:", len(words))
file.close()

# 7. Count the Number of Lines in a File
file = open("student.txt", "r")
data = file.readlines()
print("Number of Lines:", len(data))
file.close()

# 8. Display Only the First 5 Lines of a File
file = open("student.txt", "r")
for line in file.readlines()[:5]:
    print(line, end="")
file.close()

# 9. Copy Contents from One File to Another
file1 = open("student.txt", "r")
data = file1.read()
file1.close()
file2 = open("copy.txt", "w")
file2.write(data)
file2.close()
print("File copied successfully")

# 10. Merge Two Text Files
file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()
file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()
file3 = open("merged.txt", "w")
file3.write(data1 + "\n" + data2)
file3.close()
print("Files merged successfully")

# 11. Find the Number of Vowels in a File
file = open("student.txt", "r")
data = file.read().lower()
count = 0
for char in data:
    if char in "aeiou":
        count += 1
print("Number of Vowels:", count)
file.close()

# 12. Replace a Specific Word in a File
file = open("student.txt", "r")
data = file.read()
file.close()
data = data.replace("Rahul", "Arun")
file = open("student.txt", "w")
file.write(data)
file.close()
print("Word replaced successfully")

# 13. Remove All Spaces from a File
file = open("student.txt", "r")
data = file.read()
file.close()
data = data.replace(" ", "")
file = open("student.txt", "w")
file.write(data)
file.close()
print("Spaces removed successfully")

# 14. Convert All Text into Uppercase and Store It in Another File
file = open("student.txt", "r")
data = file.read()
file.close()
file = open("uppercase.txt", "w")
file.write(data.upper())
file.close()
print("Uppercase file created successfully")

# 15. Find the Longest Word in a File
file = open("student.txt", "r")
data = file.read()
file.close()
words = data.split()
longest = max(words, key=len)
print("Longest Word:", longest)

# 16. Print Only Unique Words from a File
file = open("student.txt", "r")
data = file.read()
file.close()
words = data.split()
unique_words = set(words)
for word in unique_words:    
    print(word)

# 17. Remove Duplicate Lines from a File
file = open("student.txt", "r")
lines = file.readlines()
file.close()
unique_lines = list(dict.fromkeys(lines))
file = open("student.txt", "w")
file.writelines(unique_lines)
file.close()
print("Duplicate lines removed")

# 18. Delete All Contents Inside a File
file = open("student.txt", "w")
file.close()
print("All file contents deleted")

# EXCEPTION HANDLING

# 19. Handle Division by Zero
try:    
    a = 10 
    b = 0 
    result = a / b   
    print("Result:", result)
except ZeroDivisionError:   
    print("Cannot divide by zero")

# 20. Handle Invalid Integer Input
try:  
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:  
    print("Please enter a valid integer")

# 21. Handle File Not Found Exception
try:  
    file = open("data.txt", "r") 
    print(file.read())    
    file.close()
except FileNotFoundError: 
    print("File not found")

# 22. Handle Index Out of Range Exception
try:
    numbers = [10, 20, 30] 
    print(numbers[5])
except IndexError: 
    print("Index is out of range")

# 23. Handle Key Errors in Dictionary
try:
    student = {        "name": "Rahul",        "age": 21    }    
    print(student["marks"])
except KeyError:    
    print("Key not found")



# 24. Handle Type Errors
try:
    a = 10 
    b = "20"  
    print(a + b)
except TypeError:
    print("Cannot perform operation between different data types")

# 25. Program Using Multiple Except Blocks
try:
    a = int(input("Enter first number: ")) 
    b = int(input("Enter second number: ")) 
    print(a / b)
except ValueError:
    print("Enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:    
    print("Something went wrong")

# 26. Program Using Nested Try Blocks
try:    
    a = int(input("Enter a number: "))  
    try:        
        b = 10 / a        
        print("Result:", b)   
    except ZeroDivisionError:        
        print("Cannot divide by zero") 
except ValueError:   
    print("Invalid input")

# 27. Using Finally for Cleanup Operations
file = None
try:    
    file = open("student.txt", "r")    
    print(file.read())
except FileNotFoundError:    
    print("File not found")
finally:    
    if file is not None:        
        file.close()    
        print("File operation completed")

# 28. Program Using Else Block
try:    
    a = int(input("Enter first number: "))    
    b = int(input("Enter second number: "))    
    result = a / b
except ZeroDivisionError:    
    print("Cannot divide by zero")
except ValueError:   
    print("Invalid input")
else:    
    print("Result:", result)    
    print("Calculation successful")

# REAL-WORLD EXCEPTION HANDLING PROGRAMS
# 29. Login System with Exception Handling
username = "admin"
password = "12345"
try:    
    user = input("Enter username: ")    
    pwd = input("Enter password: ")   
    if user == username and pwd == password:        
        print("Login successful")   
    else:        
        raise ValueError("Invalid username or password")
except ValueError as e:    
    print(e)

# 30. ATM Withdrawal System with Validations
balance = 50000
try:    
    amount = float(input("Enter withdrawal amount: "))    
    if amount <= 0:        
        raise ValueError("Enter a valid amount")   
    if amount > balance:        
        raise ValueError("Insufficient balance")    
    balance -= amount    
    print("Withdrawal successful")    
    print("Remaining Balance:", balance)
except ValueError as e:    
    print(e)

# 31. Calculator with Exception Handling
try:    
    a = float(input("Enter first number: "))    
    b = float(input("Enter second number: "))    
    operator = input("Enter operator (+, -, *, /): ")    
    if operator == "+":        
        print("Result:", a + b)    
    elif operator == "-":        
        print("Result:", a - b)    
    elif operator == "*":        
        print("Result:", a * b)    
    elif operator == "/":        
        print("Result:", a / b)    
    else:        
        print("Invalid operator")
except ValueError:    
    print("Please enter valid numbers")
except ZeroDivisionError:    
    print("Cannot divide by zero")

# 32. Validate Age Input
try:    
    age = int(input("Enter your age: "))    
    if age < 0:        
        raise ValueError("Age cannot be negative")    
    if age < 18:        
        print("Not eligible")    
    else:        
        print("Eligible")
except ValueError as e:    
    print("Invalid age:", e)



# 33. Validate Email Format
import re
email = input("Enter email: ")
pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
if re.match(pattern, email):    
    print("Valid email")
else:    
    print("Invalid email")

# 34. Retry User Input Until Valid
while True:    
    try:        
        number = int(input("Enter an integer: "))        
        print("Valid number:", number)        
        break    
    except ValueError:        
        print("Invalid input. Try again.")

# 35. Safely Open and Read Files
try:    
    with open("student.txt", "r") as file:        
        data = file.read()        
        print(data)
except FileNotFoundError:    
    print("File does not exist")
except PermissionError:    
    print("Permission denied")

# CUSTOM EXCEPTIONS

# 36. Custom Exception for Insufficient Balance
class InsufficientBalanceError(Exception):    
    passbalance = 5000
    try:    
        amount = int(input("Enter withdrawal amount: "))  
        if amount > balance:  
            raise InsufficientBalanceError("Insufficient balance")    
        balance -= amount    
        print("Remaining Balance:", balance)
    except InsufficientBalanceError as e:    
        print(e)

# 37. Custom Exception for Invalid Password
class InvalidPasswordError(Exception):    
    pass
try:    
    password = input("Enter password: ")    
    if len(password) < 8:     
        raise InvalidPasswordError("Password must contain at least 8 characters")    
    print("Password accepted")
except InvalidPasswordError as e:    
    print(e)

# 38. Custom Exception for Voting Age Eligibility
class NotEligibleError(Exception):    
    pass
try:    
    age = int(input("Enter your age: "))    
    if age < 18:        
        raise NotEligibleError("Not eligible for voting")    
    print("Eligible for voting")
except NotEligibleError as e:    
    print(e)

# 39. Custom Exception for Negative Marks
class NegativeMarksError(Exception):    
    pass
try:    
    marks = int(input("Enter marks: "))    
    if marks < 0:        
        raise NegativeMarksError("Marks cannot be negative")    
    print("Marks:", marks)
except NegativeMarksError as e:    
    print(e)

# 40. Custom Exception for Product Out of Stock
class OutOfStockError(Exception):    
    pass
stock = 5
try:    
    quantity = int(input("Enter quantity: "))    
    if quantity <= 0:        
        raise ValueError("Enter a valid quantity")    
    if quantity > stock:        
        raise OutOfStockError("Product is out of stock or insufficient stock")    
    stock -= quantity    
    print("Order placed successfully")    
    print("Remaining Stock:", stock)
except OutOfStockError as e:    
    print(e)
except ValueError as e:    
    print(e)