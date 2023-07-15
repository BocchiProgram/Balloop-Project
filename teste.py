import pygame
import random

from pygame.locals import *
from sys import exit

clock = pygame.time.Clock()

pygame.init()

largura = 1080
altura = 650
dt = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Regular Game')

player_pos = pygame.Vector2(tela.get_width() / 2, tela.get_height() / 2)
massa = False
player_massa = 20

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.fill("black")

    if massa == False:
        lugar_aleatorio_x = random.randrange(1, 1080)
        lugar_aleatorio_y = random.randrange(1, 650)
        
        local_comida = (lugar_aleatorio_x, lugar_aleatorio_y)
        massa = True

    pygame.draw.circle(tela, "blue", local_comida, 10)

    X_teste = player_pos.x - lugar_aleatorio_x
    Y_teste = player_pos.y - lugar_aleatorio_y
    if X_teste < 10 and X_teste > - 10:
        if Y_teste < 10 and Y_teste > - 10:
            player_massa += 5
            massa = False
            
            

    # print(f'{player_pos.x - lugar_aleatorio_x} X ')
    # print(f'{player_pos.y - lugar_aleatorio_y} Y ')

    #player 
    
    class Comida:
        comida = pygame.draw.circle(tela, "white", player_pos, player_massa)
        
        def colidir(self, player):
            comida_mask = pygame.mask.from_surface(self.comida)
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 200 * dt
    if keys[pygame.K_d]:
        player_pos.x += 200 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 200 * dt
    if keys[pygame.K_s]:
        player_pos.y += 200 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000