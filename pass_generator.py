from random import choices
from utils import ascii_chars as ac

# Run App Loop
run_generator = True
while (run_generator):
    master_list = [ac.uppercase_list, ac.lowercase_list, 
                    ac.digits_list, ac.symbols_list]
    generated_pass = ""
# Get User Input
    pass_length = int(input("Enter Password Length: \n"))
    pass_uppercase = input("Use Uppercase Letters?  [y/n] \n").lower() == 'y'
    pass_lowercase = input("Use Lowercase Letters? [y/n] \n").lower() == 'y'
    pass_digits = input("Use digits? [y/n] \n").lower() == 'y'
    pass_symbols = input("Use symbols? [y/n] \n").lower() == 'y'
# Use / Remove List Types
    if (pass_uppercase == False):
        master_list.remove(ac.uppercase_list)
    if (pass_lowercase == False):
        master_list.remove(ac.lowercase_list)
    if (pass_digits == False):
        master_list.remove(ac.digits_list)
    if (pass_symbols == False):
        master_list.remove(ac.symbols_list)
# Generate Password
    for _ in range(pass_length):
        list_type = choices(master_list)[0]
        generated_pass += choices(list_type)[0]
# Print Generated Password, Select New or Quit.
    print(f"Your Random Password is: {generated_pass}")
# Restart or Quit
    new_or_close = input(
        "Enter any key to Generate a New Pass, Enter [quit] to Quit\n").lower()
    if (new_or_close == "quit"):
        run_generator = False