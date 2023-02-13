num=int(input("Enter the number:"))
num1=str(num)
num2=num1[::-1]
num3=str(num2)
if num1==num3:
    print("Is a Palindrome")
else:
    print("Is not a Palindrome")
