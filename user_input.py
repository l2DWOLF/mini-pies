
# Logo Import
from logo import logo
# User Input
user_bill = float(input("Enter the Bill Amount\n"))
user_tip_amt = float(input("Enter Tip % Amount\n"))
user_split_amt = int(input("Enter individuals amount to split the bill?\n"))
# Calculations
final_tip = user_bill * user_tip_amt / 100
final_bill = user_bill + final_tip
final_p_person = final_bill / user_split_amt
credits_p_person = final_bill * 0.175 // user_split_amt
credits_donation = final_bill % user_split_amt
# Results 
print(f"Bill: ${user_bill}", f"Tip: ${final_tip:.2f}",
        f"Final Bill: ${final_bill:.2f}" + f" (Including {user_tip_amt}% Tip).",
        f"Bill Per Person: ${final_p_person:.2f} ({user_split_amt} Individuals).",
        f"-----\n{final_bill * 0.175} Credit Rewards, Per Person: {credits_p_person:.0f}",
        f"Credits Remainder Donated to FreeMeals: {credits_donation:.0f}", 
        sep="\n", end="\n -------------\n")
# Final Bill Confirmation 
user_confirmation = int(input("Confirm? \nEnter 1 to Confirm, 2 to Decline\n"))
if user_confirmation == 1:
    print("Submitting your Bill!")
    if(user_tip_amt > 10 and user_tip_amt < 15):
        print("Thank you.")
    elif (15 <= user_tip_amt < 20):
        print("Thank you!")
    elif(user_tip_amt >= 20):
        print("THANK YOU!")
    else:
        print("for electronic receipt enter mobile number.")
elif user_confirmation == 2:
    print("Resetting Order Information.")
else:
    print("Incorrect Entry, enter 1 to accept or 2 to declide")
print(logo)