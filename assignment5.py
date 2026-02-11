# ASSIGNMENT TASKS – FUNCTIONS, LOOPS & CONTROL STATEMENTS

# Qn 1: Function Without Parameters
# Calculates and prints the area of a rectangle
def area_of_rectangle():
    length = 10
    width = 5
    area = length * width
    print("Area of the rectangle:", area)

area_of_rectangle()


print("\n------------------------\n")

# Qn 2: Function With Parameters
# Returns sum, difference, product, and division
def arithmetic_operations(a, b):
    sum_ = a + b
    difference = a - b
    product = a * b
    division = a / b if b != 0 else "Cannot divide by zero"

    return sum_, difference, product, division

results = arithmetic_operations(20, 5)
print("Sum:", results[0])
print("Difference:", results[1])
print("Product:", results[2])
print("Division:", results[3])


print("\n------------------------\n")

# Qn 3: Control Statement (if...elif...else)
# Checks whether a number is positive, negative, or zero
def check_number():
    number = int(input("Enter a number: "))

    if number > 0:
        print("The number is Positive")
    elif number < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")

check_number()


print("\n------------------------\n")

# Qn 4: Loop with Arithmetic
# Calculates the sum from 1 to n using a for loop
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum from 1 to", n, "is:", total)

sum_to_n(10)


print("\n------------------------\n")

# Qn 5: While Loop
# Calculates squares of numbers from 1 up to a given number
def square_numbers():
    num = int(input("Enter a number: "))
    i = 1

    while i <= num:
        print("Square of", i, "is:", i * i)
        i += 1

square_numbers()