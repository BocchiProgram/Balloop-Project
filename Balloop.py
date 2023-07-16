import pygame
import random
import Transicions
from time import sleep
from pygame.locals import *
from sys import exit

class jogo:
    def __init__(self):
        clock = pygame.time.Clock()

        pygame.init()
        self.contador = 0
        largura = 1080
        altura = 650
        dt = 0

        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Regular Game')

        self.player_pos = pygame.Vector2(self.tela.get_width() / 2, self.tela.get_height() / 2)
        self.player_massa = 20
        self.comida = []
        self.lugares_aletorios = []

        self.player_cor = 'blue'
        self.fundo_cor = 'purple'

        self.criar_massas(5)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                while len(self.comida) != 5:
                    self.criar_massas(1)

            self.tela.fill(self.fundo_cor)
            try:
                self.manter_massas(5)
            except:
                pass
            
            #player 
            try:
                self.player = pygame.draw.circle(self.tela, self.player_cor, self.player_pos, self.player_massa)   
            except:
                pass
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 200 * dt
            if keys[pygame.K_d]:
                self.player_pos.x += 200 * dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 200 * dt
            if keys[pygame.K_s]:
                self.player_pos.y += 200 * dt

            self.pontos_por_comida = 400

            # Verfica a colisão uma de cada vez
            try:
                if self.player.collideobjectsall(self.comida):
                    if self.player.colliderect(self.comida[4]):
                        del self.comida[4]
                        del self.lugares_aletorios[4]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[3]):
                        del self.comida[3]
                        del self.lugares_aletorios[3]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[2]):
                        del self.comida[2]
                        del self.lugares_aletorios[2]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[1]):
                        del self.comida[1]
                        del self.lugares_aletorios[1]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[0]):
                        del self.comida[0]
                        del self.lugares_aletorios[0]
                        self.player_massa += self.pontos_por_comida
            except:
                pass
            
            #dificulta o jogo quando a massa chega a mais de 400
            if self.player_massa > 400:
                self.pontos_por_comida = 1
            try:
                if self.player_massa > 700:
                    self.player_massa = 20
                    self.contador += 1
                    self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
                    # verifica se a cor de fundo é igual a do player, caso seja, fica em um loop até não ser mais
                    while True:
                        self.player_cor = Transicions.Trans.player_color(self.contador) 
                        if self.player_cor != self.fundo_cor:
                            break
            except:
                pass
            
            pygame.display.flip()

            dt = clock.tick(60) / 1000
    
    #cria massas
    def criar_massas(self, x):
        for c in range(x):
            lugar_aleatorio_x = random.randrange(1, 1080)
            lugar_aleatorio_y = random.randrange(1, 650)

            self.lugares_aletorios.append([lugar_aleatorio_x, lugar_aleatorio_y])
            self.comida.append(pygame.draw.circle(self.tela, self.player_cor, self.lugares_aletorios[c], 10))

    #mantem as massas visiveis
    def manter_massas(self, x):
        for c in range(x):
            self.comida[c] = pygame.draw.circle(self.tela, self.player_cor, self.lugares_aletorios[c], 10)


if __name__ == "__main__":
    jogo()