"""
Program: better_dice_simulator
------------------------------
Simulates rolling two dice, three times.
Demonstrates the concept of variable scope in functions.
"""

import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Rolls two dice and prints their individual values and the total.
    This function has its own local scope for die1 and die2.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled a {die1} and a {die2} → Total: {total}")

def main():
    # This die1 is separate from the one inside roll_dice()
    die1 = 10
    print(f"Value of die1 in main() before rolling: {die1}\n")

    print("Rolling dice three times:\n")
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"\nValue of die1 in main() after rolling: {die1}")

if __name__ == '__main__':
    main()
