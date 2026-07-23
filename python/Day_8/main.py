# strings

name = "    sonia shAik"

counter = 0
for char in name:
    print(counter,char)
    counter = counter +1


name1 = "sHaik"

print(name1.capitalize())
print(name.count("a"))


# ASCII VALUES HAS DIFFERENT FOR A-Z AND a-z


print(ord("A")) 
# 65 
print(ord("a"))
# 97

print(chr(65))

# gives true or false 
print(name1.endswith("a"))
print(name1.endswith("k"))


print(name1.islower())

print(name1.upper())

new_name = name.replace("sonia","ayaan")
print(new_name)



print(len(name.strip()))


email = "ab@gmail.com"

new_email = email.split("@")
print(new_email)

username = new_email[0]



print(username[0]+"*" * (len(username) - 2) + username[-1]+"@" + new_email[1])
