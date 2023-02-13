
final=[]
n=int(input("Enter the limit:"))
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        i="FizzBuzz"
        final.append(i)
    elif(i%3==0):
        i="Fizz"
        final.append(i)
    elif(i%5==0):
        i="Buzz"
        final.append(i)
    else:
        final.append(i)
print(final)
