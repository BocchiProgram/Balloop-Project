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
        self.contador = 1
        largura = 1080
        altura = 650
        dt = 0

        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Regular Game')

        self.player_pos = pygame.Vector2(self.tela.get_width() / 2, self.tela.get_height() / 2)
        self.player_massa = 20
        self.comida = []
        self.lugares_aletorios = []

        self.player_cor = 'black'
        self.fundo_cor = 'purple'

        self.player_velocidade = 235

        self.massa_comida = 5

        self.criar_massas(20)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                while len(self.comida) != 20:
                    self.criar_massas(1)

            self.tela.fill(self.fundo_cor)
            try:
                self.manter_massas(20)
            except:
                pass
            
            #player 
            try:
                self.player = pygame.draw.circle(self.tela, self.player_cor, self.player_pos, self.player_massa)   
            except:
                pass
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= self.player_velocidade * dt
            if keys[pygame.K_d]:
                self.player_pos.x += self.player_velocidade * dt
            if keys[pygame.K_a]:
                self.player_pos.x -= self.player_velocidade * dt
            if keys[pygame.K_s]:
                self.player_pos.y += self.player_velocidade * dt

            self.pontos_por_comida = 200

            try:
                if self.player.collideobjectsall(self.comida):
                    if self.player.colliderect(self.comida[19]):
                        del self.comida[19]
                        del self.lugares_aletorios[19]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[18]):
                        del self.comida[18]
                        del self.lugares_aletorios[18]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[17]):
                        del self.comida[17]
                        del self.lugares_aletorios[17]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[16]):
                        del self.comida[16]
                        del self.lugares_aletorios[16]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[15]):
                        del self.comida[15]
                        del self.lugares_aletorios[15]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[14]):
                        del self.comida[14]
                        del self.lugares_aletorios[14]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[13]):
                        del self.comida[13]
                        del self.lugares_aletorios[13]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[12]):
                        del self.comida[12]
                        del self.lugares_aletorios[12]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[11]):
                        del self.comida[11]
                        del self.lugares_aletorios[11]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[10]):
                        del self.comida[10]
                        del self.lugares_aletorios[10]
                    if self.player.colliderect(self.comida[9]):
                        del self.comida[9]
                        del self.lugares_aletorios[9]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[8]):
                        del self.comida[8]
                        del self.lugares_aletorios[8]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[7]):
                        del self.comida[7]
                        del self.lugares_aletorios[7]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[6]):
                        del self.comida[6]
                        del self.lugares_aletorios[6]
                        self.player_massa += self.pontos_por_comida
                    if self.player.colliderect(self.comida[5]):
                        del self.comida[5]
                        del self.lugares_aletorios[5]
                        self.player_massa += self.pontos_por_comida
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
            
            if self.player_massa > 400:
                self.pontos_por_comida = 1
            try:
                if self.player_massa > 800:
                    self.player_velocidade = 235
                    self.massa_comida = 5
                    self.player_massa = 20
                    self.contador += 1
                    self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
                    while True:
                        self.player_cor = Transicions.Trans.player_color(self.contador) 
                        if self.player_cor != self.fundo_cor:
                            break
            except:
                pass
            
            if self.player_massa > 100 and self.player_massa < 200:
                self.player_velocidade = 200
                self.pontos_por_comida = 0.1
            if self.player_massa > 200:
                self.player_velocidade = 250
                self.pontos_por_comida = 0.00000000000001

            pygame.display.flip()

            dt = clock.tick(60) / 1000
        
    def criar_massas(self, x):
        for c in range(x):
            lugar_aleatorio_x = random.randrange(1, 1080)
            lugar_aleatorio_y = random.randrange(1, 650)

            # lugares_aletorios = [lugar_aleatorio_x, lugar_aleatorio_y]
            self.lugares_aletorios.append([lugar_aleatorio_x, lugar_aleatorio_y])
            self.comida.append(pygame.draw.circle(self.tela, self.player_cor, self.lugares_aletorios[c], self.massa_comida))


    def manter_massas(self, x):
        for c in range(x):
            self.comida[c] = pygame.draw.circle(self.tela, self.player_cor, self.lugares_aletorios[c], self.massa_comida)


if __name__ == "__main__":
    jogo()