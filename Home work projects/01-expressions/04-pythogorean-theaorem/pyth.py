import math  # Import the math library to use sqrt()

def main():
    # Get input for the two perpendicular sides from the user
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Use Pythagorean Theorem to calculate the hypotenuse
    bc: float = math.sqrt(ab**2 + ac**2)

    # Display the result
    print("The length of BC (the hypotenuse) is: " + str(bc))

# Required line to call main function
if __name__ == '__main__':
    main()
