# Define the minimum height required for the ride
MINIMUM_HEIGHT: int = 50  # Units can be cm, inches, etc.

def main():
    # Ask the user for their height
    height = float(input("How tall are you? "))

    # Check if the user meets the height requirement
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# This line is required to call the main() function
if __name__ == '__main__':
    main()
