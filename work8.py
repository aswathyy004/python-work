basic_salary=35000
bonus = 5000
tax = 2000
Total_salary= basic_salary + bonus
print("Total salary: ",Total_salary)
Final_salary = Total_salary - tax
print("Final salary: ",Final_salary)
Yearly_salary = Final_salary * 12
print("Yearly_salary: ", Yearly_salary)
print("Salary: ",Yearly_salary//12)

mobile_price = 45000
discount = 5000
gst = 2000

discounted_price = mobile_price - discount
final_amount = discounted_price + gst
half_amount = final_amount / 2
remainder = final_amount % 3
print("Discounted Price:", discounted_price)
print("Final Amount:", final_amount)
print("Half Amount:", half_amount)
print("Remainder:", remainder)

python_marks = 85
sql_marks = 78
powerbi_marks = 90
total_marks = python_marks + sql_marks + powerbi_marks
average_marks = total_marks / 3
python_greater = python_marks > sql_marks
powerbi_equal = powerbi_marks == python_marks
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Python > SQL:", python_greater)
print("Power BI == Python:", powerbi_equal)

product_price = 1200
quantity = 4
delivery_charge = 150
total_cost = product_price * quantity
total_bill = total_cost + delivery_charge
bill_check = total_bill > 5000
quantity_square = quantity ** 2
print("Total Product Cost:", total_cost)
print("Total Bill:", total_bill)
print("Bill Greater Than 5000:", bill_check)
print("Square of Quantity:", quantity_square)

daily_usage = 2.5
days = 30
monthly_usage = daily_usage * days
usage_mb = monthly_usage * 1024
usage_check = monthly_usage > 50
monthly_usage += 10
print("Monthly Usage:", monthly_usage - 10)
print("Usage in MB:", usage_mb)
print("Usage Greater Than 50 GB:", usage_check)
print("Usage After Adding 10 GB:", monthly_usage)

balance = 50000
deposit = 12000
withdraw = 7000
balance += deposit
balance -= withdraw
final_balance = balance * 2
balance_check = balance < 100000
print("Balance After Deposit and Withdrawal:", balance)
print("Double the Final Balance:", final_balance)
print("Balance Less Than 100000:", balance_check)

laptop_price = 80000
months = 10
emi = laptop_price / months
remainder = emi % 7
emi_check = emi > 5000
emi += 500
print("Monthly EMI:", emi - 500)
print("Remainder:", remainder)
print("EMI Greater Than 5000:", emi_check)
print("EMI After Increase:", emi)

instagram = 25000
youtube = 18000
linkedin = 12000
total_followers = instagram + youtube + linkedin
difference = instagram - linkedin
followers_check = youtube != linkedin
double_followers = total_followers * 2
print("Total Followers:", total_followers)
print("Difference:", difference)
print("YouTube != LinkedIn:", followers_check)
print("Double Total Followers:", double_followers)

student = {
    "name": "Rahul",
    "course": "Data Science",
    "marks": 88,
    "city": "Bangalore"
}
print(student["name"])
print(student["course"])
student["marks"] = 95
student["email"] = "rahul@gmail.com"
student.pop("city")
print(student.values())

employee = {
    "id": 101,
    "name": "Anjali",
    "department": "HR",
    "salary": 45000
}
print(employee["salary"])
employee["salary"] += 5000
employee["location"] = "Kochi"
employee.pop("department")
print(employee.keys())

mobile = {
    "brand": "Samsung",
    "model": "S24",
    "price": 75000,
    "storage": "256GB"
}
print(mobile["model"])
mobile["price"] = 70000
mobile["color"] = "Black"
mobile.pop("storage")
print(mobile)

movie = {
    "title": "Leo",
    "hero": "Vijay",
    "rating": 8.5,
    "language": "Tamil"
}
print(movie["title"])
movie["rating"] = 9.1
movie["director"] = "Lokesh"
movie.pop("language")
print(movie.items())

order = {
    "item": "Burger",
    "quantity": 2,
    "price": 250,
    "status": "Preparing"
}
print(order["item"])
total_price = order["quantity"] * order["price"]
order["status"] = "Delivered"
order["payment"] = "Online"
order.pop("quantity")
print("Total Price:", total_price)
print(order)

laptop = {
    "brand": "Dell",
    "ram": "16GB",
    "price": 65000,
    "processor": "i7"
}
print(laptop["ram"])
laptop["processor"] = "i9"
laptop["warranty"] = "2 Years"
laptop.pop("price")
print(laptop.keys())
print(laptop.values())

patient = {
    "name": "Arjun",
    "age": 32,
    "blood_group": "O+",
    "room": 205
}
print(patient["name"])
patient["room"] = 210
patient["doctor"] = "Dr. Meera"
patient.pop("age")
print(patient)

product = {
    "product_name": "Headphones",
    "price": 2999,
    "rating": 4.4,
    "stock": 50
}
print(product["price"])
product["stock"] = 40
product["brand"] = "Sony"
product.pop("rating")
print(product.keys())
print(product.values())

employee = {
    "name": "Akhil",
    "salary": 50000,
    "bonus": 10000
}
total_salary = employee["salary"] + employee["bonus"]
employee["department"] = "AI Team"
employee["salary"] += 5000
salary_check = total_salary > 60000
print("Total Salary:", total_salary)
print(employee)
print("Salary Greater Than 60000:", salary_check)

cart = {
    "item": "Keyboard",
    "price": 1500,
    "quantity": 3
}
total_amount = cart["price"] * cart["quantity"]
cart["delivery"] = 100
final_bill = total_amount + cart["delivery"]
bill_check = final_bill > 5000
print("Total Cart Amount:", total_amount)
print("Final Bill:", final_bill)
print("Bill Greater Than 5000:", bill_check)
print(cart)

student = {
    "name": "Diya",
    "course_fee": 45000,
    "paid": 20000
}
remaining_fee = student["course_fee"] - student["paid"]
student["course"] = "Python Full Stack"
student["paid"] = 30000
payment_check = student["paid"] == student["course_fee"]
print("Remaining Fee:", remaining_fee)
print(student)
print("Fee Fully Paid:", payment_check)

