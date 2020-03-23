# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 21:59:37 2020

@author: 92801
"""

# What does this piece of code do?
# Answer: 

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
#we define that boolean varieble of p is False
while p==False:
    #we start a while loop: judge whether p is False or not. If so, enter the loop;If not, don't enter
    p=True
    #P is true, Continue
    n = randint(1,100)
    #withdraw a random integer from (1,100)
    u = ceil(n**(0.5))
    for i in range(2,u+1):
    #i could be any number within range[2,u+1]
        if n%i == 0:
        # if any i could fit the equality, then we could conclue that:
            p=False
    #after all this code, we would judge again: p is Faluse or not to decide to break the loop or not
    
    
print (n)
    
        
        


    
