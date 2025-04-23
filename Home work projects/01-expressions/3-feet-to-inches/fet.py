"""
An example program to convert feet to inches using constants.
"""

INCHES_IN_FOOT: int = 12  # 1 foot = 12 inches

def main():
    feet: float = float(input("Enter number of feet: "))  # Input from user
    inches: float = feet * INCHES_IN_FOOT  # Conversion logic
    print("That is", inches, "inches!")  # Display result

# This provided line is required at the end of the Python file
# to call the main() function.
if __name__ == '__main__':
    main()
