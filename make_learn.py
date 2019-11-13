
from deck import Deck, makeDeck, deckList

class Make:
    def __init__(self, data, hidden=[5,5,5,5,4,4,4,4,4,4]):
        self.data = data
        self.count = 0
        self.deck = []
        self.hidden = [[],[],[],[],[],[],[],[],[],[]]
        self.set_Game()
        for i in range(10):
            _ = self.data.pop(0)
            self.deck.append(makeDeck([_]))

        self.epoc = 0
        self.move_count = 0
        self.complete_deck = 0
        self.done = True
        self.finish = False

    def set_Game(self):
        for i in range(44):
            _ = Deck()
            _.addCard(self.data.pop(0))
            self.hidden[i%10].append(_)
            
    def elseDeck(self, num):
        if num == -1:
            return self.deck
        if num == 0:
            return self.deck[1:]
        elif num == 9:
            return self.deck[:9]
        else:
            return self.deck[:num] + self.deck[num+1:]

    def print_Card_move(self, i, j):
        print('{0} -> {1}'.format(self.deck.index(i) + 1, self.deck.index(j) + 1))
        self.move_count += 1

    def print_Card_move_n(self, i, j):
        print('{0} -> {1}'.format(self.deck.index(i) + 1, j + 1))
        self.move_count += 1

    def move_1_1(self, i, flist):
        for j in flist:
            if j[-1].canAddDeck(i[-1]):
                j[-1].addDeck(i.pop())
                self.print_Card_move(i,j)
                return True
        return False

    def move_1_2(self, i, emlist):
        for j in emlist:
            if len(self.hidden[self.deck.index(j)]) == 0 and \
                (len(self.hidden[self.deck.index(i)]) != 0 or len(i) > 1):
                j.append(i.pop())
                self.print_Card_move(i,j)
                return True
        return False

    def checkEmpty(self, num):
        flist = []
        emlist = []
        for j in self.elseDeck(num):
            if len(j) == 0:
                emlist.append(j)
            else:
                flist.append(j)
        return (flist, emlist)

    def move_1(self, i, num):
        flist, emlist = self.checkEmpty(num)
        result = False
        while True:
            if len(i) == 0:
                if self.refresh(num, i):
                    result = True
                    continue
            elif self.king(i, num):
                flist, emlist = self.checkEmpty(num)
                return True
            elif self.move_1_1(i, flist):
                flist, emlist = self.checkEmpty(num)
                result = True
                continue
            elif self.move_1_2(i, emlist):
                flist, emlist = self.checkEmpty(num)
                result = True
                continue
            return result

    def king(self, i, num):
        if i[-1].firstCard() != 0:
            return False
        for j in self.checkEmpty(num)[0]:
            __ = j[-1]
            _ = i[-1]
            if __.lastCard() == 12 and __.firstCard() <= _.lastCard():
                tmp = __.divide(12 - _.lastCard())
                _.addDeck(tmp)
                self.print_Card_move_n(i,num)
                return True
        return False

    def move(self):
        print('=============={0}'.format(self.epoc))
        self.show()
        print()
        result = False
        for num, i in enumerate(self.deck):
            result = result or self.move_1(i, num)
            self.clean()
        self.epoc += 1
        return result

    def clean(self):
        for i in self.checkEmpty(-1)[0]:
            if i[-1].firstCard() == 0 and i[-1].lastCard() == 12: 
                i.pop()
                self.complete_deck += 1

    def refresh(self, num, i):
        if len(self.hidden[num]) == 0:
            return False
        #self.hidden[num] -= 1
        #print('{0}번째 카드 번호를 입력해 주세요'.format(num + 1))
        i.append(self.hidden[num].pop(0))
        return True

    def tolab(self):
        flist, emlist = self.checkEmpty(-1)
        if len(emlist) == 0:
            return False
        for i in flist:
            for j in emlist:
                j.append(i[-1].divide(1))
                flist, emlist = self.checkEmpty(-1)
                if len(i[-1].cards) == 1:
                    break
        if len(emlist) > 0:
            return True
        return False
                
    def lab(self):
        if self.complete_deck == 8:
            self.done = False
            self.finish = True
            return
        if self.count == 5 or self.tolab():
            self.done = False
            return
        self.count += 1
        print("덮어쓰기 시작")
        ###tmp
        for i in self.deck:
            _ = Deck()
            _.cards.append(self.data.pop(0))
            if i[-1].canAddDeck(_):
                i[-1].addDeck(_)
            else:
                i.append(_)
        
    def show(self):
        for num, i in enumerate(self.deck):
            pass
            print(num + 1, len(self.hidden[num]),repr(i))
        print()
    
    def showLine(self, i):
        num = self.deck.index(i)
        print(num + 1, len(self.hidden[num]), repr(i))
        print()

    def final(self):
        for i in self.deck:
            for j in i:
                print(repr(j), end='')
            print(', ', end='')
        print()
        print(self.hidden)

    def start(self):
        while self.done:
            while self.move():
                pass
            self.lab()
        return (self.move_count, self.finish)

if __name__ == '__main__':
    data = deckList()
    #hidden = [4, 5, 5, 4, 4, 3, 3, 4, 4, 2]
    a = Make(data)
    a.start()
