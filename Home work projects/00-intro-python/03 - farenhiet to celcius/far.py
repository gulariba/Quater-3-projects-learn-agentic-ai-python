"""
Program: fahrenheit_to_celsius
------------------------------
This program asks the user to input a temperature in Fahrenheit,
converts it to Celsius using the formula, and prints the result.
"""

def main():
    # Ask the user to input temperature in Fahrenheit
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    
    # Convert the input to float (to handle decimals)
    fahrenheit = float(fahrenheit)
    
    # Perform conversion
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Print the result
    print("Temperature:", str(fahrenheit) + "F =", str(celsius) + "C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
