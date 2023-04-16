import pygame#ezzel csinaljuk majd a jatekot
import json
pygame.init()
bg = pygame.image.load("letöltés.jpg")
bg = pygame.transform.scale(bg, (1024, 512))
pygame.display.set_caption('Zsírozás')
with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)
screen = pygame.display.set_mode([1024, 512])
p1hand = []
p1points = []
p2hand =[]
p2points = []
deck = [f]
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255,))
    screen.blit(bg, (0, 0))



    pygame.display.flip()

pygame.quit()