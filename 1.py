# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:15:39 2019

@author: akile
"""
import numpy as np
import sys
sys.stdout = open('file', 'w')


A=[]
B=[]
b=[]
et=[None]
ea=[]
d=int(input('Enter the dimension : '))
print('Enter all ',d*d,' elements ')
for i in range(d*d):
    A.append(int(input()))
A=np.reshape(A,[d,d])
for i in range(d):
    B.append(1)
pres=[]

i=0
while(True):
    ans=np.matmul(A,B)
    count=0
    for j in ans:
        if(j<0):
            count+=1
    if(count>0):
        pres.append(float(min(ans)))
    else:
        pres.append(float(max(ans)))
    B=ans/pres[i]
    b.append(B)
    if(i>0):
        eterror= abs((pres[i]-pres[i-1])/pres[i])*100
        et.append(eterror)
        if(pres[i]==pres[i-1]):
            break
    i+=1

EV=pres[i]

for i in range(len(pres)):
    eaerror= abs((EV-pres[i])/EV)*100
    ea.append(eaerror)

for i in range(len(pres)):
    print('At Iter ',i,' predicted : ',pres[i],' Et : ',et[i],'% \t Ea : ',ea[i],'%')    

print('The Eigen value : ',EV)
print('The Eigen Vector : ',B)      


        
    