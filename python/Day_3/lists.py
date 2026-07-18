# Lists

#  List is a collection of same or diferent data types. It is mutable and ordered collection of items. It is defined by using square brackets [].

from loguru import logger


list_1 = ["shaik","sonia","ayaan","ali"]

logger.info(f"list_1 is: {list_1}")

logger.info(f"list_1 first element is: {list_1[0]}")



# Methods of list
# append() - adds an element to the end of the list
# insert() - adds an element at a specific index
# extend() - adds multiple elements to the end of the list
# pop() - removes an element from the list

list_2 = [5,"hello", 20.5, True]

list_1.append(list_2)

logger.info(f"list_1 after appending list_2 is: {list_1}")
logger.info(f"inserting the list at index 1:{list_1.insert(1,list_2)}")
logger.info(f"extending the list with list_2:{list_1.extend(list_2)}")


# multidimensional list - a list of lists

multi_list = [[1,2,3,4],[1,2,35,6]]

logger.info(f"multi_list is {multi_list[0]}")



# Adding 2 lists 

names_1 = ["shaik","sonia","ayaan","ali"]
names_2 = ["kareem","sana","zoya"]


all_names = names_1 + names_2

logger.info(f"all_names is: {all_names}")

# this is the alternative way to add 2 lists instead of using extend() method
 


#  accessing list using : slicing method

logger.info(f"slicing method:{names_1[2:]}")
logger.info(f"slicing method:{names_1[:3]}")
# reversre the list using slicing method
logger.info(f"reverse the list:{names_1[::-1]}")

logger.info(f"lenght of the lis is :{len(names_1)}")



logger.info(f"pop method is used to remove the last element of the list:{names_1.pop(2)}")

print(names_1)


