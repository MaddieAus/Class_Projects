############################
#Code: aGradebook.py
#Author:Madison G Austin

#Lab assignment 6- we will be using the old style formatting to make a student grade book
#Example used:  python aGradebook.py
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
    print("%-12s %10.2f%%" % (assignment, grade))
    
average = sum(grade for _, grade in grades) / len(grades)

print ("--------------------------")
print("%-12s %10.2f%%" % ("Average", average))