import pygame
from pygame import mixer
from lutadores import Lutador

mixer.init()
pygame.init()

#? Cria janela e define parâmetros
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

tela = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆ Medieval Fights ⋆˖⁺‧₊☽◯☾₊‧⁺˖⋆')

#* Framerate
clock = pygame.time.Clock()
FPS = 60

#* Define cores que podem ser usadas
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)

#* Define variáveis do jogo
contagem_regressiva = 3
ultima_contagem_update = pygame.time.get_ticks()
pontos = [0,0] # [Jogador1, Jogador2]
round_over = False
cooldown_round_over = 2000

#* Define variáveis dos personagens
warrior_size = 162
warrior_scale = 4
warrior_offset = [72, 56]
dados_warrior = [warrior_size, warrior_scale, warrior_offset]

wizard_size = 250
wizard_scale = 3
wizard_offset = [112, 107]
dados_wizard = [wizard_size, wizard_scale, wizard_offset]

#* Define sons
#! MÚSICA
# Helena

#! ATAQUES
som_espada = pygame.mixer.Sound('/Users/kailynmeifittelng/Downloads/Cópias Pygame/Pygame GHK/Pygame1.0/Assets/Áudios/sword.wav')
som_espada.set_volume(0.5)
som_magia = pygame.mixer.Sound('/Users/kailynmeifittelng/Downloads/Cópias Pygame/Pygame GHK/Pygame1.0/Assets/Áudios/magic.wav')
som_magia.set_volume(0.75)

#* Define fundo
img_fundo = pygame.image.load('/Users/kailynmeifittelng/Downloads/Pygame GHK/Pygame1.0/Assets/Imagens/fundo.png').convert_alpha()

#* Spritesheets (personagens)
sheet_warrior = pygame.image.load('/Users/kailynmeifittelng/Downloads/Cópias Pygame/Pygame GHK/Pygame1.0/Assets/Imagens/Warrior/warriorTODOS.png').convert_alpha()
sheet_wizard = pygame.image.load('/Users/kailynmeifittelng/Downloads/Cópias Pygame/Pygame GHK/Pygame1.0/Assets/Imagens/Wizard/wizardTODOS.png').convert_alpha()

#* Imagem vitória
img_vitoria = pygame.image.load('/Users/kailynmeifittelng/Downloads/Cópias Pygame/Pygame GHK/Pygame1.0/Assets/Imagens/victory.png').convert_alpha()

#* Define o número de passos em cada animação
passos_anim_warrior = [10, 8, 1, 7, 7, 3, 7]
passos_anim_wizard = [8, 8, 1, 8, 8, 3, 7]

#* Define fonte
fonte_contagem = pygame.font.Font('/Users/kailynmeifittelng/Downloads/Cópias Pygame/Pygame GHK/Pygame1.0/Assets/Fonte (texto)/turok.ttf', 80) 
fonte_pontos = pygame.font.Font('/Users/kailynmeifittelng/Downloads/Cópias Pygame/Pygame GHK/Pygame1.0/Assets/Fonte (texto)/turok.ttf', 30) 

#* Função para escrever texto na tela
def draw_texto(texto, fonte, cor_texto, x, y):
    img = fonte.render(texto, True, cor_texto)
    tela.blit(img, (x, y))

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
lutador_1 = Lutador(1, 200, 310, False, dados_warrior, sheet_warrior, passos_anim_warrior, som_espada)
lutador_2 = Lutador(2, 700, 310, True, dados_wizard, sheet_wizard, passos_anim_wizard, som_magia)

#* Loop do jogo
run = True
while run:

    clock.tick(FPS)

    #* Coloca imagem de fundo
    draw_fundo()

    #* Mostra vida do jogador
    draw_health_bar(lutador_1.health,20,20)
    draw_health_bar(lutador_2.health,580,20)
    draw_texto('Jogador 1: ' + str(pontos[0]), fonte_pontos, VERMELHO, 20, 60)
    draw_texto('Jogador 2: ' + str(pontos[1]), fonte_pontos, VERMELHO, 580, 60)

    #* Update contagem regressiva
    if contagem_regressiva <= 0:
        #* Mexe lutadores
        lutador_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, tela, lutador_2, round_over)
        lutador_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, tela, lutador_1, round_over)
    else:
        #* Mostra contagem regressiva
        draw_texto(str(contagem_regressiva), fonte_contagem, VERMELHO, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        #* Update timer de contagem
        if (pygame.time.get_ticks() - ultima_contagem_update) >= 1000:
            contagem_regressiva -= 1
            ultima_contagem_update = pygame.time.get_ticks()

    #* Update lutadores
    lutador_1.update()
    lutador_2.update()
 
    #* Coloca imagem dos jogadores na tela
    lutador_1.draw(tela)
    lutador_2.draw(tela)

    #* Checa se houve derrota de um jogador
    if round_over == False:
        if lutador_1.vivo == False:
            pontos[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif lutador_2.vivo == False:
            pontos[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        tela.blit(img_vitoria,(360,150))
        if pygame.time.get_ticks() - round_over_time > cooldown_round_over:
            round_over = False
            contagem_regressiva = 3
            lutador_1 = Lutador(1, 200, 310, False, dados_warrior, sheet_warrior, passos_anim_warrior, som_espada)
            lutador_2 = Lutador(2, 700, 310, True, dados_wizard, sheet_wizard, passos_anim_wizard, som_magia)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #* Atualiza display
    pygame.display.update()

# Sai do jogo
pygame.quit()