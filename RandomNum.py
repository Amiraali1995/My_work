import random
def guess(x):
    random_number = random.randint(1, x)  # Generate a random number between 1 and x
    guess = 0  # Initialize the user's guess variable
    # Keep looping until the user's guess matches the random number
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))  # Ask the user for their guess
        if guess < random_number:
            print("Sorry, Guess again. Too low.")
        elif guess > random_number:
            print("Sorry, Guess again. Too High.")
    print(f"Yay, Congrats. You have guessed the number {random_number}.")
# Call the guess function with the maximum range of 10
guess(10)
