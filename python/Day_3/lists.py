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

list_2 = [5,"hello", 20.5, True]

list_1.append(list_2)

logger.info(f"list_1 after appending list_2 is: {list_1}")


# multidimensional list - a list of lists

multi_list = [[1,2,3,4],[1,2,35,6]]

logger.info(f"multi_list is {multi_list[0]}")