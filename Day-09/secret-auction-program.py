from art import logo
print(logo)

bids_collected = {}
no_more_bids = False
while no_more_bids == False:
    bidder_name = input('What is your name?: ')
    bid_amount = int(input('How much is your bid: $'))
    bids_collected.update({bidder_name: bid_amount})

    # Check if there are more bidders
    bidder_check = input('Are there any other bidders? ')
    if bidder_check == 'no':
        no_more_bids = True

# Loop through dictionary and determine highest bidder
greater_bid = 0
for bidder in bids_collected:
    if bids_collected[bidder] > greater_bid:
        greater_bid = bids_collected[bidder]
        winner = bidder

print(f'The winner is {winner} with a bid of ${greater_bid}')
