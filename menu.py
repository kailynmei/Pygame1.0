import pygame
def menu(tela,img1,img2):

    imagem1 = 'aparece'
    menu = 'aparece'

    while menu == 'aparece':

        pygame.display.update()
        pygame.time.wait(600)

        if menu == 'aparece':
            if imagem1 == 'aparece':
                imagem1 = 'sumiu'
                tela.blit(img2,(0,0))
            else:
                imagem1 = 'aparece'
                tela.blit(img1,(0,0))

        for e in pygame.event.get():

            if e.type == pygame.QUIT:

                pygame.quit()
                break 

            elif e.type == pygame.KEYDOWN:

                if e.key == pygame.K_c: 
                    menu = 'sumiu'


pygame.mixer.music.set_volume(0)
ativa_music_menu.play()
menu(tela,)

menu1 = pygame.image.load('Assets/Imagens/Wizard/branco.png').convert_alpha()
menu2 = pygame.image.load('Assets/Imagens/Feiticeiro2/preto.png').convert_alpha()

    