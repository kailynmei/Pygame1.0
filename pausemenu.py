

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo com Tela de Pausa")

run = True
pause = False
booster = False

def draw_pause():
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.set_alpha(150)  # Transparência
    surface.fill((128, 128, 128))  # Cor cinza
    screen.blit(surface, (0, 0))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not pause:
                booster = True
            if event.key == pygame.K_ESCAPE:
                pause = not pause
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                booster = False

    if pause:
        draw_pause()
   