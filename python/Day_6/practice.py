# practice questions

# 1. Write a Python program to print "Hello Python".


print("Hello World")

# 2. Write a Python program to do arithmetical operations addition and division.
# Explanation:
# This program performs addition and division on two numbers.
# Logic:
#  Take two numbers as input.
#  Perform addition using the + operator.
#  Perform division using the / operator.


var_1 = int(input("enter a number "))
var_2 = int(input("enter a number "))

print(var_1 + var_2)
print(var_1 / var_2)



# 3. Write a Python program to nd the area of a triangle.
# Explanation:
# This program calculates the area of a triangle using the formula:
# Area=1/2×base×height
# Logic:
#  Take base and height as input.
#  Use the formula to calculate the area.


base = float(input("enter a the base value"))
height = float(input("enter the height value"))

area = (1 / 2) * base * height

print(f"Area is : {area}")