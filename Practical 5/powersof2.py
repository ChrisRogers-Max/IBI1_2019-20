# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:19:25 2020

@author: 92801
"""
#I need to create a random integer n
#I need to define the function, that means I need to tell computer how things could be exactly done.
#then I apply the function on the random integer, I print it out
#The queston is how could I define the function?

import random
n=random.randint(1,8192)
print(n)
def two_powers(num):
    powers = []
    while num != 0:
        powers.append(num & -num)
        num = num & (num - 1)
    return powers
print(two_powers(n))