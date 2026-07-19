from loguru import logger

# Given:
numbers = [10, 15, 20, 25, 30, 35]
# Without using max() or sort(), find the largest number.

# Expected Output
# 90

# Tests:

# List traversal
# Variables
# Comparison operators


current = numbers[0]

for i in numbers:
    if i < current:
        current = i
print(current)





# # count of even number and also the odd count nuumbers
# count = 0

# for i in numbers:
#     if i%2==0:
#         count = count +1
# print(count)


# curr = 0
# for i in numbers:
#     if i%2==1:
#         curr = curr +1
# print(curr)
    

# num = [10,15,20,25,30]

# total = 0 

# for i in num:
#     if i %2 ==0:
#         total = total +i
# print(total)

# num_1 = [10, 15, 22, 7, 30, 18]


# largest = num_1[0]

# for i in num_1:
#     if i%2==0:
#         if i > largest:
#             largest = i
# print(largest)



# num_2 = [10, 15, 22, 7, 30, 18, 5]

# smallest = num_2[0]

# for i in num_2:
#     if i%2==1:
#         if i< smallest:
#             smallest = i
# print(smallest)

    

lst = [202,165,89,76,12]

num_insert = 15

new_lst = []

for i in lst:
    if i > num_insert:
        new_lst  = i + num_insert
print(new_lst)