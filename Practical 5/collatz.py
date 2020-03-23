# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:20:33 2020

@author: 92801
"""

#First I need to import the random data set
#Then I need to limit the range within positive integer
#I would pick a random n from the defined range
#n would be either even or odd
#so if we need to lead n into the Collatz sequence, we need to figure out a way to ensure n is or could 
#turn into even. Here is my thought: if n is even, then n=n/2. if n is odd, n=n-1; if n=1, the loop ends


import random
import sys
n=random.randint(0,sys.maxsize)
while n!=1:
    if n%2==0:
        n=n/2
    else:
        n=n-1
print(n)