##################
# Madison Austin 
# CSCI 136 Lab 1 
# spell check
##################

#Task 
# 1. Read in a text file of correctly spelled words. Read the words into a list named wordlist.
#   • The text file is posted on Canvas. The filename is wordlist.txt.
# 2. Ask the user if they would like to check a word or a phrase.
# 3. Get the word or phrase from the user. You can expect the input to be a single word, or a phrase 
#    with words separated by spaces. The input will be free of digits, punctuation and special characters.
# 4. Search wordlist for the word, or each word in the phrase.
# 5. Output the word or words that are misspelled; otherwise output “The spelling is correct!”


print("Word check!")

def AOW_file(): #this opens and looks through the word file
    with open("words_alpha.txt", 'r') as file:
        AOW = [line.strip().lower() for line in file] #this makes it not uppercase sensitive
        return AOW #AOW means Alot Of Words lol

def Check_it(AOW, text): #this checks the spelling 
    words = text.strip().lower().split()
    misspelled = [word for word in words if word not in AOW] # i will be honest asked chatgpt for help on this to make it more compact (smaller)

    if misspelled:
        return " , " .join(misspelled) + "is misspelled" # i asked avrey the diffrence between .join and .append and decided the .join route
    else:
        return "The spelling is correct!"

def main_function():
    AOW = AOW_file() #brings file

    CheckingPoW= input("would you like to check a word or a phrase? (write word or phrase): ").strip().lower() #asking for userinput

    if CheckingPoW == "word": #this is for a word
        word = input("type word you want to spellcheck: ").strip()
        outputW = Check_it(AOW, word)
        print(outputW)
        
    elif CheckingPoW == "phrase": #this is for a phrase
        phrase = input("type phrase you want to spellcheck: ").strip()
        outputp = Check_it(AOW, phrase)
        print(outputp)

    else: #this is just a error message
        print("invalid input. Please write a 'word' or 'phrase'.")

main_function() #i looked at pach's assighnment he made me do for most of the help with it and then the links you provided