import html
import requests 
from random import shuffle 
from utils import input_tools as itools

while True:
    q_amt = itools.get_menu_selection("Select the Amount of Questions (Max 30):\n", 1, 30)
    url = f'https://opentdb.com/api.php?amount={q_amt}'
    response = requests.get(url)
    if response.status_code == 200:
        res_json = response.json()
        results = res_json['results']
    else:
        print(f"Error with API, Restart game. \nStatus Code: {response.status_code}.")
        break

    count = 1
    score = 0
    for result in results:
        question = html.unescape(result['question'])
        correct_ans = result['correct_answer']
        all_ans = result['incorrect_answers']
        all_ans.append(correct_ans)
        shuffle(all_ans)
        
        print(f"Question {count}:\n-{question}" )
        ans_count = 1
        for ans in all_ans:
            print(f"[{ans_count}]: {html.unescape(ans)}")
            ans_count += 1
        count += 1
        user_choice = itools.get_menu_selection(f"Enter Answer Number: [1-{len(all_ans)}]\n", 1,len(all_ans)) - 1

        if correct_ans == all_ans[user_choice]:
            score +=1
            print("Correct Answer! \n")
        else:
            print(f"Wrong, The correct answer is: {correct_ans}.\n")
        print(f"Score: {score} / {q_amt} Questions.")
    game_loop = itools.get_menu_selection("Enter [1] to start a new Game.\nEnter [2] to Quit.\n", 1, 2)
    if game_loop == 1:
        print("Starting New Game!\n")
    else:
        print("Thanks for Playing :)")
        break