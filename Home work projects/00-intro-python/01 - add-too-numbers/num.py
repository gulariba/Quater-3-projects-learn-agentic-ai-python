"""
Program: add2numbers
--------------------
This is a simple Python program to practice working with variables and user input.
The program asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")

    # Prompt the user to enter the first number
    num1 = input("Enter the first number: ")
    num1 = int(num1)  # Convert to integer

    # Prompt the user to enter the second number
    num2 = input("Enter the second number: ")
    num2 = int(num2)  # Convert to integer

    # Calculate the sum
    total = num1 + num2

    # Print the result with an appropriate message
    print("The total is " + str(total) + ".")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
