from utils import rps_hands as hands
from random import randint

def disp_move(move, ptype):
    if (move == "1"):
        print(f"{ptype}: {hands.rock}")
    elif (move == "2"):
        print(f"{ptype} {hands.paper}")
    elif (move == "3"):
        print(f"{ptype} {hands.scissors}")

quit_greet = ['See you Soon!', 'Rate Us!', 'Leave Feedback!']
player_joker = 0
player_score = 0
player_points = 0
bot_score = 0
total_rounds = 1
tied_rounds = 0
playing = True

# game loop
while (playing):
# Player Move Input
    print(f"    ---===ROUND #{total_rounds}===---")
    player_move = input(
        f"Select your Move or Type [quit] to Quit, Type [reset] to Reset Scoreboard: \n[1 - Rock {hands.rock}  ] | [2 - Paper {hands.paper} ] | [3 - Scissors {hands.scissors}  ]\n").lower()

    if (player_move == "quit"):
        print("Closing Game, Thanks for Playing :)")
        print(quit_greet[randint(0, 2)])
        playing = False
        break
    elif (player_move == "reset"):
        print("Resetting Scoreboard & Stats.\n---===NEW GAME===---\n<--------------->")
        player_score = 0
        bot_score = 0
        tied_rounds = 0
        total_rounds = 1
    elif(player_move not in "123" or len(player_move) < 1):
        print("-=[Error]: Invalid Input - Try Again!=- \n------------------------")
        player_move = "Invalid"
    disp_move(f"{player_move}", "player")
# Bot move
    if (player_move != "Invalid" and player_move != "reset"):
        print("VS.")
        # Bot Move Randit
        bot_move = str(randint(1, 3))
        disp_move(f"{bot_move}", "bot")
# Game Result
        if (player_move == "1" and bot_move == "3"):
            print("Player Wins [Rock breaks Scissors]")
            player_score += 1
        elif (player_move == "2" and bot_move == "1"):
            print("Player Wins [Paper wraps Rock]")
            player_score += 1
        elif (player_move == "3" and bot_move == "2"):
            print("Player Wins [Scissors cuts Paper]")
            player_score += 1
        elif (player_move == bot_move):
            print("Tie")
            tied_rounds += 1
        else:
            if (bot_move == "1"):
                print("Bot Wins [Rock breaks Scissors]")
                bot_score += 1
            elif (bot_move == "2"):
                print("Bot Wins [Paper wraps Rock]")
                bot_score += 1
            elif (bot_move == "3"):
                print("Bot Wins [Scissors cuts Paper]")
                bot_score += 1
# Calculate Stats
        if (total_rounds - tied_rounds > 0):
            win_rate = player_score / (total_rounds - tied_rounds)
        else:
            win_rate = 0
# Print Scoreboard
        print(
            f"<----[Score Board - Round #{total_rounds}]---->\n   [Player = {player_score}] VS. [Bot = {bot_score}]. \n   [Ties: {tied_rounds}] - Win Rate: {win_rate*100:.2f}%\n<--------------------------->")
        total_rounds += 1