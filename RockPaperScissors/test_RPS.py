from mainRPS import check_win

def test_empate():
    assert check_win("rock", "rock") == "It's a tie!"
    assert check_win("paper", "paper") == "It's a tie!"
    assert check_win("scissors", "scissors") == "It's a tie!"

def test_victoria_jugador():
    assert "You win!" in check_win("rock", "scissors")
    assert "You win!" in check_win("paper", "rock")
    assert "You win!" in check_win("scissors", "paper")

def test_derrota_jugador():
    assert "You lose!" in check_win("rock", "paper")
    assert "You lose!" in check_win("paper", "scissors")
    assert "You lose!" in check_win("scissors", "rock")

def test_mensajes_victoria():
    assert check_win("rock", "scissors") == "Rock wins against scissors! You win!"
    assert check_win("paper", "rock") == "Paper wins against rock! You win!"
    assert check_win("scissors", "paper") == "Scissors wins against paper! You win!"
    
def test_mensajes_derrota():
    assert check_win("rock", "paper") == "Paper wins against rock! You lose!"
    assert check_win("paper", "scissors") == "Scissors wins against paper! You lose!"
    assert check_win("scissors", "rock") == "Rock wins against scissors! You lose!"