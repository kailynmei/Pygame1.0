import pygame
from lutadores import Lutador

from menu import *

pygame.init()


ativa_music_menu = pygame.mixer.Sound('music.mp3')
#? Cria janela e define parâmetros
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

tela = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆ Medieval Fights ⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆')

#* Framerate
clock = pygame.time.Clock()
FPS = 60

#musica


#* Define fundo
#* Define fundo
img_fundo = pygame.image.load('Assets/Imagens/fundo.png').convert_alpha()
img_fundo = pygame.transform.scale(img_fundo,[1000,600])

#* Aplica spritesheets (personagens)
sheet_feiticeiro2 = pygame.image.load('Assets/Imagens/Wizard/wizardCOMPLETO.png').convert_alpha()
sheet_feiticeiro2 = pygame.transform.scale(sheet_feiticeiro2,[1000,600])


menu1 = pygame.image.load('Assets/Imagens/branco.png').convert_alpha()
menu1 = pygame.transform.scale(menu1,[1000,600])
menu2 = pygame.image.load('Assets/Imagens/preto.png').convert_alpha()
menu2 = pygame.transform.scale(menu2,[1000,600])

#* Define o número de passos em cada animação
anim_mago2 = []
anim_feiticeiro2 = []


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
lutador_1 = Lutador(200,310)
lutador_2 = Lutador(700,310)



pygame.mixer.music.set_volume(0)
ativa_music_menu.play()
menu(tela,menu1,menu2)
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
