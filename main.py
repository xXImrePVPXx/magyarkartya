import pygame #ezzel csinaljuk majd a jatekot
import json
from object import Kartya
pygame.init()
bg = pygame.image.load("kepek/letöltés.jpg")
bg = pygame.transform.scale(bg, (1024, 512))
pygame.display.set_caption('Zsírozás')
with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

ID = 1
adat = cards[ID-1]
#if adat["priority"] == 1 or adat["szin"] == self.szin
screen = pygame.display.set_mode([1024, 512])
p1hand = []
p1points = []
p2hand =[]
p2points = []
deck = [f]
kard = Kartya(14, adat["Nev"], adat['szin'], adat['ertek'], adat['priority'], adat['kep'])
print(kard)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255,))
    screen.blit(bg, (0, 0))
    kard = Kartya(14, adat["Nev"], adat['szin'], adat['ertek'], adat['priority'], adat['kep'])


    pygame.display.flip()

pygame.quit()
