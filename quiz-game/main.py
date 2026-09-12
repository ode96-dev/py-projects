print("Welcome to the Quiz Game")

questions = [
"What does CPU stand for? ",
"What does GPU stand for? ",
"What does RAM stand for? ",
"What does PSU stand for? ",
]

answers = [
    "Central Processing unit",
    "Graphics Processing unit",
    "Random Access Memory",
    "Power Supply Unit"
]

playing = input("Do you want to play a game? (y/n): ")

if playing.lower().strip() != "y":
    quit()
print("Okay. Let the game begin!")

score = 0

for question, correct_answer in zip(questions, answers):
    user_answer = input(question)

    if user_answer.lower().strip() == correct_answer.lower().strip():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect answer. Correct answer: {correct_answer}")

print(f"Your final score is: {score}")


