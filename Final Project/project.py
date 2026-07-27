# Import random
import random


# Store all red roulette numbers
RED_NUMBERS = {
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
}


# Run the roulette game
def main():

    # Give the player 100 fake chips
    balance = 100

    # Keep track of the game statistics
    spins = 0
    wins = 0
    losses = 0

    # Display the game title
    print("Welcome to Python Roulette!")
    print("This game uses fake chips only.")

    # Keep playing while the player still has chips
    while balance > 0:

        # Display the player's balance
        print()
        print(f"Balance: {balance} chips")

        # Display the available options
        print()
        print("Choose a bet:")
        print("1. Specific number")
        print("2. Red or black")
        print("3. Odd or even")
        print("4. Low or high")
        print("5. View statistics")
        print("6. Quit")

        # Ask the player to choose an option
        option = input("Option: ").strip()

        # Stop the game if the player chooses to quit
        if option == "6":
            break

        # Show the current statistics
        if option == "5":
            print_statistics(spins, wins, losses, balance)
            continue

        # Match each menu option with a bet type
        bet_types = {
            "1": "number",
            "2": "color",
            "3": "parity",
            "4": "range"
        }

        # Make sure the selected option is valid
        if option not in bet_types:
            print("Invalid option.")
            continue

        # Save the selected bet type
        bet_type = bet_types[option]

        # Ask the player for their bet choice
        bet_choice = input(get_choice_prompt(bet_type)).strip().lower()

        # Make sure the bet choice is valid
        if not validate_bet(bet_type, bet_choice):
            print("Invalid bet choice.")
            continue

        # Ask the player how many chips they want to bet
        try:
            amount = int(input("Bet amount: "))

        # Handle input that is not a whole number
        except ValueError:
            print("Bet amount must be a whole number.")
            continue

        # Make sure the bet amount is valid
        if amount <= 0 or amount > balance:
            print("Invalid bet amount.")
            continue

        # Spin the roulette wheel
        result = spin_wheel()

        # Calculate how many chips were won or lost
        winnings = calculate_winnings(
            bet_type,
            bet_choice,
            amount,
            result
        )

        # Update the player's balance
        balance += winnings

        # Add one completed spin
        spins += 1

        # Display the result of the spin
        print()
        print(format_result(result))

        # Update the statistics if the player won
        if winnings > 0:
            wins += 1
            print(f"You won {winnings} chips!")

        # Update the statistics if the player lost
        else:
            losses += 1
            print(f"You lost {amount} chips.")

    # Display the final game results
    print()
    print("Game over!")
    print_statistics(spins, wins, losses, balance)


# Spin the wheel
def spin_wheel():

    # Return a random roulette number
    return random.randint(0, 36)


# Find the color of a roulette number
def get_color(number):

    # Return green for zero
    if number == 0:
        return "green"

    # Return red for a red number
    if number in RED_NUMBERS:
        return "red"

    # Return black for all remaining numbers
    return "black"


# Check if a bet choice is valid
def validate_bet(bet_type, choice):

    # Check a specific-number bet
    if bet_type == "number":
        try:
            number = int(choice)
            return 0 <= number <= 36
        except ValueError:
            return False

    # Check a color bet
    if bet_type == "color":
        return choice in ["red", "black"]

    # Check an odd-or-even bet
    if bet_type == "parity":
        return choice in ["odd", "even"]

    # Check a low-or-high bet
    if bet_type == "range":
        return choice in ["low", "high"]

    # Return False for an unknown bet type
    return False


# Calculate the result of a bet
def calculate_winnings(bet_type, choice, amount, result):

    # Check a specific-number bet
    if bet_type == "number":

        # Pay 35 times the bet if the number matches
        if int(choice) == result:
            return amount * 35

        # Remove the bet amount if the number does not match
        return -amount

    # Make zero lose for all other bet types
    if result == 0:
        return -amount

    # Check a red-or-black bet
    if bet_type == "color":
        if choice == get_color(result):
            return amount

    # Check an odd-or-even bet
    elif bet_type == "parity":
        if choice == "odd" and result % 2 != 0:
            return amount

        if choice == "even" and result % 2 == 0:
            return amount

    # Check a low-or-high bet
    elif bet_type == "range":
        if choice == "low" and 1 <= result <= 18:
            return amount

        if choice == "high" and 19 <= result <= 36:
            return amount

    # Remove the bet amount if the player loses
    return -amount


# Format the result of the spin
def format_result(number):

    # Get the color of the number
    color = get_color(number)

    # Return the number and color
    return f"The ball landed on {number} — {color.upper()}!"


# Choose the correct prompt for each bet type
def get_choice_prompt(bet_type):

    # Prompt for a specific number
    if bet_type == "number":
        return "Choose a number from 0 to 36: "

    # Prompt for a color
    if bet_type == "color":
        return "Choose red or black: "

    # Prompt for odd or even
    if bet_type == "parity":
        return "Choose odd or even: "

    # Prompt for low or high
    return "Choose low or high: "


# Display the game statistics
def print_statistics(spins, wins, losses, balance):

    # Print each statistic
    print()
    print("Statistics")
    print(f"Spins: {spins}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Balance: {balance} chips")


# Start the program
if __name__ == "__main__":
    main()
