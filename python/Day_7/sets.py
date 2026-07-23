# sets 
from loguru import logger


set_variable = set()
# empty set
print(type(set_variable))



a = {23,23, 1,2,3,4,4,5,1,3,5,2,4,6,}

print(a)

for i in a:
    print(i)


# methods

set1 = {1,2,8,7,4,12}
set2 = {2,4,6,5,15}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.isdisjoint(set2))

set1.add(45)

print(set1)


list1 =[1,2,3,4,5,6]
list2 = [4,5,6,7,8]

set3 = set(list1)
set4 =set(list2)

new_list_1 = (set3.difference(set4))
new_list_2 = (set4.difference(set3))
print(list(new_list_1))
print(list(new_list_2))