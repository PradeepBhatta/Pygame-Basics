import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for i in range(1, 11):
            file_name = "attack_"+str(i)+".png"
            image = pygame.image.load(file_name)
            image = pygame.transform.scale(image, (300, 150))
            self.sprites.append(image)

        self.current_sprite = 0 
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Animation")

# Creating the sprites and the Group
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)


# Mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()
        
    # Drawing  
    screen.fill((0,0,0))  
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(60)