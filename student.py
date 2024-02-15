#Create a dictionary named student with the following key-value pairs:

#"name": Your Name
#"age": Your Age
#"major": Your Major
#"hobbies": A list of your top three hobbies
#Add a new key-value pair for "State": Your State of Residence

#Update the "age" to your current age + 1

#Write a loop to iterate over the key-value pairs in the student dictionary and print each pair on a new line in a well formatted way.

#create dictionary student
student = {"Name": "Leah Nelson", "Age": 20, "Major": "Marketing & MIS", "Hobbies": "Running, reading and hiking."}

#Add a new key-value pair for "State": Your State of Residence
student["State"] = "Minnesota"

#Update the "age" to your current age + 1
student["Age"] += 1

#Loop and print student information
print("\nSTUDENT INFORMATION:")
print('-' *20)
for key, value in student.items():
    print(f"{key}: {value}")