# init
import hangman_funcs
import os
import time


# import teszt

# main control variable
run = True

# while run is true the program asks for input, when the a word is completed, or the user lost a game,
# the user can change this variable to false, then the program quits.
while run:

    # choosing a random word from a website, if this fails uses a file instead
    try:
        os.system("clear")
        choosenWord = hangman_funcs.getWordFromNet().lower()
        hangman_funcs.appendWordToTxt(choosenWord)
        print("Currently using an online random word generator!")
        time.sleep(2)
    except:
        os.system("clear")
        print("Failed to get word, no connection, or site is not reachable.")
        print("Using local wordbase instead.")
        time.sleep(5)
        wordList = hangman_funcs.loadInWords("words.txt")
        choosenWord = hangman_funcs.pick_a_word(wordList)

    # strings to store the correct and incorrect character inputs
    correct = ""
    incorrect = ""

    # variable to track the user's lives
    lives = 0

    # fill up al ist with "_" chars
    letters = ["_ "] * len(choosenWord)

    # clears the screen, prints sout a colored message, and the initial state
    # of word (underscores)
    os.system("clear")
    print("\n\x1b[1;30;47m" + "########### This is a hangman game, where you need to guess a word from letter to letter. ###########" + "\x1b[0m\n")
    for i in letters:
        print(i, end="")

    while True:

        # for debug purposes only
        # print(choosenWord)
        hangman_funcs.prGreen("\n\nCorrect: " + correct)
        hangman_funcs.prRed("\n\nInorrect: " + incorrect)

        # gets user input, checks it, modifies the printline to the correct
        # word.
        userIn = hangman_funcs.getUserInput(correct, incorrect)
        indexes = hangman_funcs.checkTip(userIn, choosenWord)
        hangman_funcs.printUnderScores(choosenWord, indexes, letters)

        # handle what happens when the user gives wrong tip
        # adding
        if len(indexes) == 0:
            incorrect = incorrect + userIn + " "
            hangman_funcs.prRed("\n\nWrong tip!")
            lives += 1
            hangman_funcs.hangmanPicsList(lives)
        else:
            correct += userIn + " "
            hangman_funcs.prGreen("\n\nCorrect tip!")
            hangman_funcs.hangmanPicsList(lives)

        # handle what happens when the user is out of lives
        # asks if the user wants to try again
        if lives == 6:
            hangman_funcs.loseanimation()
            print("\nYour word was : " + choosenWord + ".")
            again = input("Do you want to try again ? (y/n): ")

            if again == "y":
                run = True
            else:
                run = False
                hangman_funcs.deletewordbase("words.txt")
            break

        # handle what happens when the user wins
        # asks if the user want another word
        if hangman_funcs.didTheUserWin(letters):
            hangman_funcs.winanimation()
            print("\nYour word was : " + choosenWord + ".")
            again = input("\nCongratulations! Do you want another word?(y/n):")
            if again == "y":
                run = True
            else:
                run = False
                hangman_funcs.deletewordbase("words.txt")
            break
