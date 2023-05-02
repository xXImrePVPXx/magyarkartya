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
        return f'<ID: {self.id}, nev: {self.nev} >'

cards = []
with open('kartyak.txt', 'r', encoding='utf-8') as f:
    for sor in f.read().splitlines()[1:]:
        cards.append(Kartya(sor))
p1h = []
aih = []
p1t = []
ait = []
pakli = []

for i in range(10000):
   r=random.randint(0,31)
   if r not in pakli:
      pakli.append(int(r))

print(pakli)
print(len(pakli))
p1h = pakli[:4]
print(p1h)
del pakli[:4]
print(pakli)
aih = pakli[:4]
print(aih)
del pakli[:4]
print(pakli)

if len(p1h) != 4:
    p1h = p1h[:3], pakli[:1]
    print(p1h)

