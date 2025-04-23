def main():
    print("Welcome to the Square Calculator!")

    # Ask the user to enter a number
    number = float(input("Please enter any number: "))

    # Calculate the square of the number
    square = number ** 2

    # Print the result
    print(f"The square of {number} is {square}.")

if __name__ == '__main__':
    main()
