from random import choices
from utils import ascii_chars as ac, color_prt as cp, cmn_pass as cpass

# Run App Loop
run_generator = True
pass_options = 5
pass_length = 0
while (run_generator):
    master_list = [ac.uppercase_list, ac.lowercase_list, 
                    ac.digits_list, ac.symbols_list]
    generated_pass = set()
# Get User Input
    while(pass_length<1):
        try:
            pass_length = int(input(cp.print("cyan", "Enter Password Length: \n")))
        except:
            pass_length = 0
            print("Invalid Input, Round&Positive Numbers only.")
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
    if (len(master_list) < 1):
        master_list.append(ac.uppercase_list)
# max combinations: chars ^ pass_length.
    total_chars = 0
    for char_list in master_list:
        total_chars += len(char_list)
    max_comb = total_chars ** pass_length
    print("Total Possible Combinations: ", max_comb)
    gen_max = input(cp.print(
        "blue", f"Would you like to generate all possible combinations? enter [y] to confirm:\n")).lower() == 'y'
    if (gen_max == True):
        pass_options = max_comb
    else:
        pass_options = 5
# Generate Password
    try:
        while(len(generated_pass) < pass_options):
            rand_pass = ""
            for _ in range(pass_length):
                list_type = choices(master_list)[0]
                rand_pass += choices(list_type)[0]
            generated_pass.add(rand_pass)
    except IndexError:
        print("Out of Range Dude")
    except Exception as e:
        print("Invalid Password Length.\n[Error]: ", e)
        print(f"{e.with_traceback}")
    finally:
        print(".-.-.-.-.-.-.-.-.")
# Print Generated Password, Select New or Quit.
    print(cp.print("cyan", f"Your Random Passwords list:\n"))
    pass_list = list(generated_pass)
    for i in range(0,len(pass_list)):
        print(cp.print("green", f"Password {i+1}: {pass_list[i]}"))
    for cmnpass in cpass.common_pass_list:
        if cmnpass in generated_pass:
            print(cp.print("cyan", f"Common Found: {cmnpass}"))
# Restart or Quit
    new_or_close = input(cp.print("yellow", "Enter any key to Generate a New Pass, Enter [quit] to Quit\n")).lower()
    if (new_or_close == "quit"):
        run_generator = False
    else:
        pass_length = 0