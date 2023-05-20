import pygame

from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
# set our font to default with a size of 50
test_font = pygame.font.Font(None, 50)

# test text surface for menu
welcome_message = test_font.render("Welcome to My Game", False, "Green")




background_surface = pygame.image.load('graphics/bg/URy5F.png')
background_surface = pygame.transform.scale(background_surface, (800, 400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # background
    screen.blit(background_surface, (0, 0))
    screen.blit(welcome_message, (200, 100))
    # x axis, y axis, 0, 0 is the top left corner
    pygame.display.update()
    clock.tick(60)

