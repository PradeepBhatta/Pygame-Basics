import pygame, sys

# Screen
screen_width = 400
screen_height = 400
blue = (0, 150, 200)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

class Intro():
    def __init__(self):
        x = 120
        y = 50
        for i in range(20):
            pygame.draw.rect(screen, blue, pygame.Rect(x, x+30 ,y+100 ,y))
            x += 10
            y -= 20
            print(x, y)
            pygame.display.flip()
            pygame.time.delay(1000)
            screen.fill((0,0,0))
            pygame.display.flip()  


introd = Intro() 
# Mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing  
    pygame.display.flip()
    clock.tick(60)