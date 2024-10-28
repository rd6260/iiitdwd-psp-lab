
def perfect_num():
     n = int(input("Enter the number you want to check for perfect number: "))
     a = 0
     for i in range (1, (n//2)+1):
        if n%i == 0:
            a += i
        else:
            a = 0
     if a == n:
        print("It is a perfect number")
     else:
        print("not a perfect number")
