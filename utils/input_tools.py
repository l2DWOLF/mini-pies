
def get_int(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print("Invalid Input, numbers only.")

def get_float(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except:
            print("Invalid Input, numbers only.")

def get_menu_selection(msg, min, max):
    while True:
        try:
            num = int(input(msg))
            if (num < min or num > max):
                print(msg)
            else:
                return num
        except:
            print(f"Must enter a Number between: {min} and {max}.")