from random import randint as ri
from random import choice as r_choice

NAMES = ['Nina_com', 'Steve_com', 'Marike_com', 'Lena_com', 'Aimie_com', 'Alfred_com', 'Dean_com', 'Dexter_com', 'Myla_com', 'Eduard_com']


def make_move(board) -> str:
  while True:
    x = ri(0, len(board)-1)
    y = ri(0, len(board[x-1])-1)
    if board[x][y] == 0:
      return str(x) + str(y)


def get_name(list_of_players) -> str:
  while True:
    name = r_choice(NAMES)
    if not name in list_of_players:
      return name