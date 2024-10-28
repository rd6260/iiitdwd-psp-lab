import math
def stair_poss(N):
    n=N//2
    s=0
    for i in range(0,n+1):
        s+=math.factorial(N-i)/(math.factorial(i)*math.factorial(N-(2*i)))
    print(f"no. of ways to climb is {s}")

while True:
    N=int(input("enter no. of stairs u want to climb\n"))
    if N < 1:
        print("input galat hai")
        continue
    stair_poss(N)



