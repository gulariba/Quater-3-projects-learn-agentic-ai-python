"""
Mutability in Python

This program shows how lists (a mutable data type) can be changed inside functions
without needing to return them.
"""

def add_multiple_copies(target_list, item):
    """Adds the same item 3 times to the list (mutable effect)."""
    for _ in range(3):
        target_list.append(item)

# Main part of the program
def main():
    message = input("Enter a message to copy: ")
    
    copies = []  # Starting with an empty list

    print("List before:", copies)

    add_multiple_copies(copies, message)

    print("List after:", copies)

if __name__ == "__main__":
    main()
