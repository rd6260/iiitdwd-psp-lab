while True:
    l=int(input("enter number of digits\n"))
    num = [0] * (l + 1)
    num[0]=0
    for i in range(1,l+1):
        num[i]=int(input())
    for i in range(l,-1,-1):
        if num[i]==9:
            num[i]=0
        else:
            num[i]+=1
            break
    print("output is\n")
    if num[0]!=0:
        print(num[0])
    for i in range(1,l+1):
        print(num[i])



