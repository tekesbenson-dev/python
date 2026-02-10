#functions with parameters
#paremeters: They are values that get passed as arguemnts given to a function 

def greeting(name):
    print(f"{name} How are you?hope you are fine.")

greeting("Benson")
print("============================") 

def message(names):
    print(f"Hello {names}. We sahll be having a general meeting on date......please avail yourself.")

message("Joy")
message("Benson")

print("==========================")
#create function that accepts parameters to add two numbers
def add_numbers(a, b):
    return a + b

# Example usage
result = add_numbers(5, 3)
print(result)