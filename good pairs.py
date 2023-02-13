l1=[1,2,3,1,1,3]
for i in range (len(l1)):
      for j in range(i+1,len(l1)):
         if l1[i] == l1[j]:
             print("(",i,j,")")
             
