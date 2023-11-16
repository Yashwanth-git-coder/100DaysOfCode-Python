import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

guess_number = random.randint(1, 100)
print(f"Psst, the correct answer is: {guess_number}")

choose_easy_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choose_easy_hard == "easy":
    attempts = 10
    for turns in range(attempts, 0, -1):
        actual_number = int(input("Make a guess: "))
        if actual_number > guess_number:
            print(f"You have {turns} attempts remaining to guess the number.")
            print("Too high.")
            print("Guess again.")
        elif actual_number < guess_number:
            print(f"You have {turns} attempts remaining to guess the number.")
            print("Too low.")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {guess_number}.")
            break
    else:
        print("You ran out of attempts. Game over!")

elif choose_easy_hard == "hard":
    attempts = 5
    for turns in range(attempts, 0, -1):
        actual_number = int(input("Make a guess: "))
        if actual_number > guess_number:
            print(f"You have {turns} attempts remaining to guess the number.")
            print("Too high.")
            print("Guess again.")
        elif actual_number < guess_number:
            print(f"You have {turns} attempts remaining to guess the number.")
            print("Too low.")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {guess_number}.")
            break
    else:
        print("You ran out of attempts. Game over!")

