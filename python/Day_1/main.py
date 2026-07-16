
labour_1st = "Mahesh"
labour_2nd = "Ramesh"
labour_3rd = "Suresh"
labour_4th = "Naresh"



print(type(labour_1st))
print(id(labour_2nd))

print("Labour 1st Name:", labour_1st)
print("Labour 2nd Name:", labour_2nd)
print("Labour 3rd Name:", labour_3rd)
print("Labour 4th Name:", labour_4th)


labour_1st_wage = 500
labour_2nd_wage = 600
labour_3rd_wage = 700
labour_4th_wage = 800

print(type(labour_1st_wage))
print(id(labour_2nd_wage))

print(f"Labour 1st Wage: {labour_1st_wage}")
print(f"Labour 2nd Wage: {labour_2nd_wage}")
print(f"Labour 3rd Wage: {labour_3rd_wage}")
print(f"Labour 4th Wage: {labour_4th_wage}")


print(f"""Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here.""")


import logging

logging.basicConfig(
    filename="logfile.log",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s"
)


logging.info(f"print({labour_4th_wage})")

# var = hello if varibale is not defined then it will give "Name error"