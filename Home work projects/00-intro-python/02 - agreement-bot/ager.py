"""
Program: favorite_animal
------------------------
This program asks the user for their favorite animal
and then prints a response including that animal.
"""

def main():
    # Ask the user for their favorite animal
    animal = input("What's your favorite animal? ")

    # Print a friendly response using the same animal
    print("My favorite animal is also " + animal + "!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
