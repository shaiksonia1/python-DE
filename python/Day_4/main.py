# loops
# for loop - used to iterate over a sequence (list, tuple, dictionary, set, or string)



from loguru import logger


names = ["shaik","sonia","ayaan","ali"]

# for name in names:
#     logger.info(f"names are: {name}")


for i in range(len(names)):
    logger.info(f"name {i+1}: {names[i]}")


for i in range(5):
    print("* " * (i+1))


for i in range(1,101):
    if i%2==0 :
        logger.info(f"even numbers are: {i}")


for i in range(6,1, -1):
    logger.info((i*1-1) * "* ")




