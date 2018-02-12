# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:00:22 2018

@author: Muhammad Amin

Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

"""

def getGuessedWord(secretWord, lettersGuessed):
    
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far.
    '''
    
    temp=[]
    for letters in secretWord:
        if letters in lettersGuessed:
            temp.extend(letters)
        else:
            temp.extend('_')
    temp=' '.join(temp)
    return temp
    
# Correct 10.0/10.0 points (graded)

