#On the try and except block: You run some codes/statements and if it is succesful the try block will be executed other the except block will br executed when there is anticipated error.
try:
    number = 100
    answer = number / 0
    print("The answer is:", answer)
except Exception as e:
    print("There is an error :", e)

