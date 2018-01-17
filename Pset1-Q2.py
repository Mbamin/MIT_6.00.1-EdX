# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:07:43 2018

@author: Muhammad Amin
"""
#~~~~~~~~~~Instructions~~~~~~~~~
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print: Number of times bob occurs is: 2
x=0
y=1
z=2
count=0
while z<len(s):
    if s[x]=='b' and s[y]=='o' and s[z]=='b':
        count+=1
    x+=1
    y+=1
    z+=1
        
print("The number of times bob is repeated is: " +str(count))

# Passes All test cases (10/10)

