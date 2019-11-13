
from make_learn import Make
from deck import deckList
from random import sample, random, randint, choice

patton = []

population = 20
best = 10
lucky = 10
mutation = 10



def nextGeneration(patton):
    next_generation = []

    patton = list(filter(lambda x: x[2], patton))

    patton = sorted(patton, key=lambda x: x[0])

    print(patton[0][0])

    if len(patton) < 15:
        for i in range(15 - len(patton)):
            patton.append([1,deckList(),True])

    for i in range(best):
        next_generation.append(patton[i][1])

    for i in sample(patton, lucky):
        next_generation.append(i[1])

    return next_generation

def mutate(population):
    result = []
    for i in population:
        if random() * 100 < mutation:
            result.append(mutation_setting(i))
        else:
            result.append(i)
    return result

def mutation_setting(listDeck):
    b = []
    a = randint(0, len(listDeck))
    for i in range(len(listDeck)):
        if listDeck[a] != listDeck[i]:
            b.append(i)
    c = choice(b)

    tmp = listDeck[a]
    listDeck[a] = listDeck[c]
    listDeck[c] = tmp

    return listDeck

def check(generation):
    result = []
    for i in generation:
        print(i)
        ii = i[:]
        count, finish = Make(i).start()
        result.append([count, ii, finish])
    return result

if __name__ == '__main__':
    patton = []
    for i in range(population):
        patton.append(deckList())
    count = 0
    ng = check(patton)
    while True:
        print('{0}번째 세대 ======= '.format(count))
        count += 1
        ng = nextGeneration(ng)
        ng = mutate(ng)
        print(ng)
        ng = check(ng)
        