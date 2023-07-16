import Balloop

class Trans:
    def __init__(self):
        if Balloop.player_massa > 700:
            self.player_massa = 20
            return self.player_massa
        else:
            self.player_massa = Balloop.player_massa
            return self.player_massa
        

# def leve1_finished(player_massa):
#     if player_massa > 700:
#         player_massa = 20
#         player_cor = 'red'
#         fundo_cor = 'black'
#     return player_massa, player_cor, fundo_cor
