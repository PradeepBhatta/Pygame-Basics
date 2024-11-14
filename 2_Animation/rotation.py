import pygame, sys

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 0.32)
    rotated_rect = rotated_surface.get_rect(center = (250, 250))
    return rotated_surface, rotated_rect


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pickachu = pygame.image.load('pickachu.png')
pickachu_rect = pickachu.get_rect(center = (250, 250))
angle = 0
i = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            i *= -1

    angle -= i
    screen.fill((0,150,255))
    pickachu_rotated, pickachu_rotated_rect = rotate(pickachu, angle)

    screen.blit(pickachu_rotated, pickachu_rotated_rect)
    pygame.display.flip()
    clock.tick(30)