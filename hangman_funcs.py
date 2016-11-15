import string
import os
import time


# picks and returns random elment of an "x" list
# usage : pick_a_word(listname)


def pick_a_word(x):
    import random
    the_word = (x[random.randrange(len(x))])
    return the_word

##########################################################################

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

##########################################################################

# gets a word (x) counts the lenght of it and prints out the equal amounts of underscores and spaces between them
# usage : printUnderScores(wordname)


def printUnderScores(choosenWord, indexList, letters):

    if len(indexList) != 0:
        for i in indexList:
            letters[i] = choosenWord[i]

    for i in range(len(choosenWord)):
        print(str(letters[i]), end="")


##########################################################################

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
            os.system("clear")
            break
        else:
            print(
                "You gave more than 1 character, or not a character.\nOr the character is already used!")

    return userInput

##########################################################################

# gets a character, and another word string as input,
# then returns on wich index the character appearn in the given word, in a list,
# returns -1 if the given char is not in the word


def checkTip(userInput, selectedWord):
    matchIndex = []
    for i in range(len(selectedWord)):
        if selectedWord[i] == userInput:
            matchIndex.append(i)
    return matchIndex

##########################################################################

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


##########################################################################

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

##########################################################################
# iterates through an ascii art list to create a lose animation


def loseanimation():
    lista = ['''

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
       /|\  |     U got hanged!
       / \  |
            |
      =========''']

    for i in lista:
        if i == lista[0]:
            os.system('clear')
            print(i, end="\n")
            time.sleep(0.25)
            os.system('clear')
        elif i == lista[-1]:
            print(i, end="\n")
            time.sleep(0.25)
        else:
            print(i, end="\n")
            time.sleep(0.25)
            os.system('clear')

##########################################################################
# iterates through an ascii art list to create a win animation


