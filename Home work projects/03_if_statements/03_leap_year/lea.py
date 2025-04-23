def main():
    # Get the year to check from the user
    year = int(input("Please input a year: "))

    # Check if the year is a leap year using the leap year rules
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Call the main function
if __name__ == '__main__':
    main()
