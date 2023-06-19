from user_database import accounts


class Users:

    def __init__(self):
        self.account_id = 0

    def sign_up(self):
        """Creates an account for a user and stores it within the user_database module in the form of a dictionary
         within a list."""
        # Checks to ensure if a proper email has been entered and doesn't already exist withing the database
        while True:
            email = input("\nPlease enter a valid email: ").lower()
            if "@" in email and ".com" in email or ".org" in email or ".net" in email or ".edu" in email:
                list_of_emails = []
                for num in range(0, len(accounts)):
                    list_of_emails.append(accounts[num][f"user_id-00{num}"]["email"])
                if email in list_of_emails:
                    print("This email is already in use.")
                else:
                    break
            else:
                print("Invalid email address.")
        # Checks to ensure if a proper username has been entered and doesn't already exist within the database
        # Also checks if the username contains a certain number of characters
        while True:
            username = input("Please enter a username: ").lower()
            if len(username) < 3:
                print("Usernames must contain at least 3 characters.\n")
            elif len(accounts) > 0:
                # Checks if username is in use
                list_of_names = []
                for num in range(0, len(accounts)):
                    list_of_names.append(accounts[num][f"user_id-00{num}"]["username"])
                if username not in list_of_names:
                    self.account_id += 1
                    break
                else:
                    print("This username is already taken...")
            else:
                break
        # Checks if a password contains at least 8 characters
        while True:
            password = input("Please enter a password containing at least 8 characters (Case Sensitive): ")
            if len(password) >= 8:
                break
            else:
                print("Your password isn't long enough.")
        # Checks if a users security/code word contains at least 4 characters
        while True:
            code_word = input("Please enter a code word for your accounts' security. Code words must have at least "
                              "4 characters but can be anything you wish"
                              " (Case Sensitive): ")
            if len(code_word) < 4:
                print("Your code word is not long enough.\n")
            else:
                break
        # Adds user to the user_database in this format. Users are given account IDs in subsequent numerical order to
        # assist in user search and login methods
        user_info = {f"user_id-00{self.account_id}": {
                "email": email,
                "username": username,
                "password": password,
                "code": code_word,
                    }}
        accounts.append(user_info)
        print("\nAccount Has Been Created Successfully!\n")
