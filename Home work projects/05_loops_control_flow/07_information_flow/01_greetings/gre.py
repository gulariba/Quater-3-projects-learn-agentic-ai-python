def greet(name):
    return "Greetings " + name + "!"

def main():
    # Prompt the user for their name
    name = input("What's your name? ")
    # Call the greet function and print the result
    print(greet(name))

if __name__ == '__main__':
    main()
