

# weatehr if new bid need to be added
bids = {}


continue_bidding = True 
while continue_bidding:

    name = input("Enter your name: ")
    price = int(input("Enter your bid price: "))
    bids[name] = price
    should_continue = input("Are there any more bid? Type Yes or No. \n")

# compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    for bidder in  bidding_dictionary:
        bid_ammount = bidding_dictionary[bidder]
        highest_bid = 0
        highest_bidder = ""
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
find_highest_bidder(bids)

