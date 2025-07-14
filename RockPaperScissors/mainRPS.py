import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    while player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"Player chose: {player} and Computer chose: {computer}")
    if(player == computer):
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors"):
        return "Rock smashes scissors! You win!"
    elif (player == "paper" and computer == "rock"):
        return "Paper covers rock! You win!"
    elif (player == "scissors" and computer == "paper"):
        return "Scissors cut paper! You win!"
    else:
        return "You lose! Better luck next time."

