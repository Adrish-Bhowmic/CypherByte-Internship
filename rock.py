import random

def get_user_choice():
    """Get the user's choice of rock, paper, or scissors."""
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play a round of Rock, Paper, Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Main loop to play the game multiple times
def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")

if __name__ == "__main__":
    main()
