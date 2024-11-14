import pygame, sys

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(100, 100, 140, 32)
color_active = (0, 250, 100)
color_passive = (250, 0, 0)
color = color_passive
active = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_passive

        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        
    screen.fill((0,150,255))
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (255,255,255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100, text_surface.get_width() +10)

    pygame.display.flip()
    clock.tick(30)