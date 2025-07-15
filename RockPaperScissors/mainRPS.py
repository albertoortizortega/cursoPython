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
    elif (player == "scissors"):
        if (computer == "rock"):
            return "Rock smashes scissors! You lose!"
        else:
            return "Scissors cut paper! You win!"
    elif (player == "rock"):
        if (computer == "paper"):
            return "Paper covers rock! You lose!"
        else:
            return "Rock smashes scissors! You win!"
    elif (player == "paper"):
        if (computer == "scissors"):
            return "Scissors cut paper! You lose!"
        else:
            return "Paper covers rock! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
