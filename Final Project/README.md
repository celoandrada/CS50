# Python Roulette Simulator

A command-line roulette game built in Python as my final project for Harvard's CS50P.

## Video Demo



## Features

- European roulette wheel (0–36)
- Start with 100 virtual chips
- Multiple betting options:
  - Specific number
  - Red or Black
  - Odd or Even
  - Low (1–18) or High (19–36)
- Live balance tracking
- Game statistics
- Input validation
- Unit tests with pytest

## Files

### project.py

Contains the complete game logic, including:

- roulette wheel simulation
- bet validation
- winnings calculation
- game statistics
- player interaction

### test_project.py

Contains pytest unit tests covering:

- roulette colors
- bet validation
- winnings calculations
- wheel randomness
- formatted output

### requirements.txt

Lists the project's dependency:

```
pytest
```

## Project Description

Python Roulette Simulator is a command-line game that recreates the experience of playing European roulette using virtual chips. The goal of this project was to practice Python programming by combining functions, loops, conditionals, user input, randomization, and unit testing into one complete application.

The player begins with 100 virtual chips and may continue playing until choosing to quit or running out of chips. Since the game uses virtual chips, no real money is involved.

Players can bet on:

- a specific number
- red or black
- odd or even
- low (1–18) or high (19–36)

Each round the roulette wheel is spun using Python's `random` module, the outcome is displayed, and the player's balance is updated based on the result.

The simulator also tracks:

- total spins
- wins
- losses
- remaining balance

A major design decision was separating the game into multiple helper functions instead of placing everything inside one large loop. This made the program easier to read, debug, maintain, and test with pytest.

Building this project allowed me to combine many of the concepts learned throughout CS50P, including:

- functions
- loops
- conditionals
- randomness
- error handling
- modular programming
- unit testing

into one complete interactive application.
