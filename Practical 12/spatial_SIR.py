# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:54:07 2020

@author: 92801
"""
#import important library
import numpy as np
import matplotlib.pyplot as plt

#set the parameter:
#the possibility of infection B(beta) and the possibility of recovery(gamma)
#the initial for time loop
B=0.3
Y=0.05
j=1

#make array of all susceptible population
population=np.zeros((100,100))

#create an infection on one random point within the array
outbreak=np.random.choice(range(100),2)
#To know the exact row and column number of this ourbreak spot
population[outbreak[0],outbreak[1]]=1

#set the time loop for 100 and keep the whole infection and recovery process within this loop
while j<=100:
    #to nevigate the infection spot
    infectedIndex=np.where(population==1)
    #coordinate the x and y of each point
    for i in range(len(infectedIndex[0])):
        x=infectedIndex[0][i]
        y=infectedIndex[1][i]
        #The 8 Neighbours of the infection point is risk being infected
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,x+2):
                #to exclude the infected person
                if (xNeighbour,yNeighbour)!=(x,y):
                    #ensure that the infection spot doesn't fall on the edges of the array
                    if xNeighbour!=-1 and yNeighbour!=-1 and xNeighbour!=100 and yNeighbour!=100:
                        #Only the susceptible population could be infected
                        if population[xNeighbour,yNeighbour]==0:
                            #There's a possibility of infection
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-B,B])[0]
        #For the infected population. There's a possibility that they could recover and get rid of the disease
        population[x,y]=np.random.choice(range(2),1, p=[1-Y,Y])[0] +1
    j+=1
    #the loop is broken

#To plot the result in heat map and present the figure
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

                        