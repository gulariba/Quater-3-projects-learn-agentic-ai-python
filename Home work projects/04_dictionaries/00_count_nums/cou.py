def get_user_numbers():
    """
    Ask the user for numbers and store them in a list.
    The loop ends when the user enters a blank input.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers


def count_nums(num_lst):
    """
    Count how many times each number appears in the list using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict


def print_counts(num_dict):
    """
    Print each number and how many times it appears.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Required Python boilerplate
if __name__ == '__main__':
    main()
