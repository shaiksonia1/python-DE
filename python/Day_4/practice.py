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





# count of even number and also the odd count nuumbers
count = 0

for i in numbers:
    if i%2==0:
        count = count +1
print(count)


curr = 0
for i in numbers:
    if i%2==1:
        curr = curr +1
print(curr)
    