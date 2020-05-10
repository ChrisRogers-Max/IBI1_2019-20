# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:22:28 2020

@author: 92801
"""

afile= open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
gene=[]
genename=[]
c=str()
x=[]
count=0

for line in afile:
    if line.startswith('>'):
        if c!='':
            gene.append(c)
        genename.append(line[1:6])
        x.append(line)
        c=''
        count +=1
    else:
        line=line.rstrip()
        c=c+str(line)
bfile=open('mito_gene.fa','w')
for i in range(count):
    if 'R64-1-1:Mito' in x[i]:
        line1='>'+genename[i]+' '+str(len(gene[i]))+'\n'
        line2=gene[i]+'\n'
        bfile.write(line1)
        bfile.write(line2)
bfile.close()
        
        
