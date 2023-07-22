import pygame
import random
import Transicions
import math
from pygame.locals import *
from sys import exit


class Start:
    def __init__(self):
        clock = pygame.time.Clock()

        pygame.init()
        pygame.display.set_caption('Regular Game')

        largura = 1080
        altura = 650

        self.tela = pygame.display.set_mode((largura, altura))
        self.fundo_cor = Transicions.Trans.backgroud_color(1)
        self.fonte = pygame.font.SysFont('arial', 40, True, True)        

        self.player_pos = pygame.Vector2(self.tela.get_width() / 2, self.tela.get_height() / 2)
        self.player_massa = 20
        self.player_cor = [Transicions.Trans.player_color(1), 'orange']
        self.player_cor_number = 0
        self.player_velocidade = 320

        while True: 
            self.mensagem1 = f'PACIFICO'
            self.texto_formatado1 = self.fonte.render(self.mensagem1, True, (255, 255, 255))

            self.mensagem2 = f'ADVENTURE'
            self.texto_formatado2 = self.fonte.render(self.mensagem2, True, (255, 255, 255))

            self.mensagem3 = f'HARDCORE'
            self.texto_formatado3 = self.fonte.render(self.mensagem3, True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            self.tela.fill(self.fundo_cor)
            
            #player 
            self.player = pygame.draw.circle(self.tela, self.player_cor[self.player_cor_number], self.player_pos, self.player_massa)   

            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_w]:
                self.player_pos.y -= self.player_velocidade * dt
            if self.keys[pygame.K_d]:
                self.player_pos.x += self.player_velocidade * dt
            if self.keys[pygame.K_a]:
                self.player_pos.x -= self.player_velocidade * dt
            if self.keys[pygame.K_s]:
                self.player_pos.y += self.player_velocidade * dt


            self.colisao_texto() 
            pygame.display.flip()

            dt = clock.tick(60) / 1000

    def colisao_texto(self):         
        self.tela.blit(self.texto_formatado1, (190, 150))
        self.tela.blit(self.texto_formatado2, (420, 150))
        self.tela.blit(self.texto_formatado3, (700, 150))

        texto_rect1 = self.texto_formatado3.get_rect(topleft=(700, 150))
        jogador_rect1 = pygame.Rect(self.player_pos.x - self.player_massa, self.player_pos.y - self.player_massa, self.player_massa * 2, self.player_massa * 2)
        
        if texto_rect1.colliderect(jogador_rect1):
                Jogo_Hardcore()

        texto_rect2 = self.texto_formatado3.get_rect(topleft=(190, 150))
        jogador_rect2 = pygame.Rect(self.player_pos.x - self.player_massa, self.player_pos.y - self.player_massa, self.player_massa * 2, self.player_massa * 2)
        
        if texto_rect2.colliderect(jogador_rect2):
                Jogo_Pacifico()
                    
