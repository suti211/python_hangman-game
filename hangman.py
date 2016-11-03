#init
import hangman_funcs

wordList = hangman_funcs.loadInWords("words.txt")
print("Welcome!\n")
print("This is a hangman game, where you need to guess a word from letter to letter.\n")

choosenWord = hangman_funcs.pick_a_word(wordList)
print(choosenWord)

correct = ""
incorrect = ""

letters = [ "_ "] * len(choosenWord)

while True:

    print("\nCorrect: %s" % (correct))
    print("\nInorrect: %s" % (incorrect))

    userIn = hangman_funcs.getUserInput()
    hangman_funcs.printUnderScores(choosenWord, hangman_funcs.checkTip(userIn, choosenWord), letters)
    indexes = hangman_funcs.checkTip(userIn, choosenWord)

    if len(indexes) == 0:
        incorrect = incorrect + userIn + " "
        print("Wrong tip!")
        hangman_funcs.hangmanPicsList(0)
    else:
        correct += userIn + " "

print(indexes)


