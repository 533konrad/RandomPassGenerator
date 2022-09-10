import string
from random import *


def PassGenerator(passLen, passNum=False, passSpecial=False):
    finalpass = ""
    pool = string.ascii_letters
    if passNum:
        pool = pool + string.digits
    if passSpecial:
        pool = pool + string.punctuation
    for i in range(passLen):
#        char = randint(0,9)
#        char = choice(string.ascii_letters)
#        char = choice(string.punctuation)
#        random = ''.join([choice(string.ascii_letters + string.digits + string.punctuation) for n in range(4)])
#        print(random)

        finalpass = finalpass + str(choice(pool))
    return finalpass

#print(string.digits)
passLen = int(input("How long do you want your password? "))
passNum = input("Include numbers? if no press enter ")
passSpecial = input("Include special characters? if no press enter ")

print(PassGenerator(passLen, passNum, passSpecial))
