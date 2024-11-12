#Factorial
print("Factorial of a number")
n=int(input("Enter the number you want to get factorial of "))
fac=1
if n>0:
    for i in range(1,n+1):
        fac=fac*i
    print(f"The factorial of {n} is {fac}")
elif n==0:
    print(f"The factorial of {n} is 1")
else:
    print("The number is -ve")
