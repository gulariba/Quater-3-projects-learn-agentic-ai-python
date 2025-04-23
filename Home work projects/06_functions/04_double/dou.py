def double(num: int):
    return num * 2  # Multiplies the input number by 2 and returns the result

def main():
    num = int(input("Enter a number: "))  # Prompts the user for a number
    num_times_2 = double(num)  # Calls double() to multiply the number by 2
    print("Double that is", num_times_2)  # Prints the result

if __name__ == '__main__':
    main()  # Calls the main function to run the program
