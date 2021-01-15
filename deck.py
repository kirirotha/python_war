import card
from random import shuffle

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                self.all_cards.append(card.Card(suit,rank))

    
    # def shuffle(self):
    #     shuffle(self.all_cards)

    
        