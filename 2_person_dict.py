person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

# print out the name of the second child
list_of_children = person["children"]               #this one we just made a list before we called it
print(type(list_of_children))

print(list_of_children[1])    

print(person["children"][1])                        #how to do it in one line of code

# print out the name of the cat

print(person['pets']['cat'])

# use a loop to print out the names of each child

list_of_children = person["children"]

for child in list_of_children:                  #this does the exact same thing was the for loop below it
    print(child)

for child in person['children']:
    print(child)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for pet in person['pets']:
    print(f"The type of pet is {pet} and the name of the pet is: {person['pets'][pet]}")

for i, j in person['pets'].items():     #item method
    print(f"The type of pet is {i} and the name of the pet is: {j}")        #this is a lot simpler
