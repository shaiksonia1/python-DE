from loguru import logger

# Dictionaries

#  create a dictionary
data = {"shaik":300,"sonia":500,"ali":800,"ayaan":900}
# access with keys 
print(data["ali"])

# to update the dictionary 
data["raja"]=400
print(data)

# this will print only keys from dict
print(data.keys())  
# this  will print only values from dict 
print(data.values())
# this will print both keys and values from dict 
print(data.items())


# Print all the keys using a for loop.
student = {
    "name": "Sonia",
    "age": 23,
    "city": "Hyderabad"
}


for key in student:
    print(key)


for key in student:
    print(key,student[key])


# Print only the subjects whose marks are greater than 80.
marks = {
    "Math": 90,
    "Science": 75,
    "English": 88,
    "Physics": 65
}

for i in marks:
    if marks[i]>80:
        print(i)


students = {
    "A": 90,
    "B": 45,
    "C": 78,
    "D": 32,
    "E": 88
}

# Using .items(), print:

# A -> Pass
# B -> Fail
# C -> Pass
# D -> Fail
# E -> Pass


for key,value in students.items():
    if value>=50:
        print(key,"->" "Pass")
    else:
       print(key,"->","fail") 





fruits = {
    "Apple": 10,
    "Banana": 5,
    "Orange": 12,
    "Mango": 3,
    "Grapes": 8
}
# Print only the fruits whose quantity is less than 8.

for key,value in fruits.items():
    if value<8:
        print(key)


scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}

# Find who has the highest score.


curr = 0

for key,value in scores.items():
    if curr > value:
         value = value +1
print(key,value)



sentence = "apple banana apple mango banana apple orange"

# convert this into a dict like this
# # {
#     "apple": 3,
#     "banana": 2,
#     "mango": 1,
#     "orange": 1
# }
new = sentence.split(" ")
print(new)
new_dict = {}




for word in new:
    if word in new_dict:
        new_dict[word] = new_dict[word] + 1
    else:
        new_dict[word]=1
print(new_dict)


students = {
    "Rahul": 75,
    "Priya": 90,
    "Ankit": 65,
    "Neha": 82
}

# Create a new dictionary that contains only the students who scored 80 or more.


new_dictionary = {}


for key,values in students.items():
    if values>80:
        new_dictionary[key] = values
        
print(new_dictionary)



colors = ["red", "blue", "red", "green", "blue", "red"]

new_colors = {}

for key in colors:
    if key in new_colors:
        new_colors[key]=new_colors[key] +1
    else:
        new_colors[key] = 1
print(new_colors)



# dictionary methods

# get
# pop
# update
# keys
# values


new_students = {
    "Rahul": 75,
    "Priya": 90,
    "Ankit": 65,
    "Neha": 82
}

new_students.update({"Sonia": 100})

logger.info(new_students.get("Rahul"))
logger.info(new_students.keys())
logger.info(new_students.values())



logger.info(new_students.items())


# dictionary comphrension



marks = {
    "Math": 90,
    "Science": 75,
    "English": 88,
    "Physics": 65
}

for i in marks:
    if marks[i]>80:
        print(i)
