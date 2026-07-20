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