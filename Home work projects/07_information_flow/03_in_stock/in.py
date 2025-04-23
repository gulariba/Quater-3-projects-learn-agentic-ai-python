def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ")
    
    # Get the number of the fruit in stock
    stock = num_in_stock(fruit)
    
    # If the stock is 0, the fruit is not in stock
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# This function returns the number of fruit in stock.
def num_in_stock(fruit):
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # This fruit is not in stock
        return 0

# Run the main function
if __name__ == '__main__':
    main()
