



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




