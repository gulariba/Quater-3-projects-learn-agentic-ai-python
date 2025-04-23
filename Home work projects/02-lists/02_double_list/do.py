def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i
        numbers[i] = elem_at_index * 2  # Double the value at index i

    print(numbers)  # Print the updated list

if __name__ == '__main__':
    main()
