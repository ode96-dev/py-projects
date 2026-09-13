import random

MAX_LINES = 3
MAX_BET_AMOUNT = 100
MIN_BET_AMOUNT = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 5,
    "C": 8,
    "D": 10,
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        try:
            amount = int(input("Enter amount to deposit: $"))
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than 0.")
        except ValueError:
            print("Please enter a whole number.")

    return amount


def get_number_of_lines():
    while True:
        try:
            lines = int(input(f"Enter number of lines to bet on (1 - {MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        except ValueError:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        try:
            amount = int(input("Enter amount to bet on each line: $"))
            if MIN_BET_AMOUNT <= amount <= MAX_BET_AMOUNT:
                break
            else:
                print(f"Amount must be between ${MIN_BET_AMOUNT} and ${MAX_BET_AMOUNT}.")
        except ValueError:
            print("Please enter a whole number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You do not have enough money in your account. Current balance is ${balance}.")
        else:
            break

    print(f"You bet ${bet} on {lines} lines. Total bet is ${total_bet}.\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()