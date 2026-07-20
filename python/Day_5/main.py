#  while loops 

from loguru import logger

# print 1 to 5 numbers using while loop


init_var = 1

while (init_var < 6):
    logger.info(init_var)
    init_var = init_var +1 



# Print even numbers from 2 to 10 using a while loop.


var = 2

while ( var<=10):
    logger.info(var)
    var = var +2

    
v = 10 
while (v>=2):
    logger.info(v)
    v = v-2
    

# Print numbers from 7 to 15.


i = 7
while(i<=15):
    logger.info(i)
    i = i + 1


# Print numbers from 20 down to 10.

i = 20
while (i>=10):
    logger.info(i)
    i = i-1


# Print all odd numbers from 1 to 19.


i = 1
while(i%2 == 1 and i <=19):
    logger.info(i)
    i = i+ 2


i = 1
sum = 0

while(i<=19):
    logger.info(i)
    sum = sum + i
    i = i+2
print(sum)