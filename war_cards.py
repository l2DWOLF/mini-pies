
class Card:

    def __init__(self, rank:str, suit:str):
        self.rank = rank
        self.suit = suit
# Methods
    def __str__(self):
        return f"Rank: {self.rank}, Suit: {self.suit}\n"
    def show(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.card = []
        ranks = ["2", "3", "4" ,"5", "6", "7", "8", "9","J","Q","K","A"]
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    
cardA = Card("A", "Spades")
cardB = Card("K", "Hearts")

print(cardA.show())
print(cardB.show())
