#Create a dictionary named student with the following key-value pairs:

#"name": Your Name
#"age": Your Age
#"major": Your Major
#"hobbies": A list of your top three hobbies
#Add a new key-value pair for "State": Your State of Residence

#Update the "age" to your current age + 1

#Write a loop to iterate over the key-value pairs in the student dictionary and print each pair on a new line in a well formatted way.

#create dictionary student
student = {"name": "Leah Nelson", "age": 20, "major": "Marketing & MIS", "hobbies": "Running, reading and hiking."}

#Add a new key-value pair for "State": Your State of Residence
student["State"] = ["Minnesota"]

#Update the "age" to your current age + 1
student["age"] + 1

#loop to iterate
for items in student.items():                         #items is a tuple
    print(items)
    #print(f"The key is {k} and the value is {v}")
