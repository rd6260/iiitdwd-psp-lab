



def sum_odd_even():
    n = int(input("Enter the number till where you want sum: "))
    a,b = 0,0
    for i in range (0, n+1, 2):
        a += i
    print(f"The sum of all even number till {n} is {a}")
    for i in range (1, n+1, 2):
        b += i
    print(f"The sum of all odd numbers till {n} is {b}")

def numer_guess():
    low, high = 0, 100
    attempts = 0
    while low <= high:
        attempts += 1
        guess = (low+high)//2
        print(f"is your guess {guess}?")
        feedback = input("'h' if my guess is high, 'l' if my guess lower, 'c' if my guess is correct: ")
        if feedback == "h":
            low = guess + 1
        elif feedback == "l":
            high = guess - 1
        else:
            print(f"I guessed in {attempts} attempts, your number is {guess}")
            break
diamond_patt()
