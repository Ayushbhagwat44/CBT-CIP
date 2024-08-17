import random

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    choices = ["rock", "paper", "scissors"]
    
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    computer_choice = random.choice(choices)
    
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Play the game
play_game()
