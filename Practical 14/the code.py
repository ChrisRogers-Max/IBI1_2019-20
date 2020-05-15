# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:30:46 2020

@author: 92801
"""

from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

DOMTree=xml.dom.minidom.parse('go_obo.xml')
collection=DOMTree.documentElement
obo=collection.getElementsByTagName("term")

x=[]
y=[]
z=[]
X=[]
Y=[]
Z=[]
for term in obo:
    n=term.getElementsByTagName('id')[0]
    x.append(n.childNodes[0].data)
    m=term.getElementsByTagName('name')[0]
    y.append(m.childNodes[0].data)
    l=term.getElementsByTagName('defstr')[0]
    z.append(l.childNodes[0].data)
for i in range(len(x)):
    if 'autophagosome' in z[i]:
        Z.append(z[i])
        X.append(x[i])
        Y.append(y[i])
    else:
        continue

df=pd.DataFrame(index=[X,Y,Z])
df.to_excel('output.xlsx')

        
    