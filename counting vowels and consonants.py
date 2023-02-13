str=input("enter string:")
vcount,ccount=0,0
v=[]
c=[]
vowels="AaEeIiOoUu"
for i in range (0,len(str)):
    if str[i] in (vowels):
        vcount=vcount+1
        v.append(str[i])
    elif(str[i]!=" " and str[i] not in (vowels)):
        ccount=ccount+1
        c.append(str[i])
print("total number of vowels:",vcount)
print("total number of consonants:",ccount)
        
          
