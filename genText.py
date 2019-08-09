"""

"""
from numpy import random
import TransitionMatrix


def genText(TM):
    """


    Params:
        TM: 
    """
    resultSpeak = ''
    currentWord = randomStart(TM)[0]
    numWord = 50 # the number of words you want
    punc = [',', '.', '!', '?']


    for i in range(numWord):
        space = ' '
        if currentWord in punc:
            space = ''
        new = space+currentWord
        resultSpeak += new
        currentWord = nextWord(TM, currentWord)
    return resultSpeak

def randomStart(TM):
    punc = [',', '.', '!', '?']
    word = random.choice(TM.getWords(), 1)
    while word in punc:
        word = random.choice(TM.getWords(), 1)
    return word

def nextWord(TM, currentWord):
    word = random.choice(TM.getWords(), 1, p=TM.getRow(currentWord))
    return word[0]