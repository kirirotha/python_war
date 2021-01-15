'''
War Card Game
'''
import card
import deck

def deal(new_deck):
    player1=new_deck[1::2]
    player2=new_deck[0::2]
    return [player1,player2]

def play_round(hands):
    if hands[0][1].value > hands[1][0].value:
        card = hands[1].pop()
        hands[0].append(card)
    elif hands[0][1].value < hands[1][0].value:
        card = hands[0].pop()
        hands[1].append(card)
    else:
        war(hands)
    


new_deck = deck.Deck().all_cards
deck.shuffle(new_deck)

hands = deal(new_deck)
print(hands[0][0].value)
print(hands[1][0].value)
