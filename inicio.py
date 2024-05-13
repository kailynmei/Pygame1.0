import pygame
from lutadores import Lutador

pygame.init()

#? Cria janela e define parâmetros
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

tela = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆ Medieval Fights ⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆')

#* Framerate
clock = pygame.time.Clock()
FPS = 60

#* Define fundo
img_fundo = pygame.image.load('/Users/kailynmeifittelng/Downloads/Pygame GHK/Pygame1.0/Assets/Imagens/fundo.png').convert_alpha()

#* Aplica spritesheets (personagens)
sheet_warrior = pygame.image.load('/Users/kailynmeifittelng/Downloads/Pygame GHK/Pygame1.0/Assets/Imagens/Warrior/warriorCOMPLETO.png').convert_alpha()
sheet_wizard = pygame.image.load('/Users/kailynmeifittelng/Downloads/Pygame GHK/Pygame1.0/Assets/Imagens/Wizard/wizardCOMPLETO.png').convert_alpha()

#* Define o número de passos em cada animação
passos_anim_warrior = [10,8,1,7,7,3,7]
passos_anim_wizard = [8,8,1,8,8,3,7]


#* Define cores que podem ser usadas
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)

#* Função para colocar imagem de fundo
def draw_fundo():
    img_escalada = pygame.transform.scale(img_fundo,(SCREEN_WIDTH,SCREEN_HEIGHT))
    tela.blit(img_escalada,(0,0))

#* Barra de vida dos personagens
def draw_health_bar(health,x,y):
    ratio = health / 100
    pygame.draw.rect(tela, BRANCO,(x-2,y-2,404,34)) #Moldura branca
    pygame.draw.rect(tela,VERMELHO,(x,y,400,30)) #Vermelho embaixo do amarelo (mostra dano)
    pygame.draw.rect(tela,AMARELO, (x,y,400 * ratio,30)) #Amarelo = saúde

#* Cria duas instâncias de jogadores
lutador_1 = Lutador(200,310,sheet_feiticeiro2,passos_anim_feiticeiro2)
lutador_2 = Lutador(700,310,sheet_mago2,passos_anim_mago2)

#* Loop do jogo
run = True
while run:

    clock.tick(FPS)

    #* Coloca imagen de fundo
    draw_fundo()

    #* Mostra vida do jogador
    draw_health_bar(lutador_1.health,20,20)
    draw_health_bar(lutador_2.health,580,20)


    #* Mexe lutadores
    lutador_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, tela, lutador_2)

 
    #* Coloca imagem dos jogadores
    lutador_1.draw(tela)
    lutador_2.draw(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #* Astualiza display
    pygame.display.update()

# Sai do jogo
pygame.quit()