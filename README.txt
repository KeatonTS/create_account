This program is my first personal project that temporarily saves login information which is forgotten after the program ends. 
This program depends on 4 modules:

main - This contains the general loop that keeps the program going and is linked to user_model and user_options
user_database - This stores the users created in the program after choosing to sign up
user_model - This requests the necessary user information and inserts the account into the user database in a list with dictionaries
user_options - This allows a user to sign in, or reset a password, using the user_database to check against the user provided credentials

This sign up/sign in project contains a few features:
* Checks and determines if an email is valid or not, also will not allow duplicate emails to sign up
* Checks and determines if a username is already taken and if it contains at least 3 character
* Makes sure a users password contains at least 8 characters
* Has a security code for purposes involving account recovery
* Can reset your password and retrieve a username using the security code

After logging in, nothing happens.

This was made to practice my ability to use and understand classes and objects, utilizing different modules,
and working with various types of code. I focused on this project because I'm aiming to specifically create programs
that manages users and user activity/options. I also chose this because I knew it would be challenging to get the logic
correct and it would need to be intricately built to ensure it works properly between each file.