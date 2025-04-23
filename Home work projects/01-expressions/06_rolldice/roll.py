"""
Simulate rolling two dice, and print the results
of each roll along with the total.
"""

# Import the random module for simulating dice rolls
import random

# Number of sides on each die
NUM_SIDES: int = 6

def main():
    # Optional: Set a seed for predictable results (useful while testing)
    # random.seed(1)

    # Roll both dice (random numbers between 1 and 6)
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # Calculate the total
    total: int = die1 + die2

    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Required line to call the main function
if __name__ == '__main__':
    main()
