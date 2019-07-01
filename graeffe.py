a1=[1,-4,5,-2]
i=0
n=6
while(i<n):
    ans=[]
    ans.append(a1[0]**2)
    ans.append((a1[1]**2)-(2*a1[0]*a1[2]))
    ans.append((a1[2]**2)-(2*a1[1]*a1[3]))
    ans.append(a1[3]**2)
    print (ans)
    a1=ans
    i+=1
