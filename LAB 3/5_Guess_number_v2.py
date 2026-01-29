"""
Guess the number
Version 2: print if you're close if you guess at most 5 away from the correct answer.
'Now it starts burning!'
"""
import random
print("Welcome to Guess the Number!")
number = random.randint(1, 100)
print(" I'm thinking of a number between 1 and 100. Can you guess what it is? ")
guess = 0
counter = 0
while guess != number:
    try:
        guess = int(input("\nGuess: "))
        counter += 1
        if guess == number:
            print(f"Congratulations! You guessed the number in {counter} guesses! ")
            break
        elif abs(guess-number) < 5:
            print(f"Now, it's burning!")
        elif guess > number:
           print("No, it's high!")
        elif guess < number:
           print("No, it's low!")

    except ValueError:
        print("Please enter a valid number!")