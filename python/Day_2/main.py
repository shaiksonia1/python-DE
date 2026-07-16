# python operators, type casting and input function


# operators are symbols that perform operations on values like addition, subtraction, multiplication, division, etc.

from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost = 5.5
labour_1 = "Mahesh"
labour_2 = "Ramesh"

is_home_constructed = False

perimeter_of_land = 2 * (length_of_land + breadth_of_land)
logger.info(f"Perimeter of land: {perimeter_of_land} ft")


# calculating area of land
area_of_land = length_of_land * breadth_of_land
logger.info(f"Area of land: {area_of_land} sq ft")

# modulo operator is used to get the remainder of a division operation
# Floor division removes the decimal part and gives the lower integer eg: 3.333 will be 3 
# celing operatot will round up the value to the nearest integer eg:3.333 will be 4 

# Floor = go down 
# Ceiling = go up 

num_1 = 10
num_2 = 3

logger.info(f"modulo: {num_1 % num_2}")
logger.info(f"math ceiling is: {math.ceil(num_1 / num_2)}")

logger.info(f"floor division: {num_1 // num_2}")



# concatenation
name_1 = "shaik"
name_2 = "sonia"

print(name_1 + " " + name_2)  # concatenation of two strings


# type casting
# converting one data type to another data type
# this is implicit type casting, python automatically converts the data type
number_1 = 10
number_2 = 20.5

print(number_1 + number_2)  # adding int and float will give float


# this is explicit type casting, we are converting the data type manually

# print(int(number_2))  # converting float to int will give 20
print(number_1 + int(number_2))  # adding int and int will give int

length_of_land = input("Enter the length of land: ")
breadth_of_land = input("Enter the breadth of land: ")  
total_area_of_land = int(length_of_land) * int(breadth_of_land)
print(f"total_area_of_land: {total_area_of_land} sq ft")