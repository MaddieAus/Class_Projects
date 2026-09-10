############################
#Code: CaesarChiffer.py
#Author:Madison G Austin

#Lab assignment 8- this assignment we will use 
#the caesercipher algorithm to encrypt and decrypt a string

#Example used:  python CaesarChiffer.py 
############################

import sys

def menu():
    print("*************************")
    print("Menu:")
    print("C: clear string")
    print("S: set new shift")
    print("E: Encrypt")
    print("T: set new text")
    print("Q: Quit")

#functions and variables######################################################
originalL=[]
encryptL=[]
shift = 0    

while True:
    menu()
    choice = input("enter menu item: ")

    match choice:
        case "c" | "C" :
            #clear string####################################################
            originalL= []
        case "s" | "S":
            #set new shift###################################################
            shift = int(input("Enter new shift : "))
        case "e" | "E" :
            #encrypt#########################################################
            i=0
            n= len(originalL)
            while(i<n):
                char=originalL[i]
                if 'a' <= char <= 'z' :
                    newchar= chr ( (ord(char) - ord('a') + shift) % 26 + ord('a'))
                elif 'A' <= char <= 'Z' :
                    newchar= chr ( (ord(char) - ord('A') + shift) % 26 + ord('A'))
                encryptL.append(newchar)
                i = i + 1
        case "t" | "T" :
           #set new text###################################################
            newtext = input("Enter a string (max 30 characters): ")[:30] 
            originalL= list(newtext)
        case "q" | "Q" :
            #quit##########################################################
            break
        case _: #this is a error message###################################
            print("invalid input. please try again")
    print(f'******************************\n Original string: {"".join(originalL)} \n Your shift = {shift} \n Encrypted text: {"".join(encryptL)} ')