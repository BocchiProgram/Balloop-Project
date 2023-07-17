import pygame
import random
import Transicions
import math
from pygame.locals import *
from sys import exit

class Jogo:

    def __init__(self):
        clock = pygame.time.Clock()

        pygame.init()
        pygame.display.set_caption('Regular Game')

        largura = 1080
        altura = 650
        dt = 0

        #Contador de levels e pontos
        self.pontos = 0 #Conta pontos
        self.contador = 1 #Conta levels

        self.tela = pygame.display.set_mode((largura, altura))
        self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
        self.fonte = pygame.font.SysFont('arial', 40, True, True)        

        self.player_pos = pygame.Vector2(self.tela.get_width() / 2, self.tela.get_height() / 2)
        self.player_massa = 20
        self.player_cor = Transicions.Trans.player_color(self.contador)
        self.player_velocidade = 235

        self.inimigo_cor = 'red'
        self.inimigo_massa = 15
        self.inimigo_x = largura
        self.inimigo_y = altura
        self.velocidade_x, self.velocidade_y = 3, 2

        self.comida = []
        self.pontos_por_comida = 5
        self.massa_comida = 5
        self.lugares_aletorios = []
        
        self.inimigos = []
        self.lugares_aleatorios_inimigos = []

        self.criar_massas(20)
        self.criar_inimigos(5)

        while True: 
            self.mensagem = f'Pontos: {self.pontos}'
            self.texto_formatado = self.fonte.render(self.mensagem, True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    print(self.lugares_aleatorios_inimigos)
                    pygame.quit()
                    exit()

            self.tela.fill(self.fundo_cor)
            self.manter_massas(20)
            self.manter_inimigos(len(self.inimigos))
            
            #player 
            self.player = pygame.draw.circle(self.tela, self.player_cor, self.player_pos, self.player_massa)   

            for c in range(len(self.lugares_aleatorios_inimigos)):
                self.lugares_aleatorios_inimigos[c][0] += self.velocidade_x 
                self.lugares_aleatorios_inimigos[c][1] += self.velocidade_y
            
                if self.lugares_aleatorios_inimigos[c][0] <= 0 or self.lugares_aleatorios_inimigos[c][0] >= 1080:
                    self.velocidade_x *= -1

                if self.lugares_aleatorios_inimigos[c][1] <= 0 or self.lugares_aleatorios_inimigos[c][1] >= 650:
                    self.velocidade_y *= -1

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= self.player_velocidade * dt
            if keys[pygame.K_d]:
                self.player_pos.x += self.player_velocidade * dt
            if keys[pygame.K_a]:
                self.player_pos.x -= self.player_velocidade * dt
            if keys[pygame.K_s]:
                self.player_pos.y += self.player_velocidade * dt

            self.colisao_comida()
            self.colisao_inimigo()
            
            if self.player_massa > 1500:
                self.player_velocidade = 235
                self.massa_comida = 5
                self.player_massa = 20
                self.contador += 1
                self.pontos_por_comida = 5
                self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
                while True:
                    self.player_cor = Transicions.Trans.player_color(self.contador) 
                    if self.player_cor != self.fundo_cor:
                        break

            if self.player_massa > 100 and self.player_massa < 200:
                self.player_velocidade = 200
                self.pontos_por_comida = 4
            if self.player_massa > 300:
                self.player_velocidade = 250
                self.pontos_por_comida = 3

            pygame.display.flip()

            dt = clock.tick(60) / 1000

    def criar_massas(self, x):
        for c in range(x):
            lugar_aleatorio_x = random.randrange(1, 1080)
            lugar_aleatorio_y = random.randrange(1, 650)

            # lugares_aletorios = [lugar_aleatorio_x, lugar_aleatorio_y]
            self.lugares_aletorios.append([lugar_aleatorio_x, lugar_aleatorio_y])
            self.comida.append(pygame.draw.circle(self.tela, self.player_cor, self.lugares_aletorios[c], self.massa_comida))

    def criar_inimigos(self, x):
        for c in range(x):
            self.numero_random_inimigo_x = random.randrange(0, 1080)
            self.numero_random_inimigo_y = random.randrange(0, 650)

            self.lugares_aleatorios_inimigos.append([self.numero_random_inimigo_y, self.numero_random_inimigo_x])
            self.inimigos.append(pygame.draw.circle(self.tela, self.inimigo_cor, self.lugares_aleatorios_inimigos[c], self.inimigo_massa))   

    def manter_massas(self, x):
        for c in range(x):
            self.comida[c] = pygame.draw.circle(self.tela, self.player_cor, self.lugares_aletorios[c], self.massa_comida)
    
    def manter_inimigos(self, x):
        for c in range(x):
            self.inimigos[c] = pygame.draw.circle(self.tela, self.inimigo_cor, self.lugares_aleatorios_inimigos[c], self.inimigo_massa)

    def verificar_colisao(self, circulo1, circulo2):
        x1, y1, raio1 = circulo1
        x2, y2, raio2 = circulo2

        # Calcula a distância entre os centros dos círculos
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Verifica se há colisão
        if distancia <= raio1 + raio2:
            return True
        else:
            return False

    def colisao_comida(self):
        for c, comida in enumerate(self.comida):
            if self.verificar_colisao((self.player_pos.x, self.player_pos.y, self.player_massa), (comida[0], comida[1], comida[2])):
                del self.comida[c]
                del self.lugares_aletorios[c]
                self.player_massa += self.pontos_por_comida
                self.pontos += 1
                self.criar_massas(1)
                    
        self.tela.blit(self.texto_formatado, (10, 10))

    def colisao_inimigo(self):
        for c, inimigo in enumerate(self.inimigos):
            if self.verificar_colisao((self.player_pos.x, self.player_pos.y, self.player_massa), (inimigo[0], inimigo[1], inimigo[2])):
                del self.inimigos[c]
                del self.lugares_aleatorios_inimigos[c]
                self.player_massa += self.pontos_por_comida
                self.pontos += 10
                    
        self.tela.blit(self.texto_formatado, (10, 10))
if __name__ == "__main__":
    Jogo()