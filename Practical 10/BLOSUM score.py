# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:32:27 2020

@author: 92801
"""

xfile=open('SOD2_mouse.fa', 'r')
yfile=open('SOD2_human.fa', 'r')
zfile=open('RandomSeq.fa', 'r')
x=[]
y=[]
z=[]
xy=0
yz=0
xz=0
for line in xfile:
    if line.startswith('>'):
        continue
    else:
        line=line.rstrip()
        x=list(line)
    #print('The SOD2 gene sequence in mouse is:', x)
for line in yfile:
    if line.startswith('>'):
        continue
    else:
        line=line.rstrip()
        y=list(line)
    #print('The SOD2 gene sequence in human is:', y)
for line in zfile:
    if line.startswith('>'):
        continue
    else:
        line=line.rstrip()
        z=list(line)
    #print('The random gene sequence is:', z)
for i in range(len(x)):
    if x[i]!=y[i]:
        xy+=1
print('BLOSUM score in mouse humam comparison is:', xy)
for i in range(len(z)):
    if y[i]!=z[i]:
        yz+=1
print('BLOSUM score in human randon sequence comparison is:', yz)
for i in range(len(z)):
    if x[i]!=z[i]:
        xz+=1
print('BLOSUM score in mouse random sequence comparison is:', xz)