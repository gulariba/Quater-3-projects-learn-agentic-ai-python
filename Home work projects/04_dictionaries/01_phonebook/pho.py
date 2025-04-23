def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints all names and their associated numbers from the phonebook.
    """
    print("\n--- Phonebook Entries ---")
    for name in phonebook:
        print(name + " -> " + phonebook[name])


def lookup_numbers(phonebook):
    """
    Let the user search for phone numbers by name.
    """
    print("\n--- Phone Number Lookup ---")
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(phonebook[name])
        else:
            print(name + " is not in the phonebook")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# This required line runs the main function
if __name__ == '__main__':
    main()
