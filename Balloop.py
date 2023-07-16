import pygame
import random
from time import sleep
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
player_massa = 20
comida = []
lugares_aletorios = []

def criar_massas(x):
    for c in range(x):
        lugar_aleatorio_x = random.randrange(1, 1080)
        lugar_aleatorio_y = random.randrange(1, 650)

        # lugares_aletorios = [lugar_aleatorio_x, lugar_aleatorio_y]
        lugares_aletorios.append([lugar_aleatorio_x, lugar_aleatorio_y])
        comida.append(pygame.draw.circle(tela, "blue", lugares_aletorios[c], 10))


def manter_massas():
    for c in range(5):
        comida[c] = pygame.draw.circle(tela, "blue", lugares_aletorios[c], 10)

criar_massas(5)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        tela.fill('black')

        if len(comida) < 5:
            criar_massas(1)
            
        manter_massas()
        
    #player 
    player = pygame.draw.circle(tela, "white", player_pos, player_massa)   

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 200 * dt
    if keys[pygame.K_d]:
        player_pos.x += 200 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 200 * dt
    if keys[pygame.K_s]:
        player_pos.y += 200 * dt


    if player.collideobjects(comida):
        player_massa +=5
        if player.colliderect(comida[4]):
            del comida[4]
            del lugares_aletorios[4]
        if player.colliderect(comida[3]):
            del comida[3]
            del lugares_aletorios[3]
        if player.colliderect(comida[2]):
            del comida[2]
            del lugares_aletorios[2]
        if player.colliderect(comida[1]):
            del comida[1]
            del lugares_aletorios[1]
        if player.colliderect(comida[0]):
            del comida[0]
            del lugares_aletorios[0]
    

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000