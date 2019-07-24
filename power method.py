
import numpy as np
from numpy.linalg import inv

def powermethod(A,B,choice=0):
    pres=[]
    et=[None]
    ea=[]
    i=0
    while(True):
        ans=np.matmul(A,B)
        maxi=abs(ans[0])
        index=0
        for v in range(1,len(ans)):
            if(abs(ans[v])>maxi):
                maxi=abs(ans[v])
                index=v
        pres.append(ans[index])
        B=ans/pres[i]
        b.append(B)
        if(i>0):
            eterror= abs((pres[i]-pres[i-1])/pres[i])*100
            et.append(eterror)
            if(format(pres[i],'.5f')==format(pres[i-1],'.5f')):
                break
        i+=1
    if(choice==1):
        EV=1/pres[i]
    else:
        EV=pres[i]
    
    for i in range(len(pres)):
        if(choice==1):
            eaerror = abs((EV-(1/pres[i]))/EV)*100
        else:
            eaerror = abs((EV-(pres[i]))/EV)*100
        ea.append(eaerror)

    for i in range(len(pres)):
        print('At Iter ',i,' predicted : ',pres[i],' Et : ',et[i],'% \t Ea : ',ea[i],'%')    
    
    print('The Eigen value : ',EV)
    print('The Eigen Vector : ',B)      


A=[]
B=[]
b=[]

d=int(input('Enter the dimension : '))
print('Enter all ',d*d,' elements ')
for i in range(d*d):
    A.append(float(input()))
A=np.reshape(A,[d,d])
for i in range(d):
    B.append(1)

print("\nThe biggest Eigen Value : \n")
powermethod(A,B)

invA=inv(A)

print('\nThe smallest Eigen Value : \n')
powermethod(invA,B,1)
