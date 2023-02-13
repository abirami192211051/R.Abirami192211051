str=input("enter the string:")
str1=str.lower()
str2=set("aeiou")
for char in str1:
    if char in str2:
        str2.remove(char)
if len(str2)==0:
    print("accepted")
else:
    print("invalid")
