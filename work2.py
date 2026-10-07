# age = int(input("Enter your age: "))
# student = input("Are you a student? (yes/no): ")
# if age >= 18 and age <= 25 and student == "yes":
#     print("Eligible for registration")
# else:
#     print("Not eligible")

# amount = float(input("Enter order amount: "))
# premium = input("Are you a premium member? (yes/no): ")
# if amount >= 3000 or premium == "yes":
#     print("Discount available")
# else:
#     print("Discount not available")

# ticket = input("Is the ticket confirmed? (yes/no): ")
# passport = input("Is the passport valid? (yes/no): ")
# hours = float(input("Hours until departure: "))
# if ticket == "yes" and passport == "yes" and hours > 2:
#     print("Online check-in available")
# else:
#     print("Online check-in unavailable")

# age = int(input("Enter your age: "))
# if age < 12 or age >= 60:
#     print("Special ticket price")
# else:
#     print("Regular ticket price")

# income = float(input("Enter monthly income: "))
# score = int(input("Enter credit score: "))
# default = input("Have an existing loan default? (yes/no): ")
# if income >= 40000 and score >= 700 and default == "no":
#     print("Eligible for initial screening")
# else:
#     print("Not eligible")

# amount = float(input("Enter order amount: "))
# premium = input("Premium member? (yes/no): ")
# disabled = input("Has the restaurant disabled delivery? (yes/no): ")
# if (amount >= 500 or premium == "yes") and disabled == "no":
#     print("Free delivery available")
# else:
#     print("Free delivery unavailable")

# months = int(input("Months worked in the company: "))
# remote = input("Does the project allow remote work? (yes/no): ")
# if months >= 6 and remote == "yes":
#     print("Work from home allowed")
# else:
#     print("Work from home not allowed")

# available = input("Is the room available? (yes/no): ")
# payment = input("Is the payment method valid? (yes/no): ")
# stopped = input("Has the hotel stopped reservations? (yes/no): ")
# if available == "yes" and payment == "yes" and stopped == "no":
#     print("Booking can proceed")
# else:
#     print("Booking cannot proceed")

# login = input("Logged in? (yes/no): ")
# registration = input("Registration confirmed? (yes/no): ")
# active = input("Is the exam active? (yes/no): ")
# blocked = input("Is the account blocked? (yes/no): ")
# if login == "yes" and registration == "yes" and active == "yes" and blocked == "no":
#     print("Exam access granted")
# else:
#     print("Exam access denied")

# years = float(input("Years subscribed: "))
# active = input("Is the current membership active? (yes/no): ")
# yearly = input("Have you purchased a yearly plan? (yes/no): ")
# if (years >= 1 and active == "yes") or yearly == "yes":
#     print("Premium upgrade available")
# else:
#     print("Premium upgrade unavailable")

# service = input("Is the pickup within the service area? (yes/no): ")
# driver = input("Is a driver available? (yes/no): ")
# scheduled = input("Are scheduled rides enabled? (yes/no): ")
# if (service == "yes" and driver == "yes") or scheduled == "yes":
#     print("Booking allowed")
# else:
#     print("Booking unavailable")

# days = int(input("Days since purchase: "))
# unused = input("Is the product unused? (yes/no): ")
# eligible = input("Is the product eligible for return? (yes/no): ")
# if days <= 7 and unused == "yes" and eligible == "yes":
#     print("Return accepted")
# else:
#     print("Return rejected")

# overdue = input("Do you have overdue books? (yes/no): ")
# active = input("Is your library membership active? (yes/no): ")
# available = input("Is the requested book available? (yes/no): ")
# if overdue == "no" and active == "yes" and available == "yes":
#     print("Book can be borrowed")
# else:
#     print("Book cannot be borrowed")

# years = float(input("Years of Python experience: "))
# django = input("Do you know Django? (yes/no): ")
# fastapi = input("Do you know FastAPI? (yes/no): ")
# if years >= 3 or (years >= 1 and (django == "yes" or fastapi == "yes")):
#     print("Qualified for next stage")
# else:
#     print("Not qualified")

# usage = float(input("Enter data usage percentage: "))
# remaining = float(input("Enter remaining data in GB: "))
# unlimited = input("Is it an unlimited data plan? (yes/no): ")
# if unlimited == "no" and (usage >= 90 or remaining < 1):
#     print("Warning: Data limit approaching")
# else:
#     print("No warning")

# pass_valid = input("Do you have a valid parking pass? (yes/no): ")
# visitor = input("Are you paying for visitor parking? (yes/no): ")
# full = input("Is the parking lot full? (yes/no): ")
# if (pass_valid == "yes" or visitor == "yes") and full == "no":
#     print("Entry allowed")
# else:
#     print("Entry denied")

# score = float(input("Enter academic score: "))
# attendance = float(input("Enter attendance percentage: "))
# if score >= 95 or (score >= 85 and attendance >= 75):
#     print("Scholarship eligible")
# else:
#     print("Scholarship not eligible")

# opened = input("Is the restaurant open? (yes/no): ")
# delivery = input("Does it deliver to your location? (yes/no): ")
# online = input("Is it accepting online orders? (yes/no): ")
# if opened == "yes" and delivery == "yes" and online == "yes":
#     print("Order can be placed")
# else:
#     print("Order cannot be placed")

# motion = input("Is motion detected? (yes/no): ")
# door = input("Is the main door open? (yes/no): ")
# armed = input("Is the security system armed? (yes/no): ")
# if armed == "yes" and (motion == "yes" or door == "yes"):
#     print("Security alert activated")
# else:
#     print("No security alert")

age = int(input("Enter your age: "))
days = int(input("Enter trip duration in days: "))
covered = input("Is the country covered by insurance? (yes/no): ")
excluded = input("Is the destination currently excluded? (yes/no): ")
if age >= 18 and age <= 65 and days <= 30 and covered == "yes" and excluded == "no":
    print("Eligible for travel insurance")
else:
    print("Not eligible")