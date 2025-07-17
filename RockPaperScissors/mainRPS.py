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
    
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if wins[player] == computer:
        return f"{player.title()} wins against {computer}! You win!"
    else:
        return f"{computer.title()} wins against {player}! You lose!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
