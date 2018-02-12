# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:03:37 2018

@author: Muhammad Amin

10.0/10.0 points (graded)
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
    
"""
import string

def getAvailableLetters(lettersGuessed):
    
    """
    Input- list of letters -> lettersGuessed
    Output- string of letters that haven't been guessed yet
    
    """

    alphabet=string.ascii_lowercase
    alphabet=list(alphabet)
    alphabet_copy=alphabet[:]
    
    for letters in alphabet_copy:
        if letters in lettersGuessed:
            alphabet.remove(letters)
            
    alphabet=''.join(alphabet)
    return alphabet   
    
    
    
# Correct 10.0/10.0 points (graded)