# # conditional operators
from loguru import logger

# var = int(input("Enter length of land: "))

# logger.info(f"var is: {var}")


# if (var < 100):
#     logger.info("Length of land is less than 100")  

# elif (var >= 500):
#     logger.info(f"Length of land is greater than 500, can't construct home")
# else:
#     logger.info("length of land is fine we can proceed with construction")


# age = int(input("Enter your age: "))


# if (age<18):
#     logger.info("You are not eligible to vote")
# elif(age>=18 and age<60):
#     logger.info("You are eligible to vote")
# else:
#     logger.info("You are not eligible to vote")





# positive_number = int(input("Enter a number: "))


# if (positive_number >0):
#     logger.info("You have entered a positive number")
# elif(positive_number<0):
#     logger.info("You have entered a negative number")
# else:
#     logger.info("You have entered zero")



num = int(input("Enter a number: "))


if (num % 2 == 0):
    logger.info("You have entered an even number")
elif (num%2 !=0):
    logger.info("You have entered an odd number")
