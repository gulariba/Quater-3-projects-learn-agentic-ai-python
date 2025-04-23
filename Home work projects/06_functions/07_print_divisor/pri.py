def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop through numbers from 1 to num inclusive
        if num % i == 0:  # If the number is divisible by i with no remainder
            print(i)

def main():
    num = int(input("Enter a number: "))  # Get user input
    print_divisors(num)  # Call the function to print divisors

if __name__ == '__main__':
    main()  # Call the main function to run the program
