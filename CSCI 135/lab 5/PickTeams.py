############################
#Code:PickTeams.py
#Author:Madison G Austin

#Lab assignment 4- using the strings and loops to make teams using the users input
#Example used:  python PickTeams.py 
############################

import sys

print("Pick and setup your teams")
print("-----------------------------------------------")
numteam = int(input("how many teams are there?: "))
report= ""


print("-----------------------------------------------")
print("Please enter a team name when prompted. Then enter player names for that team.")
print("When done entering player names for that team, type done.")
print("-----------------------------------------------")

if numteam < 2 or numteam > 10:  #this shows that there can't be less then 2 and more then 10
    exit("Please eneter between 2 and 10 teams") #this exit will still print the error
       
for i in range(numteam): #the range is the numteam
   teamname= str(input("Please enter the name of Team " + str(i + 1) + ":" ))
   
   report+= "\n-----------------------------------\n"
   report+= "Team #" + str(i + 1) + ": "+ teamname + "\n"
   report+= "-----------------------------------\n"
   count = 0 #the count of the players
   while(1):
        nameplay = str(input("please enter the name of a player for team " + str(teamname) + ":"))
        if nameplay == 'done':
            break
        else:
            count+= 1
            report+= "player #" + str(count) + ": "+ nameplay + "\n"
   report+= "-----------------------------------\n"       
print(report)