import pygame

from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill("red")
background_surface = pygame.image.load('graphics/bg/URy5F.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # background
    screen.blit(background_surface, (0, 0))
    # x axis, y axis, 0, 0 is the top left corner
    screen.blit(test_surface, (100, 100))
    pygame.display.update()
    clock.tick(60)

