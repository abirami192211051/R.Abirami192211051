def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if i % 2==0:
            even+=(i**2)
        else:
            odd+=(i**2)
    l=[odd,even]
    return(l)
n=int(input("Enter the number of Elements:"))
if n>0:
    print("Enter the Elements:")
else:
    print("INVALID INPUT")
l=list(map(int,input().split()))
print(sumsquare(l))
