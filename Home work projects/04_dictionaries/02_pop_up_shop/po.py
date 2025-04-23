def main():
    # Price list of fruits
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    # Ask user how many of each fruit they want
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want?: "))
        total_cost += price * amount_bought

    # Print the total bill
    print("Your total is $" + str(total_cost))


# Required line to run the main function
if __name__ == '__main__':
    main()
