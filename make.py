
from deck import Deck, makeDeck, tmpFuc_input

class Make:
    def __init__(self, data, hidden=[5,5,5,5,4,4,4,4,4,4]):
        self.count = 0
        self.deck = []
        for i in data:
            self.deck.append(makeDeck(i))
        self.hidden = hidden

        self.epoc = 0

    def elseDeck(self, num):
        if num == -1:
            return self.deck
        if num == 0:
            return self.deck[1:]
        elif num == 9:
            return self.deck[:9]
        else:
            return self.deck[:num] + self.deck[num+1:]

    def move_1_1(self, i, flist):
        for j in flist:
            if j[-1].canAddDeck(i[-1]):
                j[-1].addDeck(i.pop())
                print('{0} -> {1}'.format(self.deck.index(i) + 1, self.deck.index(j) + 1))
                return True
        return False

    def move_1_2(self, i, emlist):
        for j in emlist:
            if self.hidden[self.deck.index(j)] == 0 and self.hidden[self.deck.index(i)] != 0:
                j.append(i.pop())
                print('{0} -> {1}'.format(self.deck.index(i) + 1, self.deck.index(j) + 1))
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
                result = True
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

        '''
        result = False
        moved = True
        while moved:
            moved = False
            for j in self.elseDeck(num):
                #비어있는 칸이 있을때
                #print('i = {0}, j = {1}'.format(num, self.deck.index(j)))
                if len(j) == 0:
                    #print('비어있는 칸')
                    if len(i) > 1 and self.hidden[self.deck.index(j)] == 0:
                        self.showLine(i)
                        j.append(i.pop())
                        self.showLine(j)
                        result = True
                        moved = True
                        break
                #팔아넘길게 없을때
                elif len(i) == 0:
                    #print('팔게 없음')
                    moved = False
                    break
                #팔수 있을때.
                elif j[-1].canAddDeck(i[-1]):
                    #print('팔수 있음')
                    self.showLine(i)
                    j[-1].addDeck(i.pop())
                    self.showLine(j)
                    result = True
                    moved = True
                    break
                else:
                    continue
        return result
        '''
    '''
    def move_2(self, i, num):
        flist, emlist = self.checkEmpty(num)
        for j in flist:
            if len(j) > 1:
                self.showLine(j)
                i.append(j.pop())
                self.showLine(i)
                return True
        for j in flist:
            if self.hidden[self.deck.index(j)] > 0:
                self.showLine(j)
                i.append(j.pop())
                self.showLine(i)
                return True
        return False
    '''

    def king(self, i, num):
        if i[-1].firstCard() != 0:
            return False
        for j in self.checkEmpty(num)[0]:
            __ = j[-1]
            _ = i[-1]
            if __.lastCard() == 12 and __.firstCard() <= _.lastCard():
                tmp = __.divide(12 - _.lastCard())
                _.addDeck(tmp)
                print('{0} -> {1} - King'.format(self.deck.index(j) + 1, num + 1))
                return True
        return False

    def move(self):
        result = False
        #print('=============={0}'.format(self.epoc))
        self.show()
        print()
        result = False
        for num, i in enumerate(self.deck):
            result = result or self.move_1(i, num)
            self.clean()
        self.epoc += 1
        return result
            
        '''
        result = False
        king = False
        for i in self.deck:
            if len(i) == 0: continue
            il = len(i)
            _ = i[-1]
            if _.firstCard() == 0: king = True
            if _.lastCard() == 12: continue
            for j in self.deck:
                if len(j) == 0:
                    if il > 1:
                        self.show()
                        i.pop()
                        j.append(_)
                    continue
                __ = j[-1]
                if __.firstCard == 0: continue
                if king and (__.lastCard() == 12 and __.firstCard() <= _.lastCard()):
                    pass
                if __.firstCard() == _.lastCard() + 1:
                    result = True
                    j.pop()
                    _.addDeck(__)
                    self.show()
                    break
            self.clean()
            king = False
        return result
        '''

    def clean(self):
        for i in self.checkEmpty(-1)[0]:
            if i[-1].firstCard() == 0 and i[-1].lastCard() == 12: 
                i.pop()

    def refresh(self, num, i):
        if self.hidden[num] == 0:
            return False
        self.hidden[num] -= 1
        print('{0}번째 카드 번호를 입력해 주세요'.format(num + 1))
        i.append(tmpFuc_input())
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
        if self.count == 5 or self.tolab():
            print('더이상 진행할수 없습니다.')
            exit()
        self.count += 1
        print("덮어쓰기 시작")
        ###tmp
        for num, i in enumerate(self.deck):
            print('{0}번째 입력하기.'.format(num + 1))
            _ = tmpFuc_input()
            if i[-1].canAddDeck(_):
                i[-1].addDeck(_)
            else:
                i.append(_)
        

    def show(self):
        for num, i in enumerate(self.deck):
            print(num + 1, self.hidden[num],repr(i))
        print()
    
    def showLine(self, i):
        num = self.deck.index(i)
        print(num + 1, self.hidden[num], repr(i))
        print()

    def final(self):
        for i in self.deck:
            for j in i:
                print(repr(j), end='')
            print(', ', end='')
        print()
        print(self.hidden)

if __name__ == '__main__':
    data = [['a'],['7'],['j'],['10'],['a'],['k'],['j'],['8'],['q'],['q']]
    #hidden = [4, 5, 5, 4, 4, 3, 3, 4, 4, 2]
    a = Make(data)
    while sum(a.hidden) != 0:
        while a.move():
            pass
        #a.final()
        a.lab()