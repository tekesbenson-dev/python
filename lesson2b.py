#Tuple
#A tuple is an imutable type of a list meaning it cannot change
#to introduce tuple we use parethensis()

counties = ("Nairobi" , "Mombasa" , "Eldoret" , "Kajiado" , "Nakuru" , "Eldoret")
print(counties)
print(type(counties))

#slicing tuples
print(counties[3:])

#accessing items of a type by use of the indexes
print(counties[5:])

#Note: Below will generate an error
#Attribute error
counties.append("Machakos")
print(counties)