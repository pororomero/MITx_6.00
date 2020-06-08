# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:56:06 2020

@author: Harvey

Instruction: Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
bobCount = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        bobCount += 1

print(bobCount)