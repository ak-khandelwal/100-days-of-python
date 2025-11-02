import random
import sys
def deal():
    return deck.pop()

def find_total(cards_list):
    total_score = 0
    ace_count = 0
    for card in cards_list:
        if not card.split('-')[1] == 'a':
            total_score+=map_the_score(card)
        else:
            ace_count+=1
    while ace_count>0:
        if total_score+11 <= 21:
            total_score+=11
        else:
            total_score+=1
        ace_count-=1
    return total_score

def reveal_cards(cards_list,total_score):
    '''reveal cards with total score'''
    for card in cards_list:
        print(card,end=' ')
    print('=',total_score)

def dealer_wins():
    print("dealer won the game !!!")

def player_wins():
    print('You win the game !!! 🥳🥳')

def player_lose():
    print('Oops, Better luck next time !!!')

def hit_stand_error():
    print('Please type either hit or stand')
def hit_stand_input():
    return input('hit/stand ')
def display_draw():
    print("Push! The game is a draw.")


ranks = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
suits = ['c', 'd', 'h', 's']  # clubs, diamonds, hearts, spades

deck = [f"{s}-{r}" for s in suits for r in ranks]
random.shuffle(deck)
def map_the_score(card):
    rank = card.split('-')[1]   # extract part after '-'
    return score_map[rank]
score_map = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'k':10,
    'q':10,
    'j':10,
}
is_black_jack = False
player_cards = [deal(),deal()]
computer_cards = [deal(),deal()]
player_total = find_total(player_cards)
computer_total = find_total(computer_cards)

while True:
    should_start = input('type "deal" to start the game ')
    if should_start=='deal':
        break

print('player cards:',end=' ')
reveal_cards(player_cards,player_total)

print('dealer cards:',end=' ')
print (computer_cards[0],"*")

    
is_hit = ""
if player_total==21:
    is_hit='stand'
    is_black_jack = True
while True:
    if not is_hit == 'stand':
        is_hit = hit_stand_input()
    if is_hit=='hit':
        break
    elif is_hit =='stand':
        break
    else:
        hit_stand_error()

while is_hit=='hit':
    player_cards.append(deal())
    player_total = find_total(player_cards)
    print('player cards:',end=' ')
    reveal_cards(player_cards,player_total)
    if player_total > 21:
        break
    elif player_total==21:
        is_hit='stand'
        break
    while True:
        is_hit = hit_stand_input()
        if is_hit=='hit':
            break
        elif is_hit =='stand':
            break
        else:
            hit_stand_error()

if player_total > 21:
    player_lose()
    sys.exit(0)


if is_hit == 'stand':
    computer_total = find_total(computer_cards)
    reveal_cards(computer_cards,computer_total)
    if is_black_jack and not computer_total==21:
        player_wins()
    elif computer_total>player_total:
        player_lose()
    else:
        while computer_total<17:
            computer_cards.append(deal())
            computer_total=find_total(computer_cards)
            print('dealer cards:',end=' ')
            reveal_cards(computer_cards,computer_total)
        if computer_total>21:
            player_wins()
        elif computer_total==player_total:
            display_draw()
        elif computer_total > player_total:
            player_lose()
        elif player_total > computer_total:
            player_wins()
        





