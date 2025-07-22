import pytest
from mainRPS import get_choices, check_win
from unittest.mock import patch

options = ["rock", "paper", "scissors"]

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



# Tests with mocking

# Case 1: Valid input

@patch('builtins.input', side_effect=['rock'])
@patch('random.choice', return_value='paper')
def test_get_choices_valid_input(mock_random_choice, mock_input):
    choices = get_choices()
    assert choices == {"player": "rock", "computer": "paper"}
    mock_input.assert_called_once_with("Enter your choice (rock, paper, scissors): ")

# Case 2: Invalid input followed by valid input

@patch('builtins.input', side_effect=['invalid', 'rock'])
@patch('random.choice', return_value='scissors')
def test_get_choices_invalid_then_valid_input(mock_random_choice, mock_input):
    choices = get_choices()
    assert choices == {"player": "rock", "computer": "scissors"}
    assert mock_input.call_count == 2
    mock_input.assert_called_with("Enter your choice (rock, paper, scissors): ")