############################
#Code:GradingFuntions.py 
#Author:Madison G Austin

#Lab assignment 9- this code will use functions to grade students assignments
#Example used:  python GradingFuntions.py 
############################

import sys

cutoffs = [100, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0] 
letterGrades = ['A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
report= ""

def printGradingScale():###prints scale###
    print("Percent Range  Letter Grade")
    print("-------------  ------------")
    for i in range(len(cutoffs) -1):
        low = cutoffs[i + 1]
        high = cutoffs[i]
        if low < 60:
            print(f"below {high}%  {letterGrades[i]}")
        else:
            print(f"{low} to {high}% {letterGrades[i]}")
            
def getGradeByScore(score):###gives letter grade according to score from (0.0 to 1.0)###
    percentage = score * 100
    for i in range(len(cutoffs) -1):
        if cutoffs[i + 1] <=percentage <=cutoffs[i]:
            return letterGrades[i]
        return 'f'
    
def getGradeByScores(scores):###gives letter grade acoording to average###
    average= sum(scores) / len(scores)
    return getGradeByScore (average)
    
def getGradeByPoints(pointsEarned, pointsPossible):###gives grade based on points earned and possible###
    total_Earned= sum(pointsEarned)
    total_Possible= sum(pointsPossible)
    overall= total_Earned / total_Possible if total_Possible > 0 else 0
    return getGradeByScore(overall)
    
def getGradeRange(strGrade):###gives grade range according to letter grade###
     if strGrade in letterGrades:
        index = letterGrades.index(strGrade)
        return (cutoffs[index + 1], cutoffs[index])
     return None #if grade isn't valid
     
# here is example test code if you wish to use!
# printGradingScale()
#print(getGradeByScore(0.9))
# print(getGradeByScores([0.95, 0.8, 0.85]))
#print(getGradeByPoints([8, 9, 15], [10, 10, 20])
# print(getGradeRange('B+'))