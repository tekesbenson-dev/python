# Python while loop.
#  While loop executes a block of code repeatedly as long as a certain condition is true. The syntax of a while loop in python is as follows:
"""
initilization of a variable
while keyword,
followed by the condition/statement to be evaluated,
followed by a full colon(:),
code to be printed out,
increment/decrement
"""

number = 0 
while number < 5:
    print("Hello Benson", number)
    number = number + 1

    print('===========')
    #create a python program that prints the even numbers from 50 to 70 using while loop
    # Print even numbers from 50 to 70 using a while loop

num = 50

while num <= 70:
    print(num)
    num += 2  # type: ignore