


def nth_fibo(n):
    if n <= 0:
        print("Invalid input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b

    return b



n=int(input("enter input\n"))
print("output is" ,nth_fibo(n))

