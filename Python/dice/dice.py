
import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("=== Dice Rolling Simulator 🎲 ===")
    print("Press Enter to roll, or type 'exit' to quit.")

    while True:
        user = input("Roll dice? ").strip().lower()
        if user == "exit":
            print("Goodbye! 👋")
            break
        result = roll_dice()
        print(f"🎲 You rolled: {result}")

if __name__ == "__main__":
    main()
