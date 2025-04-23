"""
Program: mass_energy_equivalence
---------------------------------
This program calculates the energy equivalent of a given mass based on Einstein's famous equation.
"""

# Speed of light in meters per second
C = 299792458  # m/s

def main():
    print("Welcome to Einstein's mass-energy equivalence calculator!")

    # Ask user for mass in kilograms
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy using the formula E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the results
    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")

if __name__ == '__main__':
    main()
