import random
cores = ['black', 'blue'], ['blue', 'black'], ['black', 'green'], ['green', 'black'], ['black', 'pink'], ['pink', 'black'],['black', 'yellow'], ['yellow', 'black']

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

    def invuneravel(x):
        if x is 'black':
            return 'white'
        else:
            return 'grey'