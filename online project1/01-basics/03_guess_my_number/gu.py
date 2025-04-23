import random

def main():
    # Generate the secret number between 1 and 99
    secret_number: int = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99...")

    # Ask the user for their first guess
    guess = int(input("Enter a guess: "))

    # Keep looping until they guess correctly
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Add a line space
        guess = int(input("Enter a new guess: "))

    # User guessed correctly
    print("Congrats! The number was: " + str(secret_number))

# Required to run the main function
if __name__ == '__main__':
    main()
