def main():
    print("🎮 Welcome to the Index Game!")
    
    words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
    
    while True:
        try:
            index = int(input(f"\nEnter an index between 0 and {len(words) - 1}: "))
            if 0 <= index < len(words):
                print(f"✅ The word at index {index} is: {words[index]}")
            else:
                print("❌ Game Over! Invalid index.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
