############################
#Code:HelloArgs.py
#Madison G Austin
#Lab assignment 2
############################

import sys

step1 = int(sys.argv[1])
flight2 = int(sys.argv[2])
height3 = float(sys.argv[3])

print("Total steps:", step1 * flight2)
print("Total height in feet:", step1 * flight2 * height3)