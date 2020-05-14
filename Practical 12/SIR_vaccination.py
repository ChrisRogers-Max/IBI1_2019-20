# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:57:38 2020

@author: 92801
"""

import numpy as np
import matplotlib.pyplot as plt

N=10000
#vaccinated=int(N*0.1)
#V=[vaccinated]
infected1=1
infected2=1
infected3=1
infected4=1
infected5=1
infected6=1
infected7=1
infected8=1
infected9=1
infected10=1


I1=[1]
I2=[1]
I3=[1]
I4=[1]
I5=[1]
I6=[1]
I7=[1]
I8=[1]
I9=[1]
I10=[1]

recovered=0
#susceptible=N-infected-vaccinated-recoved
B=0.3
y=0.05
j1=1
j2=1
j3=1
j4=1
j5=1
j6=1
j7=1
j8=1
j9=1
j10=1

l=[0]

k=1

S1=N-infected1-recovered
S2=N-infected2-recovered-int(N*0.1)
S3=N-infected3-recovered-int(N*0.2)
S4=N-infected4-recovered-int(N*0.3)
S5=N-infected5-recovered-int(N*0.4)
S6=N-infected6-recovered-int(N*0.5)
S7=N-infected7-recovered-int(N*0.6)
S8=N-infected8-recovered-int(N*0.7)
S9=N-infected9-recovered-int(N*0.8)
S10=N-infected10-recovered-int(N*0.9)


while k<=1000:
    l.append(k)
    k+=1

while j1<=1000:
    t1=np.random.choice(range(2),S1,p=[1-(B*infected1/10000),B*infected1/10000])
    S1=S1-sum(t1)
    infected1=infected1+sum(t1)
    n1=np.random.choice(range(2),infected1,p=[1-y,y])
    infected1=infected1-sum(n1)
    I1.append(infected1)
    j1+=1

while j2<=1000:
    t2=np.random.choice(range(2),S2,p=[1-(B*infected2/10000),B*infected2/10000])
    S2=S2-sum(t2)
    infected2=infected2+sum(t2)
    n2=np.random.choice(range(2),infected2,p=[1-y,y])
    infected2=infected2-sum(n2)
    I2.append(infected2)
    j2+=1

while j3<=1000:
    t3=np.random.choice(range(2),S3,p=[1-(B*infected3/10000),B*infected3/10000])
    S3=S3-sum(t3)
    infected3=infected3+sum(t3)
    n3=np.random.choice(range(2),infected3,p=[1-y,y])
    infected3=infected3-sum(n3)
    I3.append(infected3)
    j3+=1

while j4<=1000:
    t4=np.random.choice(range(2),S4,p=[1-(B*infected4/10000),B*infected4/10000])
    S4=S4-sum(t4)
    infected4=infected4+sum(t4)
    n4=np.random.choice(range(2),infected4,p=[1-y,y])
    infected4=infected4-sum(n4)
    I4.append(infected4)
    j4+=1

while j5<=1000:
    t5=np.random.choice(range(2),S5,p=[1-(B*infected5/10000),B*infected5/10000])
    S5=S5-sum(t5)
    infected5=infected5+sum(t5)
    n5=np.random.choice(range(2),infected5,p=[1-y,y])
    infected5=infected5-sum(n5)
    I5.append(infected5)
    j5+=1

while j6<=1000:
    t6=np.random.choice(range(2),S6,p=[1-(B*infected6/10000),B*infected6/10000])
    S6=S6-sum(t6)
    infected6=infected6+sum(t6)
    n6=np.random.choice(range(2),infected6,p=[1-y,y])
    infected6=infected6-sum(n6)
    I6.append(infected6)
    j6+=1

while j7<=1000:
    t7=np.random.choice(range(2),S7,p=[1-(B*infected7/10000),B*infected7/10000])
    S7=S7-sum(t7)
    infected7=infected7+sum(t7)
    n7=np.random.choice(range(2),infected7,p=[1-y,y])
    infected7=infected7-sum(n7)
    I7.append(infected7)
    j7+=1

while j8<=1000:
    t8=np.random.choice(range(2),S8,p=[1-(B*infected8/10000),B*infected8/10000])
    S8=S8-sum(t8)
    infected8=infected8+sum(t8)
    n8=np.random.choice(range(2),infected8,p=[1-y,y])
    infected8=infected8-sum(n8)
    I8.append(infected8)
    j8+=1

while j9<=1000:
    t9=np.random.choice(range(2),S9,p=[1-(B*infected9/10000),B*infected9/10000])
    S9=S9-sum(t9)
    infected9=infected9+sum(t9)
    n9=np.random.choice(range(2),infected9,p=[1-y,y])
    infected9=infected9-sum(n9)
    I9.append(infected9)
    j9+=1

while j10<=1000:
    t10=np.random.choice(range(2),S10,p=[1-(B*infected10/10000),B*infected10/10000])
    S10=S10-sum(t10)
    infected10=infected10+sum(t10)
    n10=np.random.choice(range(2),infected10,p=[1-y,y])
    infected10=infected10-sum(n10)
    I10.append(infected10)
    j10+=1


plt.figure(figsize=(6,4), dpi=150)
plt.plot(I1,label='0 vaccination immunity')
plt.plot(I2,label='10% vaccination immunity')
plt.plot(I3,label='20% vaccination immunity')
plt.plot(I4,label='30% vaccination immunity')
plt.plot(I5,label='40% vaccination immunity')
plt.plot(I6,label='50% vaccination immunity')
plt.plot(I7,label='60% vaccination immunity')
plt.plot(I8,label='70% vaccination immunity')
plt.plot(I9,label='80% vaccination immunity')
plt.plot(I10,label='90% vaccination immunity')
plt.xlabel('Time')
plt.title('SIR_Vaccination model')
plt.ylabel('number of infected people')
plt.legend();

#plt.savefig(<results from SIP model>, type='png')
