import pygame

class Lutador():
    def __init__(self,x,y):
        self.flip = False
        self.rect = pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.jump = False
        self.atacando = False 
        self.tipo_ataque = 0
        self.health = 100

    def move(self, screen_width, screen_height, surface, alvo):
        SPEED = 10
        GRAVIDADE = 2
        #* Variação nas coordenadas x e y
        dx = 0
        dy = 0

        #* Ações no teclado (pressionar)
        key = pygame.key.get_pressed()

        #* O jogador só podera executar outras ações se não estiver atacando simultaneamente
        if self.atacando == False:

            if key[pygame.K_a]: #* Tecla A
                dx = -SPEED
            if key[pygame.K_d]: #* Tecla D
                dx = SPEED

            #? Pular
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True

            #! Ataque
            if key[pygame.K_r] or key[pygame.K_t]:
                self.ataque(surface, alvo)
                #* Determina tipo de ataque
                if key[pygame.K_r]:
                    self.tipo_ataque = 1
                if key[pygame.K_t]:
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

        #* Atualiza posição do jogador
        self.rect.x += dx
        self.rect.y += dy

    #! Ataque
    def ataque(self, surface,alvo):
        self.atacando = True
        atacando_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if atacando_rect.colliderect(alvo.rect):
            alvo.health -= 10

        pygame.draw.rect(surface,('darkviolet'),atacando_rect)

    def draw(self,surface):
        pygame.draw.rect(surface,('deeppink'),self.rect)