import random

def computer_guesses():
    low, high = 1, 100
    attempts = 0

    print("Think of a number between 1 and 100, and I'll guess it!")

    while True:
        guess = random.randint(low, high)
        print(f"My guess: {guess}")
        response = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()
        attempts += 1

        if response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess + 1
        elif response == 'c':
            print(f"🎯 I guessed it in {attempts} tries!")
            break
        else:
            print("Invalid response. Please enter H, L, or C.")

computer_guesses()
