import Balloop
cores = ['purple', 'black'], ['black', 'red',], ['red', 'green'], ['green', 'black'], ['black', 'purple'], ['purple', 'black']
class Trans:
    # def init(self, x):
    #     for c in range()
    #
    def backgroud_color(x):
        return cores[x - 1][0]

    def player_color(x):
        return cores[x - 1][1]