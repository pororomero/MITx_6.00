# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:00:57 2020

@author: Harvey

Instruction: Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print:
    Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, 
if s = 'abcbcd', then your program should print
    Longest substring in alphabetical order is: abc
    
Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you 
move on to a different part of the course. If you have time, come back to this 
problem after you've had a break and cleared your head.
"""

#s = 'abcbcd'
s = 'azcbobobegghakl'
longestSubString = ''
for i in range(len(s)):
    substring = s[i]
    for j in range(i+1, len(s)):
        # checking if the last letter in substring is less than the jth element
        if substring[-1] <= s[j]: 
            substring += s[j]
        else: 
            break
    if len(substring) > len(longestSubString):
        longestSubString = substring
print(longestSubString)