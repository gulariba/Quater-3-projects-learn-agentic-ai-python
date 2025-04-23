"""
This program collects user input to create a list, and then
prints the first element of that list.
"""

def show_first_item(data):
    """Displays the first item from the given list."""
    print("The first element is:", data[0])

def create_list():
    """Creates a list based on user input, one element at a time."""
    elements = []
    while True:
        entry = input("Add an item to the list (or press enter to finish): ")
        if entry == "":
            break
        elements.append(entry)
    return elements

def main():
    user_list = create_list()
    show_first_item(user_list)

# Start the program
if __name__ == '__main__':
    main()
