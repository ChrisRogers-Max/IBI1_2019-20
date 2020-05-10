# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:06:53 2020

@author: 92801
"""

nucleotides=['A','C','G','T']
quantities=[6,4,5,6]
frequency=dict(zip(nucleotides,quantities))
print(frequency)

import matplotlib.pyplot as plt
plt.pie(quantities,labels=nucleotides,autopct='%1.1f%%',shadow=False,startangle=90,)
plt.axis('equal')
plt.show()
