# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:37:31 2020

@author: 92801
"""

#There is three population categories among all people:
#1. susceptible: assumed to be healthy but could catch the disease when contact with carriers.
#2. Infected: people who have the disease and could spread it to susceptible groups who lack immunity to the disease
#3. recoved: people recover from the infectious disease. They have acquired immunity against the disease and is assumed that they won't have it again

#There is two possibility to be defined:
#1.the possibility of infected people spread the disease to susceptible group when there's contact between the twos. It is defined as B
#2.the possibility of infected people recoved from the disease. it is defined as y

import numpy as np
import matplotlib.pyplot as plt

susceptible=9999
S=[9999]
infected=1
I=[1]
recovered=0
R=[0]
B=0.3
y=0.05
j=1
k=0
l=[0]
#while k<=1000:
 #   l.append(k)
  #  k+=1
while j<=1000:
    l.append(j)
    t=np.random.choice(range(2),susceptible,p=[1-(B*infected/10000),B*infected/10000])
    s=sum(t)
    infected=infected+s
    susceptible=susceptible-s
    S.append(susceptible)
    n=np.random.choice(range(2),infected,p=[1-y,y])
    m=sum(n)
    infected=infected-m
    recovered=recovered+m
    I.append(infected)
    R.append(recovered)
    j+=1
    
plt.figure(figsize=(6,4), dpi=150)
plt.plot(I,label='Infected')
plt.plot(S,label='Susceptible')
plt.plot(R,label='Recovered')
plt.xlabel('Time')
plt.title('SIR model')
plt.ylabel('number of people')
plt.legend();

#plt.savefig(results from SIP model, type='png')








