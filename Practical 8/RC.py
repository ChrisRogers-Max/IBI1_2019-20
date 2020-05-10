# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:56:07 2020

@author: 92801
"""
import re
# import the regular expression library
seq='ATGCGACTACGATCGAGGGCCAT'
# A given string 
seq=re.sub('A', 't',seq)
seq=re.sub('T', 'a', seq)
seq=re.sub('G', 'c', seq)
seq=re.sub('C', 'g', seq)
# Replace each nucleotide based on the base pair priciple. To avoid the substitution of nucleotides that have finished the replacement, the result is written in non-capital form
seq=seq.swapcase()
#To turn all letters into capital forms
seq=''.join(reversed(seq))
#Reverse the sequence of the complementory strand. To show it in 5' to 3' order.
print(seq)
# print out the sequence of the complementory strand