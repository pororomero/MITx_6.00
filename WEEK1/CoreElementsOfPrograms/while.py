# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:28:51 2020

@author: Harvey
Instruction: Convert the following into code that uses a while loop.
        print 2
        prints 4
        prints 6
        prints 8
        prints 10
        prints Goodbye!
"""
n = 2
while n <= 10:
    print(n)
    n += 2
print("Goodbye!")


"""
Instruction: Convert the following into code that uses a while loop.
        prints Hello!
        prints 10
        prints 8
        prints 6
        prints 4
        prints 2
"""

print('Hello!')
n = 10
while n >= 2:
    print(n)
    n -= 2
    
    
"""Instruction: Write a while loop that sums the values 1 through end, 
inclusive. end is a variable that we define for you. So, for example, 
if we define end to be 6, your code should print out the result:
"""
end = 24
total_sum = 0
n = 1
while n <= end:
    total_sum += n
    n += 1
    
print(total_sum)
    
