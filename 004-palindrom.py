def is_palindrome(n):
    N=str(n)
    l=len(N)
    for j in range(0,l//2):
        if N[j]!=N[l-j-1]:
            return False
    return True

while True:
    n=int(input("enter a number to check palindrome\n"))
    print(is_palindrome(n))


