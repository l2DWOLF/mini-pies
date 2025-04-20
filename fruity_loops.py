from random import randint

fruits = ["Apple", "Pear", "Grapes", "Pineapple", "Mango", "Watermelon", "Strawberry", "Cherry", "Peach", "Guarana", "Kiwi", "Lychee", "Orange", "Tangerine", "Rambutan", "Passionfruit", "Coconut"]

def get_new_quit(msg):
    retry_quit = ""
    while retry_quit != "y" and retry_quit != "n":
        retry_quit = input(
            f"{msg}\nPlay Again? Y/N\n").lower()
        if retry_quit != "y" and retry_quit != "n":
            print("Invalid Input..")
            retry_quit = ""
    return retry_quit
def get_input():
    while True:
        char = input(f"\nEnter your Guess:\n").strip().lower()
        if len(char) == 1 and char.isalpha():
            return char
        print("Invalid Input, Letters only.")
def r_display():
    print(f"""
=============================
  ~~[Remaining Moves: {moves} ]~~
    ┍————- /ᐠ｡ꞈ｡ᐟ\ ——--——┑ 
          (      )       |
    ┕————(..)(..) ∫∫—-——-┙
    """)
    print("   --", end="")
    print(f"{u_scores}", end="")
    print("|--")
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
print("<------------------>\n  -=Fruits Hangman=-")
print(f"RULES: You have {moves} Attempts to guess the type of fruit to feed the Cat-Owl.")
# Game Loop
running = True
while(running):
# Game Display
    r_display()
# User Input
    guess = get_input()
# Eval guess
    if(guess in guess_bank):
        print(f"You've already guessed the letter [{guess}]!")
    elif(guess in word.lower()):
        print(f"[{guess}] is Correct!")
        guess_bank.append(guess)
        for i in range(len(word)):
            if guess == word[i].lower():
                u_scores[i] = guess
    else:
        print(f"Wrong..the letter [{guess}] isn't Correct.")
        moves -= 1
# Eval Win / Lose
    if ("_ " not in u_scores):
        print(u_scores)
        retry_quit = get_new_quit(f"Game Won! ~~~ \nNow Owl-Cat can eat the: {word}! ")
    if (moves < 1):
        print(u_scores)
        retry_quit = get_new_quit(f"Game Over! ~~~ \nThe fruit was: {word}! ")
# Eval New Game / Close Game
    if (retry_quit == "y"):
        word = fruits[randint(0, len(fruits)-1)]
        moves = len(word)
        guess_bank.clear()
        u_scores = ["_ " for _ in word]
        retry_quit = ""
    if (retry_quit == "n"):
        print("Thanks for playing, See you soon!")
        running = False
