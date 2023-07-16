import Balloop
import random
cores = ['purple', 'black'], ['black', 'red',], ['red', 'green'], ['green', 'black'], ['black', 'purple'], ['purple', 'black']
class Trans:
    # def init(self, x):
    #     for c in range()
    #
    def backgroud_color(x):
        if x > len(cores): # caso acabe as programadas, começa a gerar cores aleatórias!
            x = random.randrange(len(cores))    
        return cores[x - 1][0]

    def player_color(x):
        if x > len(cores): # caso acabe as programadas, começa a gerar cores aleatórias!
            x = random.randrange(len(cores))    
        return cores[x - 1][1]