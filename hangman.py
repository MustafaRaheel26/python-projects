import random

def hangman():
    words = ["python", "developer", "streamlit", "artificial", "intelligence"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in guessed:
        print(" ".join(guessed))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

    if "_" not in guessed:
        print(f"🎉 You win! The word was {word}.")
    else:
        print(f"😞 You lose! The word was {word}.")

hangman()
