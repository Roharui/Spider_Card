
c_order = {'k' : 0,'q' : 1,'j' : 2,'10' : 3,'9' : 4,'8' : 5,'7' : 6,
'6' : 7,'5' : 8,'4' : 9,'3' : 10,'2' : 11,'a' : 12}

class Deck:
    global c_order
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return str(self.cards)

    def addDeck(self, deck):
        self.cards += deck.cards

    def addCard(self, card):
        self.cards.append(card)

    def firstCard(self):
        return c_order[self.cards[0]]
    
    def lastCard(self):
        return c_order[self.cards[-1]]

    def canAddDeck(self, deck):
        if len(self.cards) == 0:
            return True
        if self.lastCard() + 1 == deck.firstCard():
            return True 
        else:
            return False
    
    def canAddCard(self, card):
        if len(self.cards) == 0:
            return True
        if self.lastCard() + 1 == c_order[card]:
            return True 
        return False

    def divide(self, num):
        divide_num = len(self.cards) - num
        a = self.cards[divide_num:]
        self.cards = self.cards[:divide_num]
        result = Deck()
        result.cards = a
        return result

    
    

def makeDeck(decks):
    result = []
    _ = Deck()
    for i in decks:
        if _.canAddCard(i):
            _.addCard(i)
        else:
            result.append(_)
            _ = Deck()
            _.addCard(i)
    result.append(_)
    return result

def tmpFuc_input():
    while True:
        a = input('Enter - ')
        if a in c_order.keys():
            _ = Deck()
            _.cards = [a]
            return _

if __name__ == '__main__':
    a = ['10', '9', '7']
    b = makeDeck(a)
    for i in b:
        print(repr(i), end=' ')