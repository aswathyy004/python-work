python_students = {"Arun", "Megha", "Rahul", "Sneha"}
analytics_students = {"Sneha", "Rahul", "Aman", "Diya"}
print("Both Courses:", python_students & analytics_students)
print("Only Python:", python_students - analytics_students)
print("Only Data Analytics:", analytics_students - python_students)
print("All Students:", python_students | analytics_students)
print("Exactly One Course:", python_students ^ analytics_students)

customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
customer2 = {"Apple", "Vivo", "Oppo", "Samsung"}
print("Common Brands:", customer1 & customer2)
print("All Brands:", customer1 | customer2)
print("Only Customer 1:", customer1 - customer2)
print("Only One Customer:", customer1 ^ customer2)

design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"}
print("Common Tools:", design_team & marketing_team)
print("Design Team Only:", design_team - marketing_team)
print("All Tools:", design_team | marketing_team)
print("Only One Team:", design_team ^ marketing_team)

cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"}
football_fans = {"Nisha", "Rahul", "Ajay", "David"}
print("Both Sports:", cricket_fans & football_fans)
print("Only Cricket:", cricket_fans - football_fans)
print("Only Football:", football_fans - cricket_fans)
print("All Sports Fans:", cricket_fans | football_fans)

electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"}
accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"}
print("Common Products:", electronics & accessories)
print("Only Electronics:", electronics - accessories)
print("All Products:", electronics | accessories)
print("Only One Category:", electronics ^ accessories)

employee1 = {"Python", "Java", "SQL", "C"}
employee2 = {"Python", "JavaScript", "SQL", "Go"}
print("Common Languages:", employee1 & employee2)
print("Only Employee 1:", employee1 - employee2)
print("All Languages:", employee1 | employee2)
print("Only One Employee:", employee1 ^ employee2)

friend1 = {"Netflix", "Prime", "Hotstar", "SonyLiv"}
friend2 = {"Netflix", "Zee5", "Prime", "JioCinema"}
print("Common Subscriptions:", friend1 & friend2)
print("Only Friend 1:", friend1 - friend2)
print("All OTT Platforms:", friend1 | friend2)
print("Only One Friend:", friend1 ^ friend2)

available_products = {"Laptop", "Mouse", "Keyboard", "Monitor"}
sold_products = {"Mouse", "Monitor"}
available_products = available_products - sold_products
print("Remaining Products:", available_products)
print("Sold Products:", sold_products)
available_products.add("Printer")
available_products.remove("Keyboard")
print("Updated Available Products:", available_products)

music_event = {"Anu", "David", "Riya", "Sam"}
dance_event = {"Riya", "Sam", "Karthik", "John"}
print("Both Events:", music_event & dance_event)
print("Only Music:", music_event - dance_event)
print("Only Dance:", dance_event - music_event)
print("All Participants:", music_event | dance_event)

music_event = {"Anu", "David", "Riya", "Sam"}
dance_event = {"Riya", "Sam", "Karthik", "John"}
print("Both Events:", music_event & dance_event)
print("Only Music:", music_event - dance_event)
print("Only Dance:", dance_event - music_event)
print("All Participants:", music_event | dance_event)

campaign_A = {"user101", "user102", "user103", "user104"}
campaign_B = {"user103", "user104", "user105", "user106"}
print("Common Visitors:", campaign_A & campaign_B)
print("Only Campaign A:", campaign_A - campaign_B)
print("Total Unique Visitors:", campaign_A | campaign_B)
print("Only One Campaign:", campaign_A ^ campaign_B)

restaurant1 = {"Burger", "Pizza", "Fries", "Pasta"}
restaurant2 = {"Pizza", "Sandwich", "Pasta", "Momos"}
print("Common Food Items:", restaurant1 & restaurant2)
print("Restaurant 1 Only:", restaurant1 - restaurant2)
print("Restaurant 2 Only:", restaurant2 - restaurant1)
print("All Food Items:", restaurant1 | restaurant2)
print("Only One Restaurant:", restaurant1 ^ restaurant2)

