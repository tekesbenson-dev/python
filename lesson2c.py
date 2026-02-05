#A dictionary is a data type that stores data in items of key- value pair.
#It is iitroduced by the use of a dictionary can be of any data type.
#The values stored inside of a dictionary can be of many data type
#To access the values in a dictionary we use the keys

phonebook = {
    "Benson" : "254743600525",
    "Mary" :"254710369741",
    "Stephen" : "254782546978",
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

#print only benson's number
print(phonebook["Benson"])

print('==========')


player ={
    "name" : "Messi",
    "team" : ["PSG" ,"Barcelona" , "Argentina"]

}
#print barcelona - the second team he played for
print(player["team"][1])




