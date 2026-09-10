############################
#Code:Zodiac.py
#Author:Madison G Austin

#Lab assignment 4- this code when enterd your birth year will give you your chinese zodiac
#Example used:  python Zodiac.py
############################

import sys

year = (int(sys.argv[1]))

if(year % 12) == 0:
    print(" you were born in the year of the monkey")
    
elif (year % 12) == 1:
     print(" you were born in the year of the rooster")
     
elif (year % 12) == 2:
    print(" you were born in the year of the dog")
    
elif (year % 12) == 3:
    print(" you were born in the year of the pig")
    
elif (year % 12) == 4:
    print(" you were born in the year of the rat")
    
elif (year % 12) == 5:
    print(" you were born in the year of the ox")
    
elif (year % 12) == 6:
    print(" you were born in the year of the tiger")
    
elif (year % 12) == 7:
    print(" you were born in the year of the rabbit")
    
elif (year % 12) == 8:
    print(" you were born in the year of the dragon")
    
elif (year % 12) == 9:
    print(" you were born in the year of the snake")
    
elif (year % 12) == 10:
    print(" you were born in the year of the horse")
    
elif (year % 12) == 12:
    print(" you were born in the year of the sheep")