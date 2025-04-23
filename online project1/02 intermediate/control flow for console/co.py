import random

def main():
    print("🎮 Welcome to the High-Low Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    # Random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Congrats! You guessed it right in {attempts} attempts.")
        except ValueError:
            print("⚠️ Please enter a valid number!")

if __name__ == "__main__":
    main()
