############################
#Code: Matrix.py 
#Author:Madison G Austin

#Lab assignment 7- this assignment is making a list 
#that represents the maxrix and the out put of the nested loops

#Example used:  python Matrix.py 
############################

import random 

matrix = [ [0,0,0,0,0] , [0,0,0,0,0] , [0,0,0,0,0] , [0,0,0,0,0] , [0,0,0,0,0] ]

rows = 0
columns = 0

print("All zeros:")
print()
for rows in matrix:
    for y in rows:
        print( y , end=" ")
    print()
    

for rows_index in range(len(matrix)):
    for colums_index in range(len(matrix)):
        matrix[rows_index] [colums_index] = 150 * random.random() #this will stack the rows
print()

print("messy output:")
print()
for rows in matrix:
    for y in rows:
        print( y , end=" ")
    print()
print()

print("clean output:")
print()
for rows in matrix:
    for y in rows:
        print(f"{ y:> 8.2f}" , end="")
    print()