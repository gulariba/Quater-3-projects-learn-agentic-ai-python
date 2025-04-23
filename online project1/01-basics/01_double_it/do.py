def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Double and print until value is >= 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

# Required line to call main function
if __name__ == '__main__':
    main()
