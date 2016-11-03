#init
import hangman_funcs


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

myList = loadInWords("teszt.txt")
print(myList)

