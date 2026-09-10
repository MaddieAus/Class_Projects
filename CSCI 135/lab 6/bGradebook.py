############################
#Code: bGradebook.py
#Author:Madison G Austin

#Lab assignment 6- we will be using the new style formatting to make a student grade book
#Example used:  python bGradebook.py
############################

import sys

grades = []

gradebook = str(input("who is this Gradebook for: "))
course = str(input("enter the type of course: ")) 

studentN = str(input("please enter students name: "))

while (True):
    assignment= str(input("enter assignment name (or quit to exit): "))
    if assignment == "quit":
        break
    else:
        grade = float(input("enter grade in assignment " + assignment +": "))
    grades.append(( assignment , grade ))

print ("--------------------------")
print("Gradebook for: " + gradebook )
print("Course: " + course )
print("Assignment         Grades")
print ("--------------------------")

for assignment, grade in grades:
    print("{:<12.12} {:>10.2f}%".format(assignment, grade))
    
average = sum(grade for _, grade in grades) / len(grades)

print ("--------------------------")
print("{:<12.12} {:>10.2f}%".format("Average", average))
