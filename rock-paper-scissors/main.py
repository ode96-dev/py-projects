import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please enter your choice (rock, paper, scissors. Or Q to quit): ").lower()

    if user_input == "q":
        break

    if user_input not in choices:
        continue

    random_number = random.randint(0, 2)
    computer_choice = choices[random_number]
    print(f"Computer chose: {computer_choice}")

    if user_input == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("you win!")
    elif user_input == "paper" and computer_choice == "rock":
        user_wins += 1
        print("you win!")
    elif user_input == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("you win!")
    else:
        computer_wins += 1
        print("you lose!")

print("Good bye!")
print(f"Your final score is: {user_wins}. Computer wins: {computer_wins}")