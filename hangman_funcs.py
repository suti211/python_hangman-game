#init
import random

kutyafasz=["valami", "valami2", "valami3", "valami4"]


def pick_a_word(x):
    import random
    the_word = (x[random.randrange(len(x))])
    return the_word

print(pick_a_word(kutyafasz))

