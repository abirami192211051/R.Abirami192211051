num1=input("enter the number:")
num2=input("enter the number:")
num3=input("enter the number:")
bin='01'
for i in range(len(num1)):
    binary=True
    if num1[i] not in bin:
        print("invalid input")
        binary=False
        break
    for i in range(len(num2)):
        binary=True
        if num2[i] not in bin:
            print("invalid input")
            binary=False
            break
    for i in range(len(num3)):
        binary=True
        if num3[i] not in bin:
            print("invalid input")
            binary=False
            break
if binary:
    decn=[]
    dec1=int(num1,2)
    decn.append(dec1)
    dec2=int(num2,2)
    decn.append(dec2)
    dec3=int(num3,2)
    decn.append(dec3)
    print("decimal equivalent:",decn)
    if(dec1>dec2 and dec1>dec3):
        print("number one is greatest",dec1)
    elif(dec2>dec3 and dec2>dec1):
        print("number two is greatest",dec2)
    else:
        print("number three is greatest",dec3)
    
     
