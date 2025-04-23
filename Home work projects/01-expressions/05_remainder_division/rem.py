def main():
    # Ask the user for two numbers
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Perform integer division and get remainder
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    # Print the result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# This line calls the main function
if __name__ == '__main__':
    main()
