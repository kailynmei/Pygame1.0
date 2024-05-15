import pygame

class Lutador():
    def __init__(self, jogador, x, y, flip, dados, sprite_sheet, passos_animacao, som):
        self.jogador = jogador
        self.size = dados[0]
        self.imagem_scale = dados[1]
        self.offset = dados[2]
        self.flip = flip
        self.lista_animacao = self.load_imagens(sprite_sheet,passos_animacao)
        self.acao = 0 #* 0: idle, 1: correr, 2: pular, 3: ataqueI, 4: ataqueII, 5: hit, 6: morte
        self.frame_index = 0
        self.image = self.lista_animacao[self.acao][self.frame_index]
        self.update_tempo = pygame.time.get_ticks()
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.correndo = False
        self.jump = False
        self.atacando = False 
        self.tipo_ataque = 0
        self.cooldown_ataque = 0
        self.som_ataque = som
        self.hit = False
        self.health = 100
        self.vivo = True

    def load_imagens(self, sprite_sheet, passos_animacao): 
    #* Extrai imagens das sprite sheets
        lista_animacao = []
        for y, animacao in enumerate(passos_animacao):
            img_temp_lista = []
            for x in range(animacao):
                img_temp = sprite_sheet.subsurface( x * self.size, y * self.size, self.size, self.size)
                img_temp_lista.append(pygame.transform.scale(img_temp, (self.size * self.imagem_scale, self.size * self.imagem_scale)))
            lista_animacao.append(img_temp_lista)
        return lista_animacao


    def move(self, screen_width, screen_height, surface, alvo, round_over):
        SPEED = 10
        GRAVIDADE = 2
        #* Variação nas coordenadas x e y
        dx = 0
        dy = 0
        self.correndo = False
        self.tipo_ataque = 0

        #* Ações no teclado (pressionar)
        key = pygame.key.get_pressed()

        #* O jogador só podera executar outras ações se não estiver atacando simultaneamente
        if self.atacando == False and self.vivo == True and round_over == False:

            #? CHECA CONTROLE DO PLAYER 1
            if self.jogador == 1:

                if key[pygame.K_a]: #* Tecla A
                    dx = -SPEED
                    self.correndo = True
                if key[pygame.K_d]: #* Tecla D
                    dx = SPEED
                    self.correndo = True

                #! Pular
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                #! Ataque
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.ataque(alvo)
                    #* Determina tipo de ataque
                    if key[pygame.K_r]:
                        self.tipo_ataque = 1
                    if key[pygame.K_t]:
                        self.tipo_ataque = 2

            #? CHECA CONTROLE DO PLAYER 2
            if self.jogador == 2:
                
                if key[pygame.K_LEFT]: 
                    dx = -SPEED
                    self.correndo = True
                if key[pygame.K_RIGHT]: 
                    dx = SPEED
                    self.correndo = True

                #! Pular
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                #! Ataque
                if key[pygame.K_RETURN] or key[pygame.K_RSHIFT]:
                    self.ataque(alvo)
                    #* Determina tipo de ataque
                    if key[pygame.K_RETURN]:
                        self.tipo_ataque = 1
                    if key[pygame.K_RSHIFT]:
                        self.tipo_ataque = 2

        #? Aplica gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y

        #* Jogador não extrapola limite da tela
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom

        #* Verifica se os jogadores estão de frente um para o outro
        if alvo.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #* Aplica cooldown de ataque
        if self.cooldown_ataque > 0:
            self.cooldown_ataque -= 1

        #* Atualiza posição do jogador
        self.rect.x += dx
        self.rect.y += dy

    #* UPDATES DE ANIMAÇÃO
    def update(self):
        #* Checa qual ação o jogador está executando
        if self.health <= 0:
            self.health = 0
            self.vivo = False
            self.update_acao(6) #! 6 = morte
        elif self.hit == True:
            self.update_acao(5) #! 5 = hit
        elif self.atacando == True:
            if self.tipo_ataque == 1:
                self.update_acao(3) #! 3 = ataque1
            elif self.tipo_ataque == 2:
                self.update_acao(4) #! 4 = ataque2
        elif self.jump == True:
            self.update_acao(2) #! 2 = pular
        elif self.correndo == True:
            self.update_acao(1) #! 1 = correr
        else:
            self.update_acao(0) #! 0 = idle

        animacao_cooldown = 50 #Milisegundos
        #* Update imagem
        self.image = self.lista_animacao[self.acao][self.frame_index]
        #* Checa se já passou tempo o suficiente desde o último update
        if pygame.time.get_ticks() - self.update_tempo > animacao_cooldown:
            self.frame_index += 1
            self.update_tempo = pygame.time.get_ticks()
        #* Checa se a animação já acabou
        if self.frame_index >= len(self.lista_animacao[self.acao]):
            #* Checa se o jogados está morto. Se sim, a animação deve acabar
            if self.vivo == False:
                self.frame_index = len(self.lista_animacao[self.acao]) - 1
            else:
                self.frame_index = 0
                #* Checa se um ataque foi executado
                if self.acao == 3 or self.acao == 4:
                    self.atacando = False
                    self.cooldown_ataque = 20 #Milisegundos
                #* Checa se o outro jogador levou dano pelo ataque
                if self.acao == 5:
                    self.hit = False
                #* Se o jogador estava no meio de um ataque, o ataque parou
                    self.atacando = False
                    self.cooldown_ataque = 20

    #! Ataque
    def ataque(self, alvo):
        if self.cooldown_ataque == 0:
            #* Executa ataque
            self.atacando = True
            self.som_ataque.play()
            atacando_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            if atacando_rect.colliderect(alvo.rect):
                alvo.health -= 10
                alvo.hit = True

    def update_acao(self, acao_nova):
        #* Checa se a nova ação é diferente da anterior
        if acao_nova != self.acao:
            self.acao = acao_nova
        #* Update configurações da animação
            self.frame_index = 0
            self.update_tempo = pygame.time.get_ticks()

    def draw(self,surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.imagem_scale), self.rect.y - (self.offset[1] * self.imagem_scale)))
