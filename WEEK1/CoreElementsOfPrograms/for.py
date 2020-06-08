# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:39:25 2020

@author: Harvey
Instruction: Convert the following code into code that uses a for loop.
        prints 2
        prints 4
        prints 6
        prints 8
        prints 10
        prints Goodbye!
"""

for n in range(2, 11, 2):
    print(n)
print('Goodbye!')

"""Instruction: Convert the following code into code that uses a for loop.
        prints Hello!
        prints 10
        prints 8
        prints 6
        prints 4
        prints 2
"""

print('Hello!   ')
for n in range(10, 1, -2):
    print(n)
    
"""Instruction; Write a for loop that sums the values 1 through end, 
inclusive. end is a variable that we define for you."""

end = 24
total_sum = 0
for n in range(end+1):
    total_sum += n
print(total_sum)