s1=input("enter the string:")
s2=input("enter the search:")
s=s1.lower()
for i in range(0,len(s1)):
    if s1[i]==s2:
        print("index",s[i],i)