class Jogo_Hardcore:
    def __init__(self):
        clock = pygame.time.Clock()

        self.timer_tempo = 0
        self.timer_tempo_real = 0

        pygame.init()
        pygame.display.set_caption('Regular Game')

        dt = 0
        largura = 1080
        altura = 650

        #Contador de levels e pontos
        self.pontos = 0 #Conta pontos
        self.contador = 1 #Conta levels

        self.tela = pygame.display.set_mode((largura, altura))
        self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
        self.fonte = pygame.font.SysFont('arial', 40, True, True)        

        self.player_pos = pygame.Vector2(self.tela.get_width() / 2, self.tela.get_height() / 2)
        self.player_massa = 20
        self.player_cor = [Transicions.Trans.player_color(self.contador), 'orange']
        self.player_cor_number = 0
        self.player_velocidade = 320
    
        while True:
            self.player_cor[0] = Transicions.Trans.player_color(self.contador) 
            if self.player_cor[0] != self.fundo_cor:
                break

        self.inimigo_cor = 'red'
        self.inimigo_massa = 8
        self.inimigo_x = largura
        self.inimigo_y = altura
        self.velocidade_x = []
        self.velocidade_y = []
        
        self.comida = []
        self.pontos_por_comida = 2
        self.massa_comida = 5
        self.lugares_aletorios = []
        
        self.inimigos = []
        self.lugares_aleatorios_inimigos = []

        self.criar_massas(20)
        self.criar_inimigos(self.contador)

        while True: 
            self.mensagem = f'Pontos: {self.pontos}'
            self.texto_formatado = self.fonte.render(self.mensagem, True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            self.tela.fill(self.fundo_cor)
            self.manter_massas(20)
            self.manter_inimigos(len(self.inimigos))
            
            #player 
            self.player = pygame.draw.circle(self.tela, self.player_cor[self.player_cor_number], self.player_pos, self.player_massa)   

            for c in range(len(self.lugares_aleatorios_inimigos)):
                self.lugares_aleatorios_inimigos[c][0] += self.velocidade_x[c] 
                self.lugares_aleatorios_inimigos[c][1] += self.velocidade_y[c]
            
                if self.lugares_aleatorios_inimigos[c][0] <= 0 or self.lugares_aleatorios_inimigos[c][0] >= 1080:
                    self.velocidade_x[c] *= -1

                if self.lugares_aleatorios_inimigos[c][1] <= 0 or self.lugares_aleatorios_inimigos[c][1] >= 650:
                    self.velocidade_y[c] *= -1

            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_w]:
                self.player_pos.y -= self.player_velocidade * dt
            if self.keys[pygame.K_d]:
                self.player_pos.x += self.player_velocidade * dt
            if self.keys[pygame.K_a]:
                self.player_pos.x -= self.player_velocidade * dt
            if self.keys[pygame.K_s]:
                self.player_pos.y += self.player_velocidade * dt

            self.timer_tempo += 1
            if self.timer_tempo == 57:
                self.timer_tempo_real += 1
                self.timer_tempo = 0

            print(self.timer_tempo_real)

            self.colisao_comida()
            if self.timer_tempo_real > 3:
                self.colisao_inimigo()
                self.player_cor_number = 0
            else:
                if self.timer_tempo < 27.5:
                    self.player_cor_number = 1
                else:
                    self.player_cor_number = 0 
            
            if self.player_massa > 1500:
                self.timer_tempo_real = 0
                self.inimigo_cor = 'red'
                self.player_velocidade = 320
                self.massa_comida = 5
                self.player_massa = 20
                self.contador += 1
                self.pontos_por_comida = 2
                self.criar_inimigos(self.contador)
                self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
                while True:
                    self.player_cor[0] = Transicions.Trans.player_color(self.contador) 
                    if self.player_cor[0] != self.fundo_cor:
                        break

            if self.player_massa > 100 and self.player_massa < 200:
                self.player_velocidade = 355
                self.pontos_por_comida = 8
            if self.player_massa > 400:
                self.player_velocidade = 355
                self.pontos_por_comida = 3

            if self.player_massa > 38:
                self.pontos_por_comida = 8
                self.inimigo_cor = self.player_cor[0]
                
            pygame.display.flip()

            dt = clock.tick(60) / 1000

    def criar_massas(self, x):
        for c in range(x):
            lugar_aleatorio_x = random.randrange(1, 1080)
            lugar_aleatorio_y = random.randrange(1, 650)

            self.lugares_aletorios.append([lugar_aleatorio_x, lugar_aleatorio_y])
            self.comida.append(pygame.draw.circle(self.tela, self.player_cor[0], self.lugares_aletorios[c], self.massa_comida))

    def criar_inimigos(self, x):
        for c in range(x):
            self.numero_random_inimigo_x = random.randrange(0, 1080)
            self.numero_random_inimigo_y = random.randrange(0, 650)

            self.velocidade_x.append(c - 0.5)
            self.velocidade_y.append(c - 0.5)
                
            self.lugares_aleatorios_inimigos.append([self.numero_random_inimigo_x, self.numero_random_inimigo_y])
            self.inimigos.append(pygame.draw.circle(self.tela, self.inimigo_cor, self.lugares_aleatorios_inimigos[c], self.inimigo_massa))

    def manter_massas(self, x):
        for c in range(x):
            self.comida[c] = pygame.draw.circle(self.tela, self.player_cor[0], self.lugares_aletorios[c], self.massa_comida)
    
    def manter_inimigos(self, x):
        for c in range(x):
            self.inimigos[c] = pygame.draw.circle(self.tela, self.inimigo_cor, self.lugares_aleatorios_inimigos[c], self.inimigo_massa)

    def colisao_comida(self):
        for c, comida in enumerate(self.comida):
            if Functions.verificar_colisao((self.player_pos.x, self.player_pos.y, self.player_massa), (comida[0], comida[1], comida[2])):
                del self.comida[c]
                del self.lugares_aletorios[c]
                self.player_massa += self.pontos_por_comida
                self.pontos += 1
                self.criar_massas(1)
                    
        self.tela.blit(self.texto_formatado, (10, 10))

    def colisao_inimigo(self):
        for c, inimigo in enumerate(self.inimigos):
            if self.verificar_colisao((self.player_pos.x, self.player_pos.y, self.player_massa), (inimigo[0], inimigo[1], inimigo[2])):
                if self.player_massa >38:
                    del self.inimigos[c]
                    del self.lugares_aleatorios_inimigos[c]
                    del self.velocidade_x[c]
                    del self.velocidade_y[c]
                else:
                    Game_over()
                self.player_massa += self.pontos_por_comida
                self.pontos += 10
                    
        self.tela.blit(self.texto_formatado, (10, 10))

