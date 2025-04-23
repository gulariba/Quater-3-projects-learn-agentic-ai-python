MAX_TERM_VALUE = 10000  # Set maximum value for Fibonacci numbers

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number

    # Loop until the current Fibonacci number exceeds MAX_TERM_VALUE
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print the current Fibonacci number with space
        term_after_next = curr_term + next_term  # Calculate next term in the sequence
        curr_term = next_term  # Update current term to the next term
        next_term = term_after_next  # Update the next term for the next iteration

# This is the standard Python boilerplate to run the program
if __name__ == '__main__':
    main()
