def print_multiple(message: str, repeats: int):
    for i in range(repeats):  # Loop through the number of repeats
        print(message)  # Print the message each time

def main():
    message = input("Please type a message: ")  # Get the message from the user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get the number of repeats
    print_multiple(message, repeats)  # Call the function to print the message multiple times

if __name__ == '__main__':
    main()  # Call the main function to run the program
