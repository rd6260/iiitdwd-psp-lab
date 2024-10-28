


def nth_fibo(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return nth_fibo(n-1)+nth_fibo(n-2)

while True:
    n=int(input("enter input\n"))
    print("output is" ,nth_fibo(n))

