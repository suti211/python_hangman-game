import string

#picks and returns random elment of an "x" list
#usage : pick_a_word(listname)

def pick_a_word(x):
    import random
    the_word = (x[random.randrange(len(x))])
    return the_word

########################################################################################

# reads in a file into an array and returns that array.
# usage : my_List = loadInWords("Filename.txt")
def loadInWords(FILE):
    myFile = open(FILE, "r")
    array = myFile.read().split("\n")

    # removing empty lines from array
    i = 0
    while i < len(array):
        if array[i] == "":
            del array[i]
        else:
            i += 1

    myFile.close()
    return array

########################################################################################

# gets a word (x) counts the lenght of it and prints out the equal amounts of underscores and spaces between them
# usage : printUnderScores(wordname)
def printUnderScores(choosenWord, indexList, letters):

    if len(indexList) != 0:
       for i in indexList:
           letters[i] = choosenWord[i]

    for i in range(len(choosenWord)):
        print(str(letters[i]), end="")

    


########################################################################################

# asks a user for an imput and checks if that input is valid(alphabets and 1 character long) or not, if not it prints 
# that the caracters are not valid and asks the input again, if its valid it breaks out of the cycle
# gets two strings, and checks if the input occurs anywhere in those stringsm so the input cannot be used again.
# usage : call the function where u need it 
def getUserInput(correctString, incorrectString):
    while True:
        userInput = input("\nEnter a character: ")
        userInput = userInput.lower()
        alreadyUsed = False

        for i in range(len(incorrectString)):
            if incorrectString[i] == userInput:
                alreadyUsed = True
        
        for i in range(len(correctString)):
            if correctString[i] == userInput:
                alreadyUsed = True

        isAsciiLower = userInput in string.ascii_lowercase

        if len(userInput) == 1 and not userInput.isdigit() and alreadyUsed != True and isAsciiLower:
            break 
        else:
            print("You gave more than 1 character, or not a character.\nOr the character is already used!")
        
        
    return userInput

########################################################################################

# gets a character, and another word string as input,
# then returns on wich index the character appearn in the given word, in a list,
# returns -1 if the given char is not in the word
def checkTip(userInput, selectedWord):
   matchIndex = []
   for i in range(len(selectedWord)):
       if selectedWord[i] == userInput:
           matchIndex.append(i)
   return matchIndex

########################################################################################

# checks if the given list have any underscores in it
# if it has can be used to determine if the player guessed the word corectlys
def didTheUserWin(letterList):
    scoreCount = len(letterList)
    for i in letterList:
        if i != "_ ":
            scoreCount -= 1
    if scoreCount == 0:
        return True
    return False
    
        
                   
        


########################################################################################

# stores the pictures for hangman
# usage : hangmanPicsList(ahanyadik képet)
def hangmanPicsList(x):
    hangmanlist = ['''

   +---+
   |   |
       |
       |
       |
       |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
    print(hangmanlist[x])
