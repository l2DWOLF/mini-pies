from random import shuffle

class Card:
    def __init__(self, rank:str, suit:str):
        self.rank = rank
        self.suit = suit
# Methods
    def __str__(self):
        return f"Rank: {self.rank}, Suit: {self.suit}"
    def show(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        ranks = ["2", "3", "4" ,"5", "6", "7", "8", "9","J","Q","K","A"]
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def __str__(self):
        deck_list = [str(card) for card in self.cards]
        return str(deck_list)
    def shuffle_deck(self):
        shuffle(self.cards)
        

deck = Deck()
print(deck)

deck.shuffle_deck()
hmm = deck.cards
for card in hmm:
    print(card)
    
