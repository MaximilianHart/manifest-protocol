import random


def dice(number):
    result = 0
    for i in range(number):
        die = random.randint(1, 6)
        result += die
    return result
