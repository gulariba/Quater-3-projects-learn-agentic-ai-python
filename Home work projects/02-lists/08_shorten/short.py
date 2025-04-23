"""
This program shortens the list by removing elements from the end until it has no more than MAX_LENGTH items.
It prints the removed elements one by one.
"""

MAX_LENGTH = 3

def trim_list_to_max_length(data_list):
    """Removes elements from the end of the list until it has no more than MAX_LENGTH items."""
    while len(data_list) > MAX_LENGTH:
        removed_item = data_list.pop()
        print("Removed item:", removed_item)

def collect_input():
    """Prompts the user to enter elements for the list and returns the complete list."""
    items = []
    user_input = input("Enter a value (or press enter to finish): ")
    while user_input != "":
        items.append(user_input)
        user_input = input("Enter a value (or press enter to finish): ")
    return items

def main():
    user_list = collect_input()
    trim_list_to_max_length(user_list)

if __name__ == '__main__':
    main()
