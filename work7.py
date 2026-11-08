# marks=[] 
# for i in range(5):
#     mark=int(input("Enter marks of students: "))
#     marks.append(mark)
# print("Mark List: ",marks)
# highest_mark=max(marks)
# lowest_mark=min(marks)
# print(f"Highest mark: {highest_mark}")  
# print(f"Lowest mark: {lowest_mark}")   
# count=0  
# for mark in marks:
#     if mark>50:
#         count+=1
# print("Students scoring above 50:", count)

# numbers=[]  
# for i in range(10): 
#     number=int(input("enter 10 numbers: "))
#     numbers.append(number)  
# print("Numbers:",numbers)   
# list1=[]   
# for number in numbers: 
#     if number%2==0: 
#         list1.append(number)  
# list2=[] 
# for number in numbers:   
#     if number%2!=0:   
#         list2.append(number) 
# print(f"even numbers: {list1}")
# print(f"odd numbers: {list2}") 

# numbers=[]
# for i in range(10):
#     number=int(input("enter 10 numbers:"))  
#     numbers.append(number) 
# print("numbers:", numbers)  
 
# pos_count = 0
# neg_count = 0
# zero_count = 0
# for num in numbers: 
#     if num>0:  
#         pos_count+=1 
#     elif num<0:
#         neg_count+=1
#     else:
#         zero_count += 1
# print("positive numbers count:",pos_count) 
# print("negative numbers count: ",neg_count)
# print("zeroes count:",zero_count)
# list=[]
# for i in range(5):
#     number=int(input("enter 5 numbers: "))
#     list.append(number)
# print("numbers:",list)
# search_num=int(input("enter the number to be searched: "))

# if search_num in list:
#     print("number is in the list at position",list.index(search_num))
# else:
#     print("number not in the list")


# # my_list = []

# # for i in range(5):
# #     number = int(input("enter 5 numbers: "))
# #     my_list.append(number)

# # print("numbers:", my_list)
# # search_num = int(input("enter the number to be searched: "))
# # if search_num in my_list:
# #     # Find all positions using enumerate
# #     positions = []
# #     for i, num in enumerate(my_list):
# #         if num == search_num:
# #             positions.append(i)
# #     print("number is in the list at positions:", positions)
# # else:
# #     print("number not in the list")


# prices=[]
# product=int(input("how many products you want to add: "))
# for i in range(product):
#     price=int(input("enter the price of the products: "))
#     prices.append(price)
# total=sum(prices)
# print("Total price:", total)
# if total>5000:
#     discount = total * 0.10
#     final_amount=total-discount
#     print("You got a 10% discount!")
#     print("Final amount to pay:", final_amount)
# else:
#     print("Final amount to pay:", total)

# number=[]
# for i in range(10):
#     enter=int(input("enter 10 numbers:"))
#     number.append(enter)
# print("Entered numbers: ",number)
# print("sum: ",sum(number))
# print("Average:",sum(number)/len(number))
# print("Largest number: ",max(number))
# print("smallest number: ",min(number))
# even_count=0
# even=[]
# for num in number:
#     if num%2==0:
#         even.append(num)
#         even_count+=1
# print("even numbers: ",even)
# odd_count=0
# odd=[]
# for num in number:
#     if num%2!=0:
#         odd.append(num)
#         odd_count+=1

# print("Number of even numbers:", even_count)
# print("Number of odd numbers:", odd_count)


# #if zeroes is included
# # zeros = []

# # for num in number:
# #     if num == 0:
# #         zeros.append(num)
# #         zero_count += 1
# #     elif num % 2 == 0:
# #         even.append(num)
# #         even_count += 1
# #     else:
# #         odd.append(num)
# #         odd_count += 1


# list1=[]
# numbers=int(input("how many numbers :"))
# for num in range(numbers):
#     number=int(input("enter the numbers:"))
#     list1.append(number)
# print("entered numbers: ",list1)
# positive=[]
# for num in list1:
#     if num > 0:
#         positive.append(num)
# if positive:
#     print("positive numbers:", positive)
# else:
#     print("no positive numbers")

# list1=[]
# for i in range(10):
#     numbers=int(input("enter the numbers: "))
#     list1.append(numbers)
# print("Entered numbers: ",list1)
# duplicates=[]
# for num in list1:
#     if list1.count(num)>1 and num not in duplicates:  #When you use .count(num) on a list like [10, 20, 10, 20], Python checks the entire list every single time.When the loop hits the first 10, Python sees it appears twice, so it adds 10 to your duplicates list.But when the loop reaches the second 10 later on, Python checks it again, sees it appears twice, and would add 10 a second time!
#         duplicates.append(num)
# print("Duplicate numbers: ", duplicates)


# # original = int(input("Enter a number: "))
# # temp = original
# # reversed_num = 0
# # while temp > 0:
# #     digit = temp % 10                      
# #     reversed_num = reversed_num * 10 + digit 
# #     temp = temp // 10                     

# # if original == reversed_num:
# #     print(original, "is a palindrome! 🎉")
# # else:
# #     print(original, "is not a palindrome.")

# user_input = input("Enter a number: ")
# reversed_input = user_input[::-1]
# if user_input == reversed_input:
#     print(user_input, "is a palindrome!")
# else:
#     print(user_input, "is not a palindrome.")

# n = int(input("Enter a number: "))
# temp = n
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum = sum + digit ** 3
#     n = n // 10

# if sum == temp:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number") 

n = int(input("Enter a number: "))
largest = 0
while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print("Largest digit:", largest)