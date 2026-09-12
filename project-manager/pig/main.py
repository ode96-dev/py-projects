import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter number of players (2-4): ")

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Players should be between 2 and 4.")
    else:
        print("Invalid entry. Try again!")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\n--- Player {player_idx + 1}'s turn ---")
        print(f"Your current total score: {player_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y): ")

            if should_roll.lower().strip() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done, 0 points gained this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}.")

            print(f"Your turn score is: {current_score}")

        player_scores[player_idx] += current_score
        print(f"Your total score is now: {player_scores[player_idx]}")

winning_score = max(player_scores)
winning_player = player_scores.index(winning_score) + 1
print(f"\nPlayer {winning_player} wins with a score of {winning_score}!")