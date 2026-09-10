############################
#Code: Password.py
#Author:Madison G Austin

#Lab assignment 7- this assignment is making a challenged system for a "shoulder surfer" 
#so they have a harder time to find the password they want

#Example used:  python Password.py (hardcode/pin: 34576)
############################

import sys
import random

pin = [3,4,5,7,6]
randnums = [random.randint (1,3) for x in range(10)]
passwor = True

print("pin:0 1 2 3 4 5 6 7 8 9")
print("Num" , *( i for i in randnums))
passw = str(input("please enter your converted password: "))

for i in range (len(pin)): #this will make sure its in the length of the pin
    if int(passw[i]) != randnums[pin[i]]:
        passwor = False
        break
    else:
        pass #this will skip to the next part of the code
        
if  passwor == True:
    print("welcome! you are correct")
else:
    print("Sorry, you are incorrect")