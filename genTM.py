from TransitionMatrix import TransitionMatrix

def genTM():
    """

    """
    # the transition matrix involved with mapping the words
    TM = TransitionMatrix()
    
    inputText = "input/{}.txt".format(str(input("Name of input text file: ")))
    
    #FOR DEBUGGING
    #inputText = "input/{}.txt.format(FILENAME)"

    with open(inputText, "r") as f:
        line = f.readline()
        while line:
            addKeys(line, TM)
            line = f.readline()

        TM.initMatrix()
        # move file pointer back to the beginning
        f.seek(0, 0)
        line = f.readline()
        while line:
            addEntries(line, TM)
            line = f.readline()
    TM.normalize()
    return TM

def tokenizeLine(line):
    """
    
    """
    punc = [',', '.', '?', '!']
    line = line.split()
    lineSplit = []
    for word in line:
        if word[-1] in punc:
            lineSplit.append(word[:-1].lower())
            lineSplit.append(word[-1].lower())
        else:
            lineSplit.append(word.lower())
    return lineSplit
    
    
def addKeys(line, TM):
    lineProcessed = tokenizeLine(line)
    for word in lineProcessed:
        TM.addKey(word)

def addEntries(line, TM):
    wordAdj = tokenizeLine(line)
    for i in range(len(wordAdj)-1):
        TM.addToMatrix(wordAdj[i], wordAdj[i+1])
