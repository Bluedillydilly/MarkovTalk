# MarkovTalk
Using the principle of markov chains in the form of a matrix (transition matrix) to generate text based on another input text.


## The How

Program is composed of 4 parts
* Markovtalk -  a wrapper for genTM and genText
* genTM - responsible for talking the input text and constructing the transition matrix 
* genText - responsible for generating a potential abitrary amount of new lines of text using the previously generated transition matrix(TM)

## The Goal
* Create sentences that seem related to the input test.
    * The goal has not been reached.

## The Future
* Provide an url to extract text from. Support only certain websites? ie wikipedia.
* Fix capitialization of words following '.'s, '!'s, and '?'.
* Provide the option to save the output to a textfile.

## How to Run
1. Have python (3.0+ as this was tested on 3.7.2) and numpy installed.
2. Put any input text files in the input folder
3. Run MarkovTalk.py

If one wants to change how much text is outputted edit numWord in genText