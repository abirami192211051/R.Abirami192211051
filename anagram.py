str1=input("enter the string:")
str2=input("enter the string:")
str3=str1.upper()
str4=str2.upper()
if sorted(str3)==sorted(str4):
    print("its a anagram")
else:
    print("its not a anagram")
    
