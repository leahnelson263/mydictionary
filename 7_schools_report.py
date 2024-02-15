"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""


import json

infile = open('school_data.json', 'r')

#convert json to python
list_of_schools = json.load(infile)

#print(type(list_of_schools))

conference_schools = [372, 108, 107, 130]


#Grad rate for women
for school in list_of_schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if school["Graduation rate  women (DRVGR2020)"] >= 75:
            print('\n\n')
            print("University: ", school["instnm"])
            print("Graduation Rate for Women: ", school["Graduation rate  women (DRVGR2020)"], '%', sep='')


print('\n\n\n\n\n\n\n')
#Display report for all universities that have a total price for in-state students living off campus over $50,000


#in state living off campus
for school in list_of_schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        price = school["Total price for in-state students living on campus 2020-21 (DRVIC2020)"]
        if price is not None and price >= 50000:            
            print('\n\n')
            print("University: ", school["instnm"])
            print("Total price for in-state students living off campus: $", f'{school["Total price for in-state students living on campus 2020-21 (DRVIC2020)"]:,.2f}', sep='')


#Vanderbilt University also meets the criteria (but wasn't listed on the outcome picture)