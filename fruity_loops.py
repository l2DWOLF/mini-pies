from random import randint
from utils import color_prt as cp

fruits = ["Apple", "Pear", "Grapes", "Pineapple", "Mango", "Watermelon", "Strawberry", "Cherry", "Peach", "Guarana", "Kiwi", "Lychee", "Orange", "Tangerine", "Rambutan", "Passionfruit", "Coconut"]
print(f"\033[96m")

def get_new_quit(msg):
    retry_quit = ""
    while retry_quit != "y" and retry_quit != "n":
        retry_quit = input(
            f"{msg}\n\033[93m Play Again? Y/N\n \033[0m").lower()
        if retry_quit != "y" and retry_quit != "n":
            print(f"\033[91m Invalid Input.. \033[0m")
            retry_quit = ""
    return retry_quit
def get_input():
    while True:
        char = input(f"\033[95m\nEnter your Guess:\n\033[0m").strip().lower()
        if len(char) == 1 and char.isalpha():
            return char
        print("Invalid Input, Letters only.")
def r_display():
    print(cp.print("cyan", f"""
================================
  ~~[ \033[94m Remaining Moves: {moves} \033[96m]~~
    ┍————- /ᐠ｡ꞈ｡ᐟ\ ——--——┑ 
          (      )       |
    ┕————(..)(..) ∫∫—-——-┙
    """))
    print(cp.print("yellow", f"--{u_scores}--"), end="")

def new_game(word, moves, u_scores, retry_quit):
    word = fruits[randint(0, len(fruits)-1)]
    moves = len(word)
    guess_bank.clear()
    u_scores = ["_ " for _ in word]
    retry_quit = ""
    return word, moves, u_scores, retry_quit

# Game Values
word = fruits[randint(0, len(fruits)-1)]
moves = len(word)
guess_bank = []
u_scores = ["_ " for _ in word]
retry_quit = ""

# Game Rules
print(
    f"<------------------------------->\n  \t\033[91m-=\033[92mFruits\033[93m Hangman\033[94m=-\033[0m")
print(cp.print("blue", f"RULES: You have {moves} Attempts to guess the type of fruit to feed the Owl-Cat."))
# Game Loop
running = True
while(running):
# Game Display
    r_display()
# User Input
    guess = get_input()
# Eval guess
    if(guess in guess_bank):
        print(cp.print("yellow", f"You've already guessed the letter [{guess}]!"))
    elif(guess in word.lower()):
        print(cp.print("green", f"[{guess}] is Correct!"))
        guess_bank.append(guess)
        for i in range(len(word)):
            if guess == word[i].lower():
                u_scores[i] = guess
    else:
        print(cp.print("red", f"Wrong..the letter [{guess}] isn't Correct."))
        moves -= 1
# Eval Win / Lose
    if ("_ " not in u_scores):
        print(cp.print("green", u_scores))
        retry_quit = get_new_quit(cp.print("green", f"Game Won! ~~~ \nNow Owl-Cat can eat the: {word}! "))
    if (moves < 1):
        print(cp.print("yellow", u_scores))
        retry_quit = get_new_quit(
            cp.print("red", f"Game Over! ~~~ \nThe fruit was: \033[93m{word}!\033[0m "))
# Eval New Game / Close Game
    if (retry_quit == "y"):
        word = fruits[randint(0, len(fruits)-1)]
        moves = len(word)
        guess_bank.clear()
        u_scores = ["_ " for _ in word]
        retry_quit = ""
    if (retry_quit == "n"):
        print(cp.print("purple", "Thanks for playing, See you soon!"))
        running = False