class Jogo_Pacifico:
    def __init__(self):
        clock = pygame.time.Clock()

        self.timer_tempo = 0
        self.timer_tempo_real = 0
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
        self.player_cor = [Transicions.Trans.player_color(self.contador), 'orange']
        self.player_cor_number = 0
        self.player_velocidade = 320
    
        while True:
            self.player_cor[0] = Transicions.Trans.player_color(self.contador) 
            if self.player_cor[0] != self.fundo_cor:
                break
        
        self.comida = []
        self.pontos_por_comida = 2
        self.massa_comida = 5
        self.lugares_aletorios = []

        self.criar_massas(20)

        while True: 
            self.mensagem = f'Pontos: {self.pontos}'
            self.texto_formatado = self.fonte.render(self.mensagem, True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            self.tela.fill(self.fundo_cor)
            self.manter_massas(20)
            
            #player 
            self.player = pygame.draw.circle(self.tela, self.player_cor[self.player_cor_number], self.player_pos, self.player_massa)   


            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_w]:
                self.player_pos.y -= self.player_velocidade * dt
            if self.keys[pygame.K_d]:
                self.player_pos.x += self.player_velocidade * dt
            if self.keys[pygame.K_a]:
                self.player_pos.x -= self.player_velocidade * dt
            if self.keys[pygame.K_s]:
                self.player_pos.y += self.player_velocidade * dt

            self.timer_tempo += 1
            if self.timer_tempo == 57:
                self.timer_tempo_real += 1
                self.timer_tempo = 0


            self.colisao_comida()
            if self.timer_tempo_real > 3:
                self.player_cor_number = 0
            else:
                if self.timer_tempo < 27.5:
                    self.player_cor_number = 1
                else:
                    self.player_cor_number = 0 
            
            if self.player_massa > 1500:
                self.timer_tempo_real = 0
                self.player_velocidade = 320
                self.massa_comida = 5
                self.player_massa = 20
                self.contador += 1
                self.pontos_por_comida = 2
                self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
                while True:
                    self.player_cor[0] = Transicions.Trans.player_color(self.contador) 
                    if self.player_cor[0] != self.fundo_cor:
                        break

            if self.player_massa > 100 and self.player_massa < 200:
                self.player_velocidade = 355
                self.pontos_por_comida = 8
            if self.player_massa > 400:
                self.player_velocidade = 355
                self.pontos_por_comida = 3

            if self.player_massa > 38:
                self.pontos_por_comida = 8
                self.inimigo_cor = self.player_cor[0]
                
            pygame.display.flip()

            dt = clock.tick(60) / 1000

    def criar_massas(self, x):
        for c in range(x):
            lugar_aleatorio_x = random.randrange(1, 1080)
            lugar_aleatorio_y = random.randrange(1, 650)

            self.lugares_aletorios.append([lugar_aleatorio_x, lugar_aleatorio_y])
            self.comida.append(pygame.draw.circle(self.tela, self.player_cor[0], self.lugares_aletorios[c], self.massa_comida))

    def manter_massas(self, x):
        for c in range(x):
            self.comida[c] = pygame.draw.circle(self.tela, self.player_cor[0], self.lugares_aletorios[c], self.massa_comida)

    def colisao_comida(self):
        for c, comida in enumerate(self.comida):
            if Functions.verificar_colisao((self.player_pos.x, self.player_pos.y, self.player_massa), (comida[0], comida[1], comida[2])):
                del self.comida[c]
                del self.lugares_aletorios[c]
                self.player_massa += self.pontos_por_comida
                self.pontos += 1
                self.criar_massas(1)
                    
        self.tela.blit(self.texto_formatado, (10, 10))

class Game_over:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Regular Game')

        largura = 1080
        altura = 650

        #Contador de levels e pontos
        pontos = 0 #Conta pontos
        contador = 1 #Conta levels

        self.tela = pygame.display.set_mode((largura, altura))
        self.fundo_cor = Transicions.Trans.backgroud_color(contador)
        self.fonte = pygame.font.SysFont('arial', 40, True, True)   
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()
            if not keys[pygame.K_SPACE]:
                self.tela.fill((0, 0, 0))  # Preenche a tela com a cor preta
                fonte_game_over = pygame.font.SysFont('arial', 80, True, True)
                mensagem_game_over = fonte_game_over.render('Game Over', True, (255, 255, 255))
                self.tela.blit(mensagem_game_over, (self.tela.get_width() // 2 - mensagem_game_over.get_width() // 2, self.tela.get_height() // 2 - mensagem_game_over.get_height() // 2))
                pygame.display.flip()
                pygame.display.flip()
            else:
                Jogo_Hardcore()

class Functions:
    def verificar_colisao(circulo1, circulo2):
        x1, y1, raio1 = circulo1
        x2, y2, raio2 = circulo2

        # Calcula a distância entre os centros dos círculos
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Verifica se há colisão
        if distancia <= raio1 + raio2:
            return True
        else:
            return False

if __name__ == "__main__":
    Start()