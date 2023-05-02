import random

class Kartya:
    def __init__(self, sor):
        id, nev, szin, ertek, priority = sor.split(';')
        self.id = int(id)
        self.nev = nev
        self.szin = int(szin)
        self.ertek = int(ertek)
        self.priority = int(priority)

    def __repr__(self):
        return f'{self.nev}'


cards = []
with open('kartyak.txt', 'r', encoding='utf-8') as f:
    for sor in f.read().splitlines():
        cards.append(Kartya(sor))

def getcard(id):
    global cards
    for i in cards:
        if i.id == id:
            return i
    return 'card'+str(id)
p1h = []
aih = []
p1t = []
ait = []
pakli = []

for i in range(10000):
   r=random.randint(1,32)
   if r not in pakli:
      pakli.append(int(r))

pakli = list(map(getcard, pakli))



aipont=0
p1pont=0
aiw = False

print('Magyar Kártya:')
print('ZSÍROZÁS')
szab = input('Ismered a szabályokat?(Igen/Nem)')
if szab == 'Nem':
    print('Szabályok:')
    print('Minden játékos 4 lappal kezd')
    print('Az ászt és 10-est kell gyűjteni.')
    print('Egy adott színre, ügyan azt a színt kell rakni.')
    print('A hetes mindig üt.')
    print('Aki ütött, az rak legközelebb.')
    print('Aki hamarabb összegyűjti az 5 pontot, nyer.')
    print('----------------------')
elif szab == 'Igen':
    print('Akkor kezdődjön a játék!')
else:
    print('Ezt egy Nemnek veszem.')
    print('Szabályok:')
    print('Minden játékos 4 lappal kezd')
    print('Az ászt és 10-est kell gyűjteni.')
    print('Egy adott színre, ügyan azt a színt kell rakni.')
    print('A hetes mindig üt.')
    print('Aki ütött, az rak legközelebb.')
    print('Aki hamarabb összegyűjti az 5 pontot, nyer.')
    print('----------------------')


p1h = pakli[:4]
print('Kártyáid:')
print(*p1h)
del pakli[:4]
aih = pakli[:4]
print(aih)
del pakli[:4]
while aipont < 5 and p1pont < 5:
    if aiw:
        aicard = aih[0]
        del aih[0]

        print('Robot által lerakott kártya', end=':')
        print(aicard.nev)
    a = int(input('Válassz egy kártyát(1,2,3,4):'))
    selectedcard = p1h[a-1]
    del p1h[a-1]
    if not aiw:
        aicard = aih[0]
        del aih[0]

    if selectedcard.szin == aicard.szin or selectedcard.priority == 1 or aicard.priority == 1:
        if selectedcard.priority < aicard.priority or selectedcard.priority == 1:
            p1t.append(selectedcard)
            p1t.append(aicard)
            print('Játékos vitte.')
            print('---------------------')
            print(f'Pontjaid:{p1pont}')
            aiw = False
            print('Pakli:')
            print(len(pakli))
        elif selectedcard.priority > aicard.priority or aicard.priority == 1:
            ait.append(selectedcard)
            ait.append(aicard)
            print('Robot vitte.')
            print('---------------------')
            print(f'Pontjaid:{p1pont}')
            aiw = True
            print('Pakli:')
            print(len(pakli))
    else:
        if aiw:
            ait.append(selectedcard)
            ait.append(aicard)
            print('Robot vitte.')
            print('---------------------')
            print(f'Ponjaid:{p1pont}')
            aiw = True
            print('Pakli:')
            print(len(pakli))
        if not aiw:
            p1t.append(selectedcard)
            p1t.append(aicard)
            print('Játékos vitte.')
            print('---------------------')
            print(f'Ponjaid:{p1pont}')
            aiw = False
            print('Pakli:')
            print(len(pakli))

    if len(p1h) < 4:
        p1h = p1h[:3] + pakli[:1]
        del pakli[:1]
        print('Kártyáid:')
        print(*p1h)

    if len(aih) < 4:
        aih = aih[:3] + pakli[:1]
        del pakli[:1]
        print(aih)


    p1pont = 0
    for i in p1t:
        p1pont += i.ertek

    aipont = 0
    for i in ait:
        aipont += i.ertek

    if pakli == [] and p1h ==[] and aih ==[]:
        print('Elfogytak a kártyák.')
        break

if p1pont == 5:
    print('Nyertél')
elif aipont == 5:
    print('Vesztetél.')
else:
    print('Döntetlen.')

print('Vége a játéknak.')