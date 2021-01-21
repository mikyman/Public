from random import randint as ri
from random import choice as r_choice

NAMES = ['Nina_com', 'Steve_com', 'Marike_com', 'Lena_com', 'Aimie_com', 'Alfred_com', 'Dean_com', 'Dexter_com', 'Myla_com', 'Eduard_com']

def make_move(board):
    while True:
        y = ri(1, len(board))
        x = ri(1, len(board[y-1]))
        if board[y-1][x-1] == 0:
            return str(y)+str(x)
            
def get_name(list_of_players):
    while True:
        name = r_choice(NAMES)
        if not name in list_of_players:
            return name