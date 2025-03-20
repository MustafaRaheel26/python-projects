import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    score = {"wins": 0, "losses": 0, "ties": 0}

    while True:
        user = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user == "quit":
            print(f"Final Score: {score}")
            break
        if user not in choices:
            print("Invalid choice. Try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            score["ties"] += 1
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            score["wins"] += 1
            print("You win!")
        else:
            score["losses"] += 1
            print("You lose!")

rock_paper_scissors()
