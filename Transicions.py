import random
cores = cores = [
    # Sequência 1
    ['black', 'lightgreen'],

    # Sequência 2
    ['lightgreen', 'black'],

    # Sequência 3
    ['black', 'green'],

    # Sequência 4
    ['green', 'black'],

    # Sequência 5
    ['black', 'pink'],

    # Sequência 6
    ['pink', 'black'],

    # Sequência 7
    ['black', 'yellow'],

    # Sequência 8
    ['yellow', 'black'],

    # Sequência 9
    ['black', (0, 0, 255)],

    # Sequência 10
    [(0, 0, 255), 'black'],

    # Sequência 11
    ['black', (0, 128, 0)],

    # Sequência 12
    [(0, 128, 0), 'black'],

    # Sequência 13
    ['black', (255, 0, 255)],

    # Sequência 14
    [(255, 0, 255), 'black'],

    # Sequência 15
    ['black', (0, 128, 128)],

    # Sequência 16
    [(0, 128, 128), 'black'],

    # Sequência 17
    ['black', (0, 255, 255)],

    # Sequência 18
    [(0, 255, 255), 'black'],

    # Sequência 19
    ['black', (0, 255, 0)],

    # Sequência 20
    [(0, 255, 0), 'black'],

    # Sequência 21
    ['black', (255, 0, 0)],

    # Sequência 22
    [(255, 0, 0), 'black'],

    # Sequência 23
    ['black', (128, 0, 0)],

    # Sequência 24
    [(128, 0, 0), 'black'],

    # Sequência 25
    ['black', (255, 165, 0)],

    # Sequência 26
    [(255, 165, 0), 'black'],

    # Sequência 27
    ['black', (0, 0, 139)],

    # Sequência 28
    [(0, 0, 139), 'black'],

    # Sequência 29
    ['black', (128, 0, 128)],

    # Sequência 30
    [(128, 0, 128), 'black']
]

class Trans:
    def backgroud_color(x):
        if x > len(cores): # caso acabe as programadas, começa a gerar cores aleatórias!
            x = random.randrange(len(cores))  
        return cores[x - 1][0]

    def player_color(x):
        if x > len(cores): # caso acabe as programadas, começa a gerar cores aleatórias!
            x = random.randrange(len(cores))    
        return cores[x - 1][1]