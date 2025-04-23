"""
This program takes user input continuously and stores each entry in a list.
When the user presses enter without typing anything, the list is printed.
"""

def start_input_collection():
    """Collects user inputs into a list until a blank input is received."""
    entries = []
    while True:
        user_input = input("Type a value (or press enter to stop): ")
        if user_input == "":
            break
        entries.append(user_input)
    
    print("Collected values:", entries)

def main():
    start_input_collection()

if __name__ == '__main__':
    main()
