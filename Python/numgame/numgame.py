
import random

def main():
    print("=== Guess the Number Game ===")
    print("I have picked a number between 1 and 100.")
    print("Try to guess it!")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = input("Enter your guess (or 'exit' to quit): ").strip()
            if guess.lower() == "exit":
                print("Game over! The number was:", number)
                break

            guess = int(guess)
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
