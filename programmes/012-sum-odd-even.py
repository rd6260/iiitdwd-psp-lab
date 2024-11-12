



def sum_odd_even():
    n = int(input("Enter the number till where you want sum: "))
    a,b = 0,0
    for i in range (0, n+1, 2):
        a += i
    print(f"The sum of all even number till {n} is {a}")
    for i in range (1, n+1, 2):
        b += i
    print(f"The sum of all odd numbers till {n} is {b}")

