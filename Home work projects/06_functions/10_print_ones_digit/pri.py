def print_ones_digit(num):
    print("The ones digit is", num % 10)  # % 10 gives the ones digit of num

def main():
    num = int(input("Enter a number: "))  # Get user input as an integer
    print_ones_digit(num)  # Call the function to print the ones digit

if __name__ == '__main__':
    main()  # Call the main function to run the program
