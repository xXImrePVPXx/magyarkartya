import pygame#ezzel csinaljuk majd a jatekot
pygame.init()
bg = pygame.image.load("letöltés.jpg")
bg = pygame.transform.scale(bg, (1024, 512))

screen = pygame.display.set_mode([1024, 512])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255,))
    screen.blit(bg, (0, 0))

    pygame.display.flip()

pygame.quit()