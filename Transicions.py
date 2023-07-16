import Balloop
import random
cores = ['purple', 'blue'], ['black', 'red',], ['yellow', 'purple'], ['green', 'black']
class Trans:
    # def __init__(self, x):
    #     for c in range()
    #      
    # Define a cor do player e de fundo do game
    def backgroud_color(x):
        if x > len(cores): # caso acabe as programadas, começa a gerar cores aleatórias!
            x = random.randrange(len(cores))      
        return cores[x][0]

    def player_color(x):
        if x > len(cores):
            x = random.randrange(len(cores))  
        return cores[x][1]
