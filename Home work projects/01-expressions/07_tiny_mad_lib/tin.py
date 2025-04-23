# Starting part of the sentence
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # Ask user for inputs
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Form and print the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Required line to call the main function
if __name__ == '__main__':
    main()
