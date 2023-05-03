import random

class Kartya:#Feldolgozza a fájlt
    def __init__(self, sor):
        id, nev, szin, ertek, priority = sor.split(';')
        self.id = int(id)
        self.nev = nev
        self.szin = int(szin)
        self.ertek = int(ertek)
        self.priority = int(priority)

    def __repr__(self):
        return f'|{self.nev}|'


cards = []
with open('kartyak.txt', 'r', encoding='utf-8') as f:
    for sor in f.read().splitlines():
        cards.append(Kartya(sor))

def getcard(id):
    global cards
    for i in cards:
        if i.id == id:
            return i
    return 'card'+str(id)#számot "id"-vé tud alakítani
p1h = []
aih = []
p1t = []
ait = []
pakli = []

for i in range(10000):
   r=random.randint(1,32)
   if r not in pakli:
      pakli.append(int(r))#megkeveri a paklit

pakli = list(map(getcard, pakli))#a paklinak a számait "id"-vé azaz kártyákká alakítjuk



aipont=0
p1pont=0
aiw = False

print('Magyar Kártya:')#hoppa szabalyok
print('ZSÍROZÁS')
szab = input('Ismered a szabályokat?(Igen/Nem)')
if szab == 'Nem' or szab == 'nem' or szab == 'n' or szab == 'N':
    print('Szabályok:')
    print('Minden játékos 4 lappal kezd')
    print('Az ászt és 10-est kell gyűjteni.')
    print('Egy adott színre, ügyan azt a színt kell rakni.')
    print('A hetes mindig üt.')
    print('Aki ütött, az rak legközelebb.')
    print('Aki hamarabb összegyűjti az 5 pontot, nyer.')
    print('Irányítás: 1-4 vagy kevesebb számot kell beírni, hogy kiválasz egy kártyát.')
    print('----------------------')
elif szab == 'Igen' or szab == 'igen' or szab == 'i' or szab == 'I':
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
    print('Irányítás: 1-4 vagy kevesebb számot kell beírni, hogy kiválasz egy kártyát.')
    print('----------------------')


p1h = pakli[:4]#Kiosztja a kártyát
print('Kártyáid:')
print(*p1h)
del pakli[:4]
aih = pakli[:4]#A robotnak is kiosztja
del pakli[:4]
while True:
    if len(p1h) < 4:#Húzz kártyát
        p1h = p1h[:3] + pakli[:1]
        del pakli[:1]
        print('Kártyáid:')
        print(*p1h)

    if len(aih) < 4:#Húzz kártyát
        aih = aih[:3] + pakli[:1]
        del pakli[:1]
    if aiw:
        aicard = aih[0]
        del aih[0]
        print('Robot által lerakott kártya', end=':')
        print(aicard.nev)
    if len(p1h)==4:
        a = int(input('Válassz egy kártyát(1,2,3,4):'))
        selectedcard = p1h[a-1]#Kártyát lerakja a játékos(4)
    if len(p1h)==3:
        a = int(input('Válassz egy kártyát(1,2,3):'))
        selectedcard = p1h[a-1]#Kártyát lerakja a játékos(3)
    if len(p1h)==2:
        a = int(input('Válassz egy kártyát(1,2):'))
        selectedcard = p1h[a-1]#Kártyát lerakja a játékos(2)
    if len(p1h)==1:
        a = int(input('Válassz egy kártyát(1):'))
        selectedcard = p1h[a-1]#Kártyát lerakja a játékos(1)
    del p1h[a-1]
    if not aiw:
        aicard = aih[0]
        del aih[0]
        print('Robot által lerakott kártya', end=':')
        print(aicard.nev)

    if selectedcard.szin == aicard.szin or selectedcard.priority == 1 or aicard.priority == 1:#Megnézi hogy a szín ugyan az-e vagy az egyik hetes e
        if selectedcard.priority < aicard.priority or selectedcard.priority == 1:#Hogyha a játékos nyert
            p1t.append(selectedcard)
            p1t.append(aicard)
            print('Játékos vitte.')
            print('---------------------')
            print(f'Pontjaid:{p1pont}')
            aiw = False
            print('Pakli:')
            print(len(pakli))
        elif selectedcard.priority > aicard.priority or aicard.priority == 1:#Hogyha a bot nyert
            ait.append(selectedcard)
            ait.append(aicard)
            print('Robot vitte.')
            print('---------------------')
            print(f'Pontjaid:{p1pont}')
            aiw = True
            print('Pakli:')
            print(len(pakli))
    else:#Ha nem ugyan az a szín
        if aiw:#Ha nyert a bot
            ait.append(selectedcard)
            ait.append(aicard)
            print('Robot vitte.')
            print('---------------------')
            print(f'Ponjaid:{p1pont}')
            aiw = True
            print('Pakli:')
            print(len(pakli))
        if not aiw:#Ha nem nyert
            p1t.append(selectedcard)
            p1t.append(aicard)
            print('Játékos vitte.')
            print('---------------------')
            print(f'Ponjaid:{p1pont}')
            aiw = False
            print('Pakli:')
            print(len(pakli))
    if pakli == [] and p1h ==[] and aih ==[]: #Ha elfogytak a kártyák
        print('Elfogytak a kártyák.')
        break
    p1pont = 0#Pontot számol
    for i in p1t:
        p1pont += i.ertek

    aipont = 0#Pontot számol
    for i in ait:
        aipont += i.ertek

if p1pont>aipont:#Kinyert?
    print('Nyertél')
elif aipont>p1pont:
    print('Vesztetél.')
else:
    print('Döntetlen.')

print('Vége a játéknak.')