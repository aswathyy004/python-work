# numbers = [10, 5, 25, 8, 15] 
# largest = numbers[0]
# for number in numbers:
#     if number > largest :
#         largest = number
# print(f"largest element is {largest}")  

# numbers = [10, 5, 25, 8, 15] 
# smallest = numbers[0]
# for number in numbers:
#     if number < smallest:
#         smallest = number
# print(f"smallest element is {smallest}")        

# numbers = [1, 2, 3, 4, 5] 
# sum = 0
# for n in numbers:
#     sum+=n
# print("sum:", sum)    

# numbers = [10, 20, 30, 40, 50] 
# n = len(numbers)
# sum = 0
# for num in numbers:
#     sum+=num
# average = sum // n   
# print("average:",average) 

# numbers = [1, 2, 3, 4, 5]
# # print(numbers[::-1]) 
# reverse = []
# for num in numbers:
#     reverse.insert(0,num)
# print(reverse)    

# numbers = [1, 2, 2, 3, 4, 4, 5] 
# nope = []
# for num in numbers:
#     if num not in nope:
#         nope.append(num)
# print(nope)        
    
# numbers = [10, 20, 50, 40, 30] 
# numbers.sort()
# print("second largest:", numbers[-2])

# numbers = [1, 2, 3, 4, 5, 6] 
# even=[]
# odd=[]
# for num in numbers:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("even:",even)
# print("odd:",odd)           

# list1 = [1, 2, 3, 4, 5] 
# list2 = [3, 4, 5, 6, 7] 
# common = []
# for num in list1:
#     if num in list2:
#         common.append(num)
# print("common:",common)        

# list1 = [1, 2, 3] 
# list2 = [3, 4, 5] 
# merge = []
# for num in list1+list2:
#     if num not in merge:
#         merge.append(num)
# print(merge)        

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# sum = 0
# for row in matrix:
#     for num in row:
#         sum += num
# print("sum:", sum)

# matrix = [
#     [1, 2, 3],
#     [10, 5, 6],
#     [7, 8, 9]
# ]
# largest = matrix[0][0]
# for row in matrix:
#     for num in row:
#         if num > largest:
#             largest = num
# print("Largest element:", largest)