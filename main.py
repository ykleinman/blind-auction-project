from replit import clear
from art import logo

user_bid = {}

#STEP-1: Show Logo from art.py
print(logo)

game_over = False
while not game_over:
    #STEP-2: Ask for name input
    name = input("What is your name? ")

    #STEP-3: Ask for bid price
    bid_price = int(input("What is your bid? $"))

    def activate_bidder(user_name, bid):
        #STEP-4: Add name and bid into a dictionary as the key and value.
        user_bid[name] = bid_price

    activate_bidder(user_name=name, bid=bid_price)

    #STEP-5:
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'\n")

    if other_bidders == "yes":
        clear()
        activate_bidder(user_name=name, bid=bid_price)
    elif other_bidders == "no":
        for user in user_bid:
            winning_bid = 0
            final_bid = user_bid[user]
            if final_bid > winning_bid:
                winning_bid = final_bid
        print(f"The winner is {user} with a bid of ${winning_bid}")
        game_over = True
