# Jordan R. Worrobah    
# 5/13/2026
from random import shuffle 

print("\n---------- Number Guesser Game ----------\n")

numberPool = list(range(1, 21))

shuffle(numberPool)

secretNumber = numberPool[0]

guessedNumbers = []

guessCount = 0

print("I am thinking of a number between 1 and 20.\n")

while True:

    try:

        guess = int(input("Enter your guess: "))

    except ValueError:

        print("Please enter a valid number.\n")

        continue

    guessedNumbers.append(guess)

    guessCount += 1

    if guess < secretNumber:

        print("Higher!\n")

    elif guess > secretNumber:

        print("Lower!\n")

    else:

        print("\nCorrect!")
        print(f"You guessed the number in {guessCount} guesses!")

        print("\nYour guesses were:")

        for number in guessedNumbers:
            print(f"- {number}")

        if guessCount < 5:
            print("\nYou're awesome!")

        break