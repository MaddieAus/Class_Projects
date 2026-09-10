############################
#Code:Lottery.py
#Author:Madison G Austin

#Lab assignment 4- we will randomly genarate numbers to see if we won the lottery!
#Example used:  python Lottery.py 
############################

import random
import sys

userN1 = (int(sys.argv[1]))
userN2 = (int(sys.argv[2]))

lotteryN1 = random.randint (1,10)
lotteryN2 = random.randint (1,10)



print("the lottery numbers were", lotteryN1, "and", lotteryN2)
print("your picks were", userN1, "and", userN2)

if (userN1 == lotteryN1 and userN2 == lotteryN2) or (userN2 == lotteryN1 and userN1 == lotteryN2):
    print("You matched both numbers! Congratulations! you win $1000!!")
    
elif (userN1 == lotteryN1 or userN1 == lotteryN2) or (userN2 == lotteryN1 or userN1 == lotteryN2):
    print("You matched one number! You win $100!!")

else:
    print("sorry, no match") 