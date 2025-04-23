def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    # Test the in_range function with an example
    print(in_range(5, 1, 10))  # Should return True
    print(in_range(15, 1, 10)) # Should return False

if __name__ == '__main__':
    main()
