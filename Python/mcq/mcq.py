

import random

questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Seoul", "B. Tokyo", "C. Beijing", "D. Bangkok"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Blue Planet?",
        "options": ["A. Earth", "B. Neptune", "C. Uranus", "D. Venus"],
        "answer": "A"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
        "answer": "A"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "What is the national sport of Japan?",
        "options": ["A. Judo", "B. Karate", "C. Sumo Wrestling", "D. Baseball"],
        "answer": "C"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["A. 1942", "B. 1945", "C. 1948", "D. 1950"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    {
        "question": "What is the currency of the United Kingdom?",
        "options": ["A. Euro", "B. Pound Sterling", "C. Dollar", "D. Franc"],
        "answer": "B"
    }
]

def run_quiz():
    print("=== 🌍 GENERAL KNOWLEDGE QUIZ ===")
    print("Answer the following MCQs (A/B/C/D). Type 'exit' anytime to quit.\n")

    # Pick random 5 questions from the pool
    quiz_questions = random.sample(questions, 5)
    score = 0

    for i, q in enumerate(quiz_questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for option in q["options"]:
            print(option)

        user = input("Your answer (A/B/C/D): ").strip().upper()
        if user == "EXIT":
            print("Exiting the quiz... 👋")
            break

        if user == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was {q['answer']}.")

    print("\n=== QUIZ OVER ===")
    print(f"Your Score: {score}/{len(quiz_questions)}")
    percentage = (score / len(quiz_questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    # Fun feedback
    if percentage == 100:
        print("🎉 Perfect! You're a genius!")
    elif percentage >= 70:
        print("👍 Great job! You know your stuff.")
    elif percentage >= 40:
        print("🙂 Not bad, but keep learning.")
    else:
        print("📚 Time to brush up on your general knowledge!")

def main():
    run_quiz()

if __name__ == "__main__":
    main()
