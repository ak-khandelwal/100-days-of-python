import os
bids = {}
currency_symbol = "$"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear 2>/dev/null')
def find_highest_bid(bids):
    max_bidder_name = ''
    max_amt = 0
    ties = []
    for name in bids:
        bid_amount = bids[name]
        if bid_amount > max_amt:
            max_bidder_name = name
            max_amt = bid_amount

    for name in bids:
        if name==max_bidder_name:
            continue
        if max_amt==bids[name]:
            ties.append(name)

    if not len(ties) == 0:
        ties.append(max_bidder_name)
        print(f'there is tie between maximum amount of {currency_symbol}{max_amt}.... ')
        for st in ties:
            print(st,end=', ')
    else:
        print(f"The winner is {max_bidder_name} with a bid of {currency_symbol}{max_amt}")
while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "+currency_symbol))
    if price <= 0:
        print("oops!! price cannot be zero or less than zero")
        print("please try again!!!")
        continue
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue=='no':
        find_highest_bid(bids)
        break
    else:
        clear()
