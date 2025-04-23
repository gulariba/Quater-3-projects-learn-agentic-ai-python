"""
Program to display the last element of a list.
Takes user input one element at a time.
"""

def display_last_value(data_list):
    """Prints the last item from the provided list."""
    print("Last item in the list is:", data_list[-1])
    # Alternate way (for clarity): print(data_list[len(data_list) - 1])

def collect_list():
    """Asks user to input items to create a list."""
    items = []
    item = input("Enter an item (or press enter to finish): ")
    while item != "":
        items.append(item)
        item = input("Enter an item (or press enter to finish): ")
    return items

def main():
    user_items = collect_list()
    display_last_value(user_items)

if __name__ == '__main__':
    main()
