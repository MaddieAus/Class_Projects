############################
#Code:Shipping.py
#Author:Madison G Austin

#Lab assignment 4- calculating how much money it will be for shipping
#Example used:  python shipping.py 50
############################

import sys

maxweight=100
basecharge=15
subcharge=5
morethen=30
cost=0

package = (float(sys.argv[1]))

if  package > maxweight:
    print("the package weighs over 100 pounds and cannot be shipped")
    
elif 70 > package > 2:
    cost= basecharge + ((package - 2) * 5)
    print("it will cost", "$",cost , "to ship your package")
elif package > 70 :
    cost= ((package - 2) * 5) + morethen
    print("it will cost", "$",cost , "to ship your package")
    
elif package <=2:
    cost= basecharge
    print("it will cost", "$",cost , "to ship your package")