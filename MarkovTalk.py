"""
    Main driver for creating markov chain and generating text from it.
"""

from TransitionMatrix import TransitionMatrix
from genTM import genTM
from genText import genText

def main() -> None:
    """
        Creates a transition matrix and output generated text from it.
    """
    welcome()

    TM: TransitionMatrix = genTM()
    output: str = genText(TM)
    
    print(output)

def welcome() -> None:
    """
        Prints a welcome message.
    """
    text = 'Put input file in input folder'

    print(text)

    pass

if __name__ == "__main__":
    main()