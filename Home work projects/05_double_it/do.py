def main():
    # Ask the user for an initial number
    curr_value = int(input("Enter a number: "))

    # Loop while the current value is less than 100
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the value
        print(curr_value, end=" ")  # Print the doubled value with a space

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
