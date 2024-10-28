



i=1
while True:
    n=int(input("enter the number\n"))
    if n<1:
        print("invalid input")
    else:
        while True:
            if i*i==n:
                print(i)
                break
            elif i*i>n:
                print(i-1)
                break
            i+=1




