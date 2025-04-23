ADULT_AGE = 18  # U.S. age for adulthood

def is_adult(age: int):
    # Check if age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True
    return False

def main():
    # Prompt user for age input and convert to integer
    age = int(input("How old is this person?: "))
    # Print whether the person is an adult
    print(is_adult(age))

if __name__ == "__main__":
    main()
