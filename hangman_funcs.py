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
def printUnderScores(x):
    for i in range(len(x)):
        print("_ ", end="")


########################################################################################

# asks a user for an imput and checks if that input is valid(alphabets and 1 character long) or not, if not it prints 
# that the caracters are not valid and asks the input again, if its valid it breaks out of the cycle
# usage : call the function where u need it 
def getUserInput():
    while True:
        userInput = input("Enter a character: ")

        if len(userInput) == 1 and not userInput.isdigit():
            break
        else:
            print("You gave more than 1 character, or not a character.")
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
