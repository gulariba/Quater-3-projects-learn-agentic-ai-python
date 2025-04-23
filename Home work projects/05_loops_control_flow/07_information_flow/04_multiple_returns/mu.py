def get_user_info():
    # Ask the user for their first name
    first_name = input("What is your first name?: ")
    
    # Ask the user for their last name
    last_name = input("What is your last name?: ")
    
    # Ask the user for their email address
    email_address = input("What is your email address?: ")
    
    # Return all the gathered data as a tuple
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    # Call get_user_info to get the data
    user_data = get_user_info()
    
    # Print the user data
    print("Received the following user data:", user_data)

# Run the main function
if __name__ == "__main__":
    main()
