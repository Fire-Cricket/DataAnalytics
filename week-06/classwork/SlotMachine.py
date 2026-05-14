# Jordan R. Worrobah
# 5/12/2026
# Slot Machine

import random
import time

# Function to spin the slot machine
def spin_slot_machine():

    symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]

    result = []

    print("\n🎰 Spinning...\n")

    # FOR LOOP
    for spin in range(3):

        symbol = random.choice(symbols)

        result.append(symbol)

        time.sleep(1)

        print(symbol)

    return result


# Function to check winner
def check_winner(result):

    if result[0] == result[1] == result[2]:
        return "\n🎉 JACKPOT! 3 matching symbols!"

    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        return "\n🔥 Nice! You got 2 matching symbols!"

    else:
        return "\n❌ No match. Try again!"


# Main game function
def play_game():

    print("🎰 Welcome to Jordan's Slot Machine! 🎰")

    name = input("Enter your name: ")

    print(f"\nGood luck, {name}!")

    # Ask how many rounds
    rounds = int(input("\nHow many rounds would you like to play? "))

    # Check for positive number
    if rounds <= 0:
        print("Please enter a positive number.")
        return

    # FOR LOOP for rounds
    for round_number in range(1, rounds + 1):

        input(f"\nPress Enter to spin Round {round_number}...")

        result = spin_slot_machine()

        message = check_winner(result)

        print(message)

    print("\n🎉 Thanks for playing!")


# Start the game
play_game()