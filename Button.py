import pygame
import sys

pygame.init()

largura_tela = 800
altura_tela = 600
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Dividir Tela e Gerenciar Cliques")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def desenhe_divisao():
    screen.fill(WHITE)
    pygame.draw.line(screen, RED, (largura_tela // 2, 0), (largura_tela // 2, altura_tela), 5)
    pygame.display.flip()

def clique (pos):
    x, y = pos
    if x < largura_tela // 2:
        print("Clique no lado esquerdo - Jogar de novo")
  
    else:
        print("Clique no lado direito - Voltar para tela inicial")

def main():
    running = True
    desenhe_divisao()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clique (event.pos)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()