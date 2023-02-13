L=[8,1,2,3,4]
l1=[]
for i in range (len(L)):
    count=0
    for j in range(len(L)):
        if L[i]>L[j]:
        
            count=count+1
    l1.append(count)
print(l1)
            
        
