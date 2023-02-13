str=input("enter a string:")
a , d , s , spl = 0 , 0  , 0 , 0
alpha = []
digit = []
spl_char = []
for i in range (len(str)):
    if str[i].isalpha():
        a= a+1
        alpha.append(str[i])
    elif str[i].isdigit():
        d=d+1
        digit.append(str[i])
    elif str[i].isspace():
        s=s+1
    else:
        spl=spl+1
        spl_char.append(str[i])
print("alphabet letters:",alpha,a)
print("\nnumbers:",digit,d)
print("\nspace:",s)
print("\nspecial charcter:",spl,spl_char)
