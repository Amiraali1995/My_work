import random

# Function to determine the winner
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

# Function to play the game
def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):
        return 'You win!'

    return 'You lose!'

# Call the play() function to start the game and print the result

print(play())
