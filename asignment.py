import pygame

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My First Game Screen")


text = pygame.font.Font(None, 36).render('This is a rectangle', True, pygame.Color('black'))

text_rect = text.get_rect(center=(screen_width // 2 - 30, screen_height // 2 - 30))

screen.fill((255, 255, 255))
screen.blit(text, text_rect)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (0, 125, 0), pygame.Rect(screen_width // 2, screen_height // 2, 100, 60))

    pygame.display.flip()