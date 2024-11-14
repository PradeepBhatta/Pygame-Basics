import pygame, sys, random

# Classes
class CrossHair(pygame.sprite.Sprite):
    def __init__(self,pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gunshot.mp3")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(Player, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    
class Target(pygame.sprite.Sprite):
    def __init__(self,pic_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class GameState():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

        pygame.display.flip()
        screen.blit(background, (0,0))
        screen.blit(ready_text, (screen_width/2-115, screen_height/2-33))
        player_group.draw(screen)
        player_group.update()    

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                Player.shoot()

        pygame.display.flip()
        screen.blit(background, (0,0))
        player_group.draw(screen)
        target_group.draw(screen)
        player_group.update()
        
    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()


# General Setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

# Screen
screen_width = 1152
screen_height = 648
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("space.png")
ready_text = pygame.image.load("text_ready.png")
pygame.mouse.set_visible(False)

# CrossHair
Player = CrossHair("crosshair.png")
player_group = pygame.sprite.Group()
player_group.add(Player)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("target.png", random.randrange(0, screen_width), random.randrange(0, screen_height ))
    target_group.add(new_target)

# Mainloop
while True:
    game_state.state_manager()

    clock.tick(60)