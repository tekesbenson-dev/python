#Python lists
#A list in python is a collection of items that are ordered in a certain way.
#A list is introduced by the use of the square brackets[]
#The items of a list are stored inside pf indexes.In programming we start counting from iindex zero.
#A list is mutable i.e the contents of  a list can be changed
cars=["BMW", "Benze", "Hiance", "Prado", "Probox", "MacLarren"]
print(cars)

#Accessing items of a list
print(cars[2])
print("The car on index four is: ",cars[4])

#list slicing- This is creating a list from a given a given bigger list
print(cars[4:])

#printing from index zero index three
print(cars[:4])

#printing cars from hiance to probox
print(cars[2:5])

#list -Mutability
#we use append to add an item at the end of the list
cars.append("Mercedes")
print(cars)

cars.append("subaru")
print(cars)

#we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

#we can use an index to add item in a list
cars[5] = "pajero"
print(cars)

#we can use the sort function to sort items in alphabetical order
cars.sort()
print(cars)


# we can use the sort function to sort out items in alphabetical order
cars.sort(reverse=True)
print(cars)
del cars[4]
print(cars)
cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)