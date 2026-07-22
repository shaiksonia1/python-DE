# tuples 


# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.


from loguru import logger


# test_tuple = ("shaik",677,90,89,True,"sonia")
# logger.info(f"{test_tuple}")

# logger.info(type(test_tuple))


# # test_tuple[2]=900
# # print(test_tuple)

# print(test_tuple[1:5])
# print(test_tuple[:6])

# test_tuple_1 = ([45,5,6,7],["sonia","shaik"],[77.99,89])
# # output:(45,5,6,7,"sonia","shaik",77.99,89)

# result =()

# for lists in test_tuple_1:
#     new_var = tuple(lists)
#     result = result + new_var
# print(result)


# tuple1 = (10,2,3,5)
# tuple2 = (3,6,4,3)
# final_tuple = ()

# for i in range(len(tuple1)):
#     result = tuple1[i] ** tuple2[i]
#     final_tuple = final_tuple + (result,)
# print(final_tuple)


# numbers = (10, 20, 30, 40, 50)

# # Print each element using a loop.

# for i in numbers:
#     print(i)


# fruits = ("apple", "banana", "mango", "orange")

# # Count how many fruits are in the tuple without using len().

# # Hint: Use a counter variable.


# counter = 0

# for i in fruits:
#     counter = counter+1
# print(counter)


names = ("Sonia", "Rahul", "Priya", "Ankit")

# Print each name along with its index.


for i in enumerate(names):
    print(i)