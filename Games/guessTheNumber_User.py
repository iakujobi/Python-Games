# User comes up with a random number and the computer guesses the number
import random


# This program accounts for lowercase and uppercase characters.
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    # As long as the user does not identify that CPU is correct,
    # continue to run
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high because low = high
        # converts ALL user inputs to lowercase
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)? "
        ).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guess your number, {guess}, correctly!")


computer_guess(10)
