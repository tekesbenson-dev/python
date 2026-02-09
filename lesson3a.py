#Boolean - This is  a data type that evalutes either true or false

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))


#comparison operators - they are used to compare two or more statements and they ususally return a boolean answer

number1 = 2
number2 = 5

print("is number1greater than number2?",number1> number2)
print("is number1 less than number2?",number1< number2)
print("is number1  greater than or equal to number2?" ,number1>=number2)
print("is number1  less  or equal to number2?" ,number1>=number2)
print("is number1 equal to number2?" ,number1=number2)

#logical operators
#logical AND
#It returns true if and only if the condition/statement evaluates to true
print((3 > 1) and (7 > 6))

#logical or
#it evaluates to true if one of the statement/comdition is true
print((3>1) or (7 < 6))

#logical not
#it is used to nagete a statement/condition
print(not(90 > 70))
