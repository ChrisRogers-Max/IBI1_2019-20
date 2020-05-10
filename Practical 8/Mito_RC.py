# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:56:47 2020

@author: 92801
"""
import re
xfile=open('mito_gene.fa','r')
geneinformation=[]
genesequence=[]
seq=str()
count=0

for line in xfile:
    if line.startswith('>'):
        geneinformation.append(line)
        seq=''
        count+=1
    else:
        line=line.rstrip()
        seq=str(line)
        seq=re.sub('A', 't', seq)
        seq=re.sub('T', 'a', seq)
        seq=re.sub('G', 'c', seq)
        seq=re.sub('C', 'g', seq)
        seq=seq.swapcase()
        seq=''.join(reversed(seq))
        genesequence.append(seq)

yfile=open('Reverse_complementary_sequences_of_mitochondria_genes.fa','w')
for i in range(count):
    line1=geneinformation[i]
    line2=genesequence[i] +'\n'
    yfile.write(line1)
    yfile.write(line2)
yfile.close()
    



        
        
        
        
        
        