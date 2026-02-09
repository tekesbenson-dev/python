#loops -->  sometimes we may need to do a piece of work a number of times, in such cases we may use loops.
#a loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
#ther are two types of lops in python i.e the the for loop and while loop

#below is the syntax of a for loop in python:
"""
for variable in range(n):
    #block of code to be executed
"""



for greeting in range(5):
    print("Hello Benson")



    for number in range(10,20):
        print(number)



#print numer in the range of 50 to 70
for number in range(50, 71, 2):
    print (number)



print('=================')
#create a python that program that prints the odd numbers from 100 to 150
for number in range(101 ,150,2):
    print(number)


# create a program that prints the multiples of 3 starting from 201 to 150
for number in range(201,150,-3):
    print(number)
# create a python program that prints the leap years in between 2000 and 2024
for years in range(2000 ,2024, 4):
    print(years)