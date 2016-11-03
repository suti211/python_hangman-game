#init


def loadInWords(FILE):
    myFile = open(FILE, "r")
    array = myFile.read().split("\n")
    myFile.close()
    return array
