
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def main():
    print("=== Rock, Paper, Scissors ===")
    print("Type rock, paper, or scissors (or 'exit' to quit).")

    while True:
        user_choice = input("Your move: ").strip().lower()
        if user_choice == "exit":
            print("Goodbye! Thanks for playing.")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = decide_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
