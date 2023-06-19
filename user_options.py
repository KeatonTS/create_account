from user_database import accounts


def sign_in():
    """Signs a user into their account according to the information found within the user_database"""
    while True:
        user = input("\nPlease enter your Email or Username: ").lower()
        password = input("Please enter your Password (Case Sensitive): ")
        for u_id in range(0, len(accounts)):
            if user == accounts[u_id][f"user_id-00{u_id}"]["username"] and password == accounts[u_id] \
                    [f"user_id-00{u_id}"]["password"] or user == accounts[u_id][f"user_id-00{u_id}"]["email"] \
                    and password == accounts[u_id][f"user_id-00{u_id}"]["password"]:
                print("\nYou've successfully logged in!")
                return
            else:
                print("Username or password is incorrect.")
                if input("Try again? ").lower() in ['y', 'yes', 'yeah']:
                    continue
                else:
                    return


def forgot_login(credential):
    """"Passes in the user input for whether they forgot their username or password"""
    email_check = input("\nPlease enter the email associated with your account: ").lower()
    security = input("Please enter this accounts' associated code word (Case Sensitive): ")
    print(look_up(email_check, security, credential))


def look_up(u_email, u_code, option):
    """Takes information from the 'forgot_login' function """
    account_audit = []
    account_id = 0
    # Separates list of accounts from the 'accounts' user database into the account_audit list to check a list a users
    # if the user information matches any existing account. The id goes up to catch subsequent users.
    for user in accounts:
        account_audit.append(user[f"user_id-00{account_id}"])
        account_id += 1
    account_found = False
    # Loops through account audit for matching information using account ID to catch a user.
    for info in range(len(account_audit)):
        # Verifying account ownership by checking the users code word and email for their registered account.
        if u_code == account_audit[info]["code"] and u_email == account_audit[info]["email"]:
            account_found = True
            if option in ["password", "pass", "pas", "p", "pw"]:
                while True:
                    new_pass = input("\nPlease enter a new password containing at least 8 characters"
                                     " (Case Sensitive): ")
                    if len(new_pass) >= 8:
                        confirm_pass = input("Re-enter your new password: ")
                        if confirm_pass == account_audit[info]["password"]:
                            print("New password matches current password. Please enter a different password or"
                                  " sign in with your current password.")
                            if input("\nDo you wish to sign in instead? ").lower() in ["y", "yes", "yeah", "yup"]:
                                sign_in()
                                return ""
                            else:
                                continue
                        elif confirm_pass == new_pass:
                            accounts[info][f"user_id-00{info}"]["password"] = new_pass
                            return "Your password has been reset!"
                        else:
                            print("The passwords did not match.")
                    else:
                        print("Your password isn't long enough.")

            elif option in ["username", "user", "name", "un"]:
                identity = accounts[info][f"user_id-00{info}"]["username"]
                return f"Your username is: {identity}\n"
    if not account_found:
        return "\nAn account could not be found."


