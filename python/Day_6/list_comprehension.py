number_list = [1,2,3,4,5,6,7,8,9,10]

new_list = []

for i in number_list:
    if i%2==0:
        new_list.append(i)
print(new_list)

# in list comprehension it becomes in 1 line 

new_list = [i for i in number_list if i%2==0]

print(new_list)



for i in number_list:
    if i%2==0:
        new_list.append("even")
    else:
        new_list.append("odd")
print(new_list)


new_list = ["even"if i%2==0 else "odd" for i in number_list]

print(new_list)


list_1 = [1,2,3,4,5,6,7,8,9,10]

q_list = [i for i in list_1]

print(q_list)


# Create a list containing only the words with more than 3 characters.
words = ["apple", "bat", "cat", "elephant", "dog"]

new_words = []
for i in words:
    if len(i) > 3:
        new_words.append(i)

print(new_words)


new_words = [i  for i in words if len(i)>3]
print(new_words)


words_1 = ["python", "java", "sql", "spark"]
new_words_1 = []
# Convert only the words longer than 4 characters to uppercase.


for i in words_1:
    if len(i)>4:
        new_words_1.append(i.upper())
print(new_words_1)


new_words_1 = [i.upper() for i in words_1 if len(i)>4]
print(new_words_1)