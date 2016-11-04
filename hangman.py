#init
import hangman_funcs

# main control variable
run = True

# while run is true the program asks for input, when the a word is completed, or the user lost a game,
# the user can change this variable to false, then the program quits.
while run:
    wordList = hangman_funcs.loadInWords("words.txt")
    print("Welcome!\n")

    # choosing a random word from a file, the file must exist!
    choosenWord = hangman_funcs.pick_a_word(wordList)

    # for debug purposes only
    #print(choosenWord)

    # strings to store the correct and incorrect character inputs
    correct = ""
    incorrect = ""

    # variable to track the user's lives
    lives = 0

    # fill up al ist with "_" chars
    letters = [ "_ "] * len(choosenWord)

    print("\n#############################This is a hangman game, where you need to guess a word from letter to letter.#############################\n")
    for i in letters:
        print(i, end="")

    while True:
        print("\n\nCorrect: %s" % (correct))
        print("\nInorrect: %s" % (incorrect))

        # gets user input, checks it, modifies the printline to the correct word.
        userIn = hangman_funcs.getUserInput(correct, incorrect)
        indexes = hangman_funcs.checkTip(userIn, choosenWord)
        hangman_funcs.printUnderScores(choosenWord, indexes, letters)

        # handle what happens when the user gives wrong tip
        if len(indexes) == 0:
            incorrect = incorrect + userIn + " "
            print("\n\nWrong tip!")
            hangman_funcs.hangmanPicsList(lives)
            lives += 1
        else:
            correct += userIn + " "
        
        # handle what happens when the user is out of lives
        # asks if the user wants to try again
        if lives == 7:
            print("\nYour word was : " + choosenWord + ".")
            print("You failed miserably... Again...")

            again = input("Do you want to try again ? (y/n): ")

            if again == "y":
                run = True
            else:
                run = False
            break
        
        # handle what happens when the user wins
        # asks if the user want another word
        if hangman_funcs.didTheUserWin(letters):
            again = input("\nCongratulations! Do you want another word?(y/n):")
            if again == "y":
                run = True
            else:
                run = False
            break
   


