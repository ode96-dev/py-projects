name = input("What is your name? ")
print(f"Welcome {name} to this adventure!\n")

answer = input("You are on a dirt road that has come to an end. You can go left or right. Which way? ").lower().strip()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. (walk/swim): ").lower().strip()

    if answer == "swim":
        print("You swam across and were eaten by an alligator. You lose!")
    elif answer == "walk":
        print("You walked for many miles, ran out of energy, and got lost. You lose!")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come to a wobbly bridge. Do you want to cross it or go back? (cross/back): ").lower().strip()

    if answer == "back":
        print("You walked back to the start and ran out of time. You lose!")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (talk/ignore): ").lower().strip()

        if answer == "talk":
            print("The stranger offers you safe passage and gold. You win!")
        elif answer == "ignore":
            print("You ignore the stranger. They get offended and block your path. You lose!")
        else:
            print("Not a valid option. You lose!")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")