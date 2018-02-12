# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:53:47 2018

@author: Muhammad Amin

Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem.
First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False
For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

"""

def isWordGuessed(secretWord, lettersGuessed):
    """
    Input- String-> SecretWord, list->lettersGuessed
    Output- True if ALL letters of secretWord are in lettersGuess, else False
    
    """

    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

# Correct 10.0/10.0 points (graded)