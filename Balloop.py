import pygame
import random
import Transicions
import math
import yaml
from button import Button
from pygame.locals import *
from sys import exit


with open('config.yaml') as f:
    config = yaml.safe_load(f)

if config['level'] == '':
    config['level'] = 1
                
    with open('config.yaml', 'w') as f:
        yaml.dump(config, f)
            

class Start:
    def __init__(self):
        clock = pygame.time.Clock()

        pygame.init()
        pygame.display.set_caption('Regular Game')

        largura = 1080
        altura = 650
        dt = 0

        self.tela = pygame.display.set_mode((largura, altura))
        self.fundo_cor = Transicions.Trans.backgroud_color(1)
        self.fonte = pygame.font.SysFont('arial', 40, True, True)        

        self.player_pos = pygame.Vector2(self.tela.get_width() / 2, self.tela.get_height() / 2)
        self.player_massa = 20
        self.player_cor = [Transicions.Trans.player_color(1), 'orange']
        self.player_cor_number = 0
        self.player_velocidade = 320

        while True: 
            self.mensagem1 = f'PEACEFUL'
            self.texto_formatado1 = self.fonte.render(self.mensagem1, True, ('green'))

            self.mensagem2 = f'ADVENTURE'
            self.texto_formatado2 = self.fonte.render(self.mensagem2, True, ('yellow'))

            self.mensagem3 = f'HARDCORE'
            self.texto_formatado3 = self.fonte.render(self.mensagem3, True, ('red'))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            self.tela.fill(self.fundo_cor)
            
            #player 
            self.player = pygame.draw.circle(self.tela, self.player_cor[self.player_cor_number], self.player_pos, self.player_massa)   

            Functions.andar_player(dt, self.player_pos, self.player_velocidade)

            self.colisao_texto() 
            pygame.display.flip()

            dt = clock.tick(60) / 1000

    def colisao_texto(self):         
        self.tela.blit(self.texto_formatado1, (self.tela.get_width() / 2 - self.texto_formatado1.get_width() // 2, 500))
        self.tela.blit(self.texto_formatado2, (50, 50))
        self.tela.blit(self.texto_formatado3, (840, 50))

        texto_rect1 = self.texto_formatado3.get_rect(topleft=(840, 50))
        jogador_rect1 = pygame.Rect(self.player_pos.x - self.player_massa, self.player_pos.y - self.player_massa, self.player_massa * 2, self.player_massa * 2)

        
        if texto_rect1.colliderect(jogador_rect1):
                Dificuldade.hardcore()

        texto_rect2 = self.texto_formatado3.get_rect(topleft=(self.tela.get_width() / 2 - self.texto_formatado1.get_width() // 2, 500))
        jogador_rect2 = pygame.Rect(self.player_pos.x - self.player_massa, self.player_pos.y - self.player_massa, self.player_massa * 2, self.player_massa * 2)
        
        if texto_rect2.colliderect(jogador_rect2):
                Dificuldade.pacifico()
        
        texto_rect3 = self.texto_formatado3.get_rect(topleft=(50, 50))
        jogador_rect3 = pygame.Rect(self.player_pos.x - self.player_massa, self.player_pos.y - self.player_massa, self.player_massa * 2, self.player_massa * 2)
        
        if texto_rect3.colliderect(jogador_rect3):
                Dificuldade.adventure(self.tela)

class Jogo:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.timer_tempo = 0
        self.timer_tempo_real = 0

        pygame.init()
        pygame.display.set_caption('Regular Game')

        self.dt = 0
        self.largura = 1080
        self.altura = 650
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.fonte = pygame.font.SysFont('arial', 40, True, True)  

        self.player_pos = pygame.Vector2(self.tela.get_width() / 2, self.tela.get_height() / 2)
        
        self.inimigos = []
        self.lugares_aleatorios_inimigos = []
        self.inimigo_cor = 'red'
        self.inimigo_massa = 8
        self.inimigo_x = self.largura
        self.inimigo_y = self.altura

        self.velocidade_x = []
        self.velocidade_y = []
        
        self.comida = []
        self.lugares_aletorios = []

    def run(self, atributos):
        self.atributos = atributos
        #Contador de levels e pontos
        self.pontos = atributos['pontos'][0] #Conta pontos
        self.contador = atributos['contador'][0] #Conta levels

        self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
        
        self.player_massa = atributos['player_massa'][0]
        self.player_cor = [Transicions.Trans.player_color(self.contador), 'orange']
        self.player_cor_number = atributos['player_cor_number'][0]
        self.player_velocidade = atributos['player_velocidade'][0]
    
        while True:
            self.player_cor[0] = Transicions.Trans.player_color(self.contador) 
            if self.player_cor[0] != self.fundo_cor:
                break

        
        self.pontos_por_comida = atributos['pontos_por_comida'][0]
        self.massa_comida = atributos['massa_comida'][0]

        self.criar_massas(atributos['criar_massas'][0])
        if atributos['inimigos']:
            self.criar_inimigos(self.contador)

        while True: 
            self.mensagem = f'Pontos: {self.pontos}'
            self.texto_formatado = self.fonte.render(self.mensagem, True, (255, 255, 255))

            self.mensagem1 = f'Level: {self.contador}'
            self.texto_formatado_level = self.fonte.render(self.mensagem1, True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            self.tela.fill(self.fundo_cor)
            self.manter_massas(atributos['criar_massas'][0])
            if atributos['inimigos']:
                self.manter_inimigos(len(self.inimigos))
            
            #player 
            self.player = pygame.draw.circle(self.tela, self.player_cor[self.player_cor_number], self.player_pos, self.player_massa) 
              
            if atributos['inimigos']:
                Functions.andar_inimigos(self.lugares_aleatorios_inimigos, self.velocidade_x, self.velocidade_y)
            Functions.andar_player(self.dt, self.player_pos, self.player_velocidade)
            Functions.pause(self.tela)

            self.timer_tempo += 1
            if self.timer_tempo == 57:
                self.timer_tempo_real += 1
                self.timer_tempo = 0

            self.colisao_comida()
            if atributos['inimigos']:
                if self.timer_tempo_real > 3:
                    self.colisao_inimigo()
                    self.player_cor_number = atributos['player_cor_number'][1]
                else:
                    if self.timer_tempo < 27.5:
                        self.player_cor_number = atributos['player_cor_number'][2]
                    else:
                        self.player_cor_number = atributos['player_cor_number'][3] 
            
            if self.player_massa > 1500:
                self.timer_tempo_real = 0
                self.inimigo_cor = 'red'
                self.player_velocidade = atributos['player_velocidade'][1]
                self.massa_comida = atributos['massa_comida'][1]
                self.player_massa = atributos['player_massa'][1]
                self.contador += 1
                if atributos['modo'] == 'adventure':
                    config['level'] = int(self.contador) / 5
                        
                    with open('config.yaml', 'w') as f:
                        yaml.dump(config, f)
                self.pontos_por_comida = atributos['pontos_por_comida'][1]
                if atributos['inimigos']:
                    self.criar_inimigos(self.contador)
                self.fundo_cor = Transicions.Trans.backgroud_color(self.contador)
                while True:
                    self.player_cor[0] = Transicions.Trans.player_color(self.contador) 
                    if self.player_cor[0] != self.fundo_cor:
                        break

            if self.player_massa > 100 and self.player_massa < 200:
                self.player_velocidade = atributos['player_velocidade'][2]
                self.pontos_por_comida = atributos['pontos_por_comida'][2]
            if self.player_massa > 400:
                self.player_velocidade = atributos['player_velocidade'][3]
                self.pontos_por_comida = atributos['pontos_por_comida'][3]

            if self.player_massa > 38:
                self.pontos_por_comida = atributos['pontos_por_comida'][4]
                self.inimigo_cor = self.player_cor[0]
                
            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

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

            self.velocidade_x.append(c + 0.2)
            self.velocidade_y.append(c + 0.2)

            if self.contador > 1:
                self.velocidade_x.append(- 1)
                self.velocidade_y.append(- 1)

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
                del self.comida[c], self.lugares_aletorios[c]
                self.player_massa += self.pontos_por_comida
                self.pontos += 1
                self.criar_massas(1)
                    
        self.tela.blit(self.texto_formatado, (10, 10))

        self.tela.blit(self.texto_formatado_level, (910, 10))

    def colisao_inimigo(self):
        for c, inimigo in enumerate(self.inimigos):
            if Functions.verificar_colisao((self.player_pos.x, self.player_pos.y, self.player_massa), (inimigo[0], inimigo[1], inimigo[2])):
                if self.player_massa >38:
                    del self.inimigos[c], self.lugares_aleatorios_inimigos[c], self.velocidade_x[c], self.velocidade_y[c]
                else:
                    self.gameover()
                self.player_massa += self.pontos_por_comida
                self.pontos += 10
                    
        self.tela.blit(self.texto_formatado, (10, 10))

    def gameover(self):
        pygame.init()
        pygame.display.set_caption('Regular Game')

        largura = 1080
        altura = 650
        contador = 1

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
                mensagem_game_over = fonte_game_over.render('Game Over', True, ('red'))
                self.tela.blit(mensagem_game_over, (self.tela.get_width() // 2 - mensagem_game_over.get_width() // 2, self.tela.get_height() // 2 - mensagem_game_over.get_height() // 2))

                fonte_try_again = pygame.font.SysFont('arial', 30, True, True)
                mensagem_try_again = fonte_try_again.render("Press 'space' to try again!", True, (255, 255, 255))
                self.tela.blit(mensagem_try_again, (self.tela.get_width() // 2 - mensagem_try_again.get_width() // 2, 390 - mensagem_try_again.get_height() // 2))

                pygame.display.flip()
                pygame.display.flip()
            else:
                if self.atributos['modo'] == 'hardcore':
                        Dificuldade.hardcore()
                
                if self.atributos['modo'] == 'adventure':
                        Dificuldade.adventure()

class Dificuldade:
    def hardcore():
        atributos = {
            'modo': 'hardcore',
            'inimigos': True,
            'contador': [1],
            'player_massa': [20, 20],
            'pontos': [0],
            'player_cor_number': [0, 0, 1, 0],
            'player_velocidade': [360, 360, 355, 355],
            'pontos_por_comida': [2, 2, 10, 5, 15],
            'massa_comida': [5, 5],
            'timer_tempo_real': [0],
            'inimigo_cor': ['red'],
            'criar_massas': [20]
        }   
        jogo = Jogo()
        jogo.run(atributos)
        
    def pacifico():
        atributos = {
            'modo': 'pacifico',
            'inimigos': False,
            'pontos': [0],
            'contador': [1],
            'player_massa': [20, 20],
            'player_cor_number': [0, 0, 0, 0],
            'player_velocidade': [320, 320, 355, 355],
            'pontos_por_comida': [5, 5, 15, 1, 5],
            'massa_comida': [5, 5],
            'timer_tempo_real': [0],
            'criar_massas': [20]
        }
        jogo = Jogo()
        jogo.run(atributos)
    
    def adventure(tela):
        atributos = {
            'modo': 'adventure',
            'inimigos': True,
            'contador': [config['level']],
            'player_massa': [20, 20],
            'pontos': [0],
            'player_cor_number': [0, 0, 1, 0],
            'player_velocidade': [360, 360, 355, 355],
            'pontos_por_comida': [2, 2, 10, 5, 15],
            'massa_comida': [5, 5],
            'timer_tempo_real': [0],
            'inimigo_cor': ['red'],
            'criar_massas': [20]
        }

        Functions.level_select(tela)

        # jogo = Jogo()
        # jogo.run(atributos)
    
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
    
    def andar_player(dt, player_pos, player_velocidade):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_pos.y -= player_velocidade * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += player_velocidade * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos.x -= player_velocidade * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_pos.y += player_velocidade * dt
    
    def andar_inimigos(lugares_aleatorios_inimigos, velocidade_x, velocidade_y):
        for c in range(len(lugares_aleatorios_inimigos)):
            lugares_aleatorios_inimigos[c][0] += velocidade_x[c] 
            lugares_aleatorios_inimigos[c][1] += velocidade_y[c]
            
            if lugares_aleatorios_inimigos[c][0] <= 0 or lugares_aleatorios_inimigos[c][0] >= 1080:
                velocidade_x[c] *= -1

            if lugares_aleatorios_inimigos[c][1] <= 0 or lugares_aleatorios_inimigos[c][1] >= 650:
                velocidade_y[c] *= -1

    def pause(tela):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            c = False
            while not c:
                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                tela.fill("black")

                PLAY_TEXT = pygame.font.SysFont('arial', 80, True, True).render("PAUSED.", True, "white")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(tela.get_width() / 2, tela.get_height() / 4))
                tela.blit(PLAY_TEXT, PLAY_RECT)

                PLAY_MAIN_MENU = Button(image=None, pos=(tela.get_width() / 2, 400), 
                            text_input="MAIN MENU", font=pygame.font.SysFont('arial', 60, True, True), base_color="White", hovering_color="Green")
                PLAY_MAIN_MENU.changeColor(PLAY_MOUSE_POS)
                PLAY_MAIN_MENU.update(tela)

                PLAY_BACK = Button(image=None, pos=(tela.get_width() / 2, 460), 
                            text_input="BACK", font=pygame.font.SysFont('arial', 60, True, True), base_color="White", hovering_color="Green")
                PLAY_BACK.changeColor(PLAY_MOUSE_POS)
                PLAY_BACK.update(tela)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                            c = True
                        
                        if PLAY_MAIN_MENU.checkForInput(PLAY_MOUSE_POS):
                            c = True
                            Start()
                            

                pygame.display.update()

    def level_select(tela):
        LEVEIS = []
        for c in range(config['level']):
            c += 1
            LEVEIS.append(c)

        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            tela.fill("black")

            CHOOSE_TEXT = pygame.font.SysFont('arial', 60, True, True).render("CHOOSE LEVEL.", True, "white")
            CHOOSE_RECT = CHOOSE_TEXT.get_rect(center=(tela.get_width() / 2, tela.get_height() / 10))
            tela.blit(CHOOSE_TEXT, CHOOSE_RECT)

            PLAY_MAIN_MENU = Button(image=None, pos=(tela.get_width() / 2, 580), 
                        text_input="MAIN MENU", font=pygame.font.SysFont('arial', 40, True, True), base_color="White", hovering_color="Green")
            PLAY_MAIN_MENU.changeColor(PLAY_MOUSE_POS)
            PLAY_MAIN_MENU.update(tela)

            PLAY_BACK = Button(image=None, pos=(tela.get_width() / 2, 630), 
                        text_input="BACK", font=pygame.font.SysFont('arial', 40, True, True), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(tela)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for level in range(0, 30, 10):
                
                for c in range(10):
                    c +=1
                    botao_level = Button(image=None, pos=(c * 100, 250 + (level * 8)), 
                            text_input=f"{level + c}", font=pygame.font.SysFont('arial', 50, True, True), base_color="White", hovering_color="Green")
                    botao_level.changeColor(PLAY_MOUSE_POS)
                    botao_level.update(tela)

            pygame.display.update()

            
if __name__ == "__main__":
    Start()