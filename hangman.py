#init
import hangman_funcs

run = True

while run:
    wordList = hangman_funcs.loadInWords("words.txt")
    print("Welcome!\n")

    choosenWord = hangman_funcs.pick_a_word(wordList)
    print(choosenWord)

    correct = ""
    incorrect = ""
    lives = 0

    letters = [ "_ "] * len(choosenWord)

    print("\n#############################This is a hangman game, where you need to guess a word from letter to letter.#############################\n")
    for i in letters:
        print(i, end="")

    while True:
        print("\n\nCorrect: %s" % (correct))
        print("\nInorrect: %s" % (incorrect))

        userIn = hangman_funcs.getUserInput(correct, incorrect)
        indexes = hangman_funcs.checkTip(userIn, choosenWord)
        hangman_funcs.printUnderScores(choosenWord, indexes, letters)

        if len(indexes) == 0:
            incorrect = incorrect + userIn + " "
            print("\n\nWrong tip!")
            hangman_funcs.hangmanPicsList(lives)
            lives += 1
        else:
            correct += userIn + " "

        if lives == 7:
            print("\nYour word was : " + choosenWord + ".")
            print("You failed miserably... Again...")

            again = input("Do you want to try again ? (y/n): ")

            if again == "y":
                run = True
            else:
                run = False
            break

        if hangman_funcs.didTheUserWin(letters):
            

            again = input("\nCongratulations! Do you want another word?(y/n):")

            if again == "y":
                run = True
            else:
                run = False
            break
   


