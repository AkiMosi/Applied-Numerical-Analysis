#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:08:07 2019

@author: akimosi
"""
import math
import matplotlib.pyplot as plt

def fbncr(n,r,forb):
    if (r == 0):
        return 1
    ans = n
    for i in range(1,r):
        if(forb == 0):
            ans *= float(format((n - i),".5f"))
        else:
            ans *= float(format((n + i),".5f"))
    return float(format(ans/math.factorial(r),".5f"))

#x = [45,50,55,60,65]
#y = [114.84,96.16,83.52,74.48,68.48]
#x = [20,23,26,29]
#y = [0.342,0.3907,0.4384,0.4848]
#x = [1941,1951,1961,1971,1981,1991]
#y = [20,24,29,36,46,51]
x = [40,60,80,100,120]
y = [250,370,470,540,590]

h = x[1] - x[0]

xx = 70
forb = 0

dif = [xx-i for i in x]
mini = 10000
index = 0

for i in range(len(dif)):
    if(abs(dif[i]) < mini):
        mini = abs(dif[i])
        index = i
        
if(dif[index] > 0):
    uv = (xx - x[0]) / h
    forb = 0
else:
    uv = (xx - x[len(x) - 1]) / h
    forb = 1

#uv = (xx - x[len(x) - 1]) / h
#forb = 1


yt = [y]
temp = []
for i in range(len(x)-1):
    temp = list()
    for j in range(len(yt[i])-1):
        temp.append(0)
    yt.append(temp)

for i in range(1,len(yt)):    
    for j in range(len(yt[i])):
        yt[i][j] = float(format((yt[i-1][j+1] - yt[i-1][j]),".5f"))
        
print("y",end = '\t')
for i in range(len(x)-1):
    print("del^",i+1,end = '\t')
for i in range(len(yt)):
    print('\n')
    for j in range(len(yt[i])):
        print(yt[j][i],end = '\t')
        
print("\n\n\n")
yy = 0

for i in range(len(yt)):
    if(forb == 0):
        yy += yt[i][0] * fbncr(uv,i,0)
        print(yt[i][0] ,fbncr(uv,i,0))
    else:
        yy += yt[i][len(yt[i])-1] * fbncr(uv,i,1)
        print(yt[i][len(yt[i])-1] ,fbncr(uv,i,1))
    
print("\n\n\ny(",xx,") = ",yy)
plt.plot(x,y,c = 'r')
#plt.plot(x,y,c = 'g')