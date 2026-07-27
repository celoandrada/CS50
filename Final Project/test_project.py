# Import pytest
import pytest

# Import the functions to test
from project import (
    calculate_winnings,
    format_result,
    get_color,
    spin_wheel,
    validate_bet
)


# Test the color of different roulette numbers
def test_get_color():
    assert get_color(0) == "green"
    assert get_color(1) == "red"
    assert get_color(2) == "black"
    assert get_color(36) == "red"


# Test valid roulette bets
def test_validate_bet_valid():
    assert validate_bet("number", "0") == True
    assert validate_bet("number", "36") == True
    assert validate_bet("color", "red") == True
    assert validate_bet("parity", "even") == True
    assert validate_bet("range", "high") == True


# Test invalid roulette bets
def test_validate_bet_invalid():
    assert validate_bet("number", "37") == False
    assert validate_bet("number", "cat") == False
    assert validate_bet("color", "green") == False
    assert validate_bet("parity", "middle") == False
    assert validate_bet("range", "medium") == False


# Test winning and losing specific-number bets
def test_number_winnings():
    assert calculate_winnings("number", "17", 10, 17) == 350
    assert calculate_winnings("number", "17", 10, 18) == -10
    assert calculate_winnings("number", "0", 5, 0) == 175


# Test winning and losing color bets
def test_color_winnings():
    assert calculate_winnings("color", "red", 10, 1) == 10
    assert calculate_winnings("color", "black", 10, 1) == -10
    assert calculate_winnings("color", "red", 10, 0) == -10


# Test winning and losing odd-or-even bets
def test_parity_winnings():
    assert calculate_winnings("parity", "odd", 10, 7) == 10
    assert calculate_winnings("parity", "even", 10, 8) == 10
    assert calculate_winnings("parity", "even", 10, 7) == -10
    assert calculate_winnings("parity", "even", 10, 0) == -10


# Test winning and losing low-or-high bets
def test_range_winnings():
    assert calculate_winnings("range", "low", 10, 18) == 10
    assert calculate_winnings("range", "high", 10, 19) == 10
    assert calculate_winnings("range", "low", 10, 20) == -10


# Test how roulette results are displayed
def test_format_result():
    assert format_result(0) == "The ball landed on 0 — GREEN!"
    assert format_result(1) == "The ball landed on 1 — RED!"
    assert format_result(2) == "The ball landed on 2 — BLACK!"


# Test that the wheel only returns numbers from 0 to 36
def test_spin_wheel():
    for _ in range(100):
        result = spin_wheel()
        assert 0 <= result <= 36