def winanimation():
    lista = ['''                    









  _____________ o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''









  _____________ o ___<
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''








                     o
  _____________ o __<(
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''







                     _
                    o)
  _____________ o _<(_
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''






                     .
                    __
                   o)_
  _____________ o <(__
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''






                    .-
                   __|
                  o)__
  _____________ o (__(
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''





                     (
                   .--
                  __||
                 o)__ 
  _____________ o __(*
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''




                     (
                    ()
                  .--.
                 __||_
                ~)__ |
  _____________.o _(*)
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''




                    ( 
                   (  
                 .--. 
                __||__
               o)__ |_
  ____________< o (*)_
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''




                    ( 
                    ) 
                .--.  
               __||___
              o)__ |_ 
  ___________<( o *)_(
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''



                     (
                  (   
                 ()   
               .--.  -
              __||___|
             o)__ |_ |
  __________<(  o )_(*
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''



                    ( 
                   ) )
                (     
              .--.  --
             __||___|[
            o)__ |_ | 
  _________<(_  o _(*)
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''




                   ) )
                ()    
             .--.  ---
            __||___|[_
           o)__ |_ | .
  ________<(_ ( o (*)_
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


                    ( 
                  (  )
               ( ) )  
              ()      
            .--.  ----
           __||___|[_]
          o)__ |_ | ..
  _______<(__(* o *)_~
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


                    ( 
                     )
               (   )  
              (       
           .--.  -----
          __||___|[_]|
         o)__ |_ | ..|
  ______<(__(*) o )_~_
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''



                (  )  
             ( )      
            (         
          .--.  ----- 
         __||___|[_]| 
        o)__ |_ | ..|=
  _____<(__(*)_ o _~__
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


                 (    
                  )  )
              )       
           ()        _
         .--.  ----- |
        __||___|[_]| |
       o)__ |_ | ..|=|
  ____<(__(*)_( o ~___
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


                 (    
               (  )   
            (   )     
            )       __
        .--.  ----- | 
       __||___|[_]| |.
      o)__ |_ | ..|=|_
  ___<(__(*)_(* o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


               (      
             (  )  )  
          ( ) )       
         ()        ___
       .--.  ----- |  
      __||___|[_]| |.|
     o)__ |_ | ..|=|_|
  __<(__(*)_(*) o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


               (      
                  )   
          ( )         
         (        ____
      .--.  ----- |  _
     __||___|[_]| |.|#
    o)__ |_ | ..|=|_|-
  _<(__(*)_(*)_ o ___~
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


             (        
           (  )  )    
        ( ) )         
       ()        ____.
     .--.  ----- |  _ 
    __||___|[_]| |.|#|
   o)__ |_ | ..|=|_|-|
  <(__(*)_(*)_~ o __~(
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''



              )  )    
        () )          
       (        ____._
    .--.  ----- |  _  
   __||___|[_]| |.|#|.
  o)__ |_ | ..|=|_|-|_
  (__(*)_(*)_~_ o _~(*
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


           ( )        
         (  )         
        ) )           
     ()        ____.__
   .--.  ----- |  _  -
  __||___|[_]| |.|#|.[
  )__ |_ | ..|=|_|-|__
  __(*)_(*)_~__ o ~(*)
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


             )        
         (  )         
     (  ) )           
      )       ____.___
  .--.  ----- |  _  - 
  _||___|[_]| |.|#|.[]
  __ |_ | ..|=|_|-|___
  _(*)_(*)_~___ o (*)_
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


         (            
       (  )  )        
    ( ) )             
   ()        ____.____
  --.  ----- |  _  - a
  ||___|[_]| |.|#|.[].
  _ |_ | ..|=|_|-|____
  (*)_(*)_~____ o *)__
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


        ( )           
      (               
   (  )               
   )        ____._____
  -.  ----- |  _  - a:
  |___|[_]| |.|#|.[].[
   |_ | ..|=|_|-|_____
  *)_(*)_~____  o )___
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


       (              
     (  )  )          
  ( ) )               
  )        ____.______
  .  ----- |  _  - a:f
  ___|[_]| |.|#|.[].[]
  |_ | ..|=|_|-|______
  )_(*)_~_____~ o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


       ( )            
     (  )             
   ( )                
          ____.______.
    ----- |  _  - a:f 
  __|[_]| |.|#|.[].[].
  _ | ..|=|_|-|_______
  _(*)_~_____~( o ___(
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''



   (  )               
  ) )                 
         ____.______._
   ----- |  _  - a:f -
  _|[_]| |.|#|.[].[].[
   | ..|=|_|-|________
  (*)_~_____~(* o __(*
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


    (                 
  (                   
   )                  
        ____.______.__
  ----- |  _  - a:f - 
  |[_]| |.|#|.[].[].[]
  | ..|=|_|-|_________
  *)_~_____~(*) o _(*)
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


   (                  

  )                   
       ____.______.___
  ---- |  _  - a:f -  
  [_]| |.|#|.[].[].[].
   ..|=|_|-|__________
  )_~_____~(*)_ o (*)_
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''


   (                  
   )                  

      ____.______.____
  --- |  _  - a:f -   
  _]| |.|#|.[].[].[]..
  ..|=|_|-|___________
  _~_____~(*)__ o *)__
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''



  )                   

     ____.______._____
  -- |  _  - a:f -   |
  ]| |.|#|.[].[].[]..|
  .|=|_|-|___________|
  ~_____~(*)___ o )___
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''





    ____.______._____ 
  - |  _  - a:f -   | 
  | |.|#|.[].[].[]..| 
  |=|_|-|___________| 
  _____~(*)____ o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''





   ____.______._____  
   |  _  - a:f -   |  
   |.|#|.[].[].[]..|  
  =|_|-|___________|  
  ____~(*)____( o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''





   ____.______._____  
   |  _  - a:f -   |  
   |.|#|.[].[].[]..|  
  =|_|-|___________|  
  ____~(*)____( o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''', '''





   ____.______._____  
   | ._  -     -   |  
   |.: | YOU WON!  |  
  =|_: |___________|  
  ____-(*)____( o ____
  ~ ~ ~ ~ ~ ~ ~< >~ ~ 
                |     ''']

    for i in lista:
        if i == lista[0]:
            os.system('clear')
            print(i, end="\n")
            time.sleep(0.25)
            os.system('clear')
        elif i == lista[-1]:
            print(i, end="\n")
            time.sleep(0.25)
        else:
            print(i, end="\n")
            time.sleep(0.25)
            os.system('clear')
