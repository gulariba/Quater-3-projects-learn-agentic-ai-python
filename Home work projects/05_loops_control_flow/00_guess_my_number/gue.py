import random

def main():
    # Randomly choose a number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Ask for the user's first guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Blank line for clarity
        guess = int(input("Enter a new guess: "))  # Try again
    
    # Congratulate the user
    print("Congrats! The number was: " + str(secret_number))

# Required line to start the program
if __name__ == '__main__':
    main()
