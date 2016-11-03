#init
import hangman_funcs
 

wordList = hangman_funcs.loadInWords("words.txt")
choosenWord = hangman_funcs.pick_a_word(wordList)
print(choosenWord)
hangman_funcs.printUnderScores(choosenWord)

correctTips = []
incorrectTips = []

userIn = hangman_funcs.getUserInput()

indexes = hangman_funcs.checkTip(userIn, choosenWord)
print(indexes)


