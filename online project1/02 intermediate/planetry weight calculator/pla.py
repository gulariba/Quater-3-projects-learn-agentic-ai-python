def main():
    print("🌍 Welcome to the Planetary Weight Calculator! 🌌")
    
    try:
        weight = float(input("Enter your weight on Earth (in kg): "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        return

    print("\nSelect a planet:")
    print("1. Mercury")
    print("2. Venus")
    print("3. Mars")
    print("4. Jupiter")
    print("5. Saturn")
    print("6. Uranus")
    print("7. Neptune")

    choice = input("Enter the number of your chosen planet: ")

    gravity_multipliers = {
        "1": ("Mercury", 0.38),
        "2": ("Venus", 0.91),
        "3": ("Mars", 0.38),
        "4": ("Jupiter", 2.34),
        "5": ("Saturn", 1.06),
        "6": ("Uranus", 0.92),
        "7": ("Neptune", 1.19)
    }

    if choice in gravity_multipliers:
        planet, multiplier = gravity_multipliers[choice]
        new_weight = weight * multiplier
        print(f"\n🌠 Your weight on {planet} would be approximately {new_weight:.2f} kg.")
    else:
        print("❌ Invalid selection! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
