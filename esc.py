import pygame
import sys

def cheque_sair(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo Pygame - Saída com ESC")

running = True
while running:
    events = pygame.event.get()
    cheque_sair(events)
    
    
    screen.fill((0, 0, 0))  
    pygame.display.flip()

pygame.quit()