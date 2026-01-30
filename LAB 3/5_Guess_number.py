"""
Guess the number
Make a game that randomly selects a secret number between 1 and 100. Then you try to guess it. If you guess too low or too high, the game will tell you about it. After you guess correctly, the game will print the number of guesses.
# Randomize a secret number
secret = random.randint(1, 100)
Example:
Welcome to Guess the Number! I'm thinking of a number between 1 and 100. Can you guess what it is?
Guess: 40
No, it's too low!
Guess: 55
No, it's too high!
Guess: 51
That's right!! You did it in 3 guesses.
"""
import random
print("Welcome to Guess the Number!")
number = random.randint(1, 100)
print(" I'm thinking of a number between 1 and 100. Can you guess what it is? ")
guess = 0
counter = 0
try:
    while guess != number:
        guess = int(input("\nGuess(1 -100): "))
        if 0 < guess <= 100:
            if guess == number:
                print(f"Congratulations! You guessed the number in {counter} guesses! ")
                break
            elif guess > number:
                print("No, it's high!")
            elif guess < number:
                print("No, it's low!")
            counter += 1
        else:
            print("Enter a valid number!")
except ValueError:
    print(f"Invalid input!!!")