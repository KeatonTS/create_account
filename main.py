from user_model import Users
import user_options as option
users = Users()

on_site = True

# This loop mimics the action of being on a website and the sign in and sign up option being ever-present. The loop
# ends if none of the options were properly entered, in which case the 'on_site' variable closes, ending the program
while on_site:
    print("\nWelcome to BlankBook! The non-existent social media site where nothing happens!\n")
    choice = input("(Sign In / Sign Up) | If you've forgotten your login info, please type 'y': ").lower()
    if choice == "sign in":
        option.sign_in()
    elif choice == "sign up":
        users.sign_up()
    elif choice == "y":
        option.forgot_login(input("Which did you forget? (Username / Password): ").lower())
    else:
        on_site = False


