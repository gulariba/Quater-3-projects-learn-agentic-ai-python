def main():
    print("Let's calculate the perimeter of a triangle!")

    # Get the 3 side lengths of the triangle
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print the result
    print("The perimeter of the triangle is " + str(perimeter))

if __name__ == '__main__':
    main()
