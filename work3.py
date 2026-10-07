# mark = int(input("Enter your marks:")) 
# if 90<=mark<=100:
#     print("A+")
# elif 80<=mark<90:
#     print("A")
# elif 70<=mark<80:
#     print("B")
# elif 60<=mark<70:
#     print("C")
# elif 50<=mark<60:
#     print("D")
# else:
#     print("Fail")

# balance = float(input("Enter account balance: "))
# amount = float(input("Enter withdrawal amount: "))
# if amount > balance:
#     print("Insufficient Balance")
# elif amount % 100 != 0:
#     print("Enter an amount in multiples of ₹100")
# else:
#     print("Withdrawal Successful")

# order = float(input("Enter order value: "))
# if order >= 5000:
#     delivery = 0
# elif order >= 2000:
#     delivery = 50
# else:
#     delivery = 100
# final_amount = order + delivery
# print("Delivery charge:", delivery)
# print("Final payable amount:", final_amount)

# score = int(input("Enter performance score: "))
# if 90 <= score <= 100:
#     print("Excellent")
# elif 75 <= score < 90:
#     print("Very Good")
# elif 60 <= score < 75:
#     print("Good")
# elif 40 <= score < 60:
#     print("Needs Improvement")
# else:
#     print("Poor")

# units = int(input("Enter units consumed: "))
# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + ((units - 100) * 3)
# elif units <= 400:
#     bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
# else:
#     bill = (100 * 2) + (100 * 3) + (200 * 5) + ((units - 400) * 7)
# print("Electricity bill:", bill)

# age = int(input("Enter age: "))
# if 5 <= age < 13:
#     print("Ticket price: ₹0")
# elif 13 <= age < 60:
#     print("Ticket price: ₹100")
# else:
#     print("Ticket price: ₹120")

# speed = int(input("Enter vehicle speed: "))
# if speed <= 60:
#     print("No fine")
# elif 61 <= speed <= 80:
#     print("Fine: ₹500")
# elif 81 <=  speed <= 100:
#     print("Fine: ₹1000")
# else:
#     print("Fine: ₹2000 and License Review")

# bill = float(input("Enter total bill: "))
# if bill >= 5000:
#     discount = bill * 20 / 100
# elif 3000 <= bill < 5000:
#     discount = bill * 15 / 100
# elif 1000 <= bill < 3000:
#     discount = bill * 10 / 100
# else:
#     discount = 0
# final_bill = bill - discount
# print("Discount:", discount)
# print("Final bill:", final_bill)

# score = int(input("Enter entrance score: "))
# if 90 <= score <= 100:
#     print("Direct Admission")
# elif 75 <= score < 90:
#     print("Admission + Interview")
# elif 60 <= score < 75:
#     print("Waitlisted")
# else:
#     print("Not Eligible")

# score = int(input("Enter credit score: "))
# default = input("Existing loan default? (yes/no): ")
# if default == "yes":
#     print("Loan Approval Requires Manual Review")
# elif 750 <= score <= 900:
#     print("Low Risk")
# elif 650 <= score < 750:
#     print("Medium Risk")
# elif 550 <= score < 650:
#     print("High Risk")
# else:
#     print("Very High Risk")

# room = input("Enter room type: ")
# nights = int(input("Enter number of nights: "))
# if room == "Standard":
#     price = 2000
# elif room == "Deluxe":
#     price = 3500
# elif room == "Suite":
#     price = 5000
# else:
#     price = 0
#     print("Invalid room type")
# if price != 0:
#     total = price * nights
#     if nights > 5:
#         total = total - (total * 10 / 100)
#     print("Final bill:", total)

# salary = float(input("Enter annual salary: "))
# performance = int(input("Enter performance score: "))
# if 90 <= performance <= 100:
#     bonus = salary * 20 / 100
# elif 75 <= performance < 90:
#     bonus = salary * 15 / 100
# elif 60 <= performance < 75:
#     bonus = salary * 10 / 100
# else:
#     bonus = 0
# print("Bonus:", bonus)

# data = float(input("Enter monthly data requirement in GB: "))
# if 1 <= data < 5:
#     print("Basic Plan - ₹199")
# elif 5 <= data <= 20:
#     print("Standard Plan - ₹399")
# elif 20 < data <= 50:
#     print("Premium Plan - ₹699")
# else:
#     print("Unlimited Plan - ₹999")

# hours = int(input("Enter parking duration in hours: "))
# electric = input("Is it an electric vehicle? (yes/no): ")
# if 0 <= hours <= 2:
#     fee = 30
# elif 3 <= hours <= 5:
#     fee = 50
# elif 6 <= hours <= 10:
#     fee = 100
# else:
#     fee = 150
# if electric == "yes":
#     fee = fee - (fee * 20 / 100)
# print("Final parking fee:", fee)

# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))
# if theory <= 40 or practical <= 40:
#     print("Fail")
# else:
#     average = (theory + practical) / 2
#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")

# weight = float(input("Enter baggage weight: "))
# business = input("Business Class? (yes/no): ")
# if business == "yes":
#     free_limit = 25
# else:
#     free_limit = 15
# if weight <= free_limit:
#     charge = 0
# elif weight <= 20:
#     charge = 500
# elif weight <= 30:
#     charge = 1000
# else:
#     charge = 2000
# print("Baggage charge:", charge)

# days = int(input("Days since purchase: "))
# unused = input("Is the product unused? (yes/no): ")
# returnable = input("Is the product returnable? (yes/no): ")
# if days > 7:
#     print("Return Rejected: Purchased more than 7 days ago")
# elif unused != "yes":
#     print("Return Rejected: Product is used")
# elif returnable != "yes":
#     print("Return Rejected: Product is not returnable")
# else:
#     print("Return Approved")

# salary = float(input("Enter annual salary: "))
# if 0 <= salary <= 300000:
#     tax = 0
# elif 300001 <= salary <= 600000:
#     tax = salary * 5 / 100
# elif 600001 <= salary <= 1000000:
#     tax = salary * 10 / 100
# else:
#     tax = salary * 20 / 100
# final_salary = salary - tax
# print("Tax:", tax)
# print("Final salary:", final_salary)

# distance = float(input("Enter distance in km: "))
# peak = input("Is it peak hour? (yes/no): ")
# if 0 <= distance <= 5:
#     fare = 100
# elif 6 <= distance <= 15:
#     fare = 100 + (distance - 5) * 15
# elif 16 <= distance <= 30:
#     fare = 100 + (10 * 15) + (distance - 15) * 12
# else:
#     fare = 100 + (10 * 15) + (15 * 12) + (distance - 30) * 10
# if peak == "yes":
#     fare = fare + (fare * 20 / 100)
# print("Final fare:", fare)

available = int(input("Enter available leave: "))
requested = int(input("Enter requested leave: "))
if requested > available:
    print("Leave Rejected")
elif requested <= 3:
    print("Leave Automatically Approved")
elif 4 <= requested <= 7:
    print("Manager Approval Required")
else:
    print("HR Approval Required")