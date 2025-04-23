import random

# Constants
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=' ')  # Print numbers on the same line with a space

# This provided line is required to call the main() function
if __name__ == '__main__':
    main()
