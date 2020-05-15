# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:47:07 2020

@author: 92801
"""

import numpy as np

#input the number N, please feel free to change the value of it if you want
N=4
#withdraw numbers whose values are within [0,22] in the amount of N 
alist=np.random.choice(range(23),N)
#According to the requirement, the random numbers should be within[1,23], so use the loop to change range from[0,22] to [1,23]
for i in range(len(alist)):
    alist[i]=alist[i]+1

#Import itertools which could withdraw specific numbers of elements and organize them in a certain sequence to generate a new list
import itertools

if N>=2:
    b=list(itertools.permutations(alist,2))
    for i in range(len(b)):
        x=b[i][0]
        y=b[i][1]
        if x+y==24 or x-y==24 or y-x==24 or x*y==24 or x/y==24 or y/x==24:
            print('yes')
        else:
            continue
if N>=3:
    b=list(itertools.permutations(alist,3))
    for i in range(len(b)):
        x=b[i][0]
        y=b[i][1]
        z=b[i][2]
        if (x+y)+z==24 or (x+y)-z==24 or (x+y)*z==24 or (x+y)/z:
            print('yes')
        elif x*y+z==24 or x*y-z==24 or x*y*z==24 or x*y/z==24:
            print('yes')
        elif (x-y)+z==24 or (x-y)-z==24 or (x-y)*z==24 or (x-y)/z==24:
             print('yes')
        elif x/y+z==24 or x/y-z==24 or x/y*z==24 or x/y/z==24:
            print('yes')
        else:
            continue
