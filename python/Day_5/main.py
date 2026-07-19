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
    