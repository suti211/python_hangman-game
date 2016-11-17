import time
import urllib.request

# fills up a file with 1k words


def getWord():
    req = urllib.request.Request(
        "http://watchout4snakes.com/wo4snakes/Random/RandomWordPlus", b"Pos=n&Level=20")
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    return the_page.decode("utf-8")

file = open("words.txt", "a+")

for i in range(1000):
    file.writelines(getWord() + "\n")
    print("loading...", i)
    time.sleep(0.02)

file.close()
