from random import randint as ri
from random import choice as r_choice

NAMES = ['Nina_com', 'Steve_com', 'Marike_com', 'Lena_com', 'Aimie_com', 'Alfred_com', 'Dean_com', 'Dexter_com', 'Myla_com', 'Eduard_com']

possible_moves = dict()
pairs = list()


def make_move(board_state: int, board_pic: str) -> (int):
    if pairs:
      if board_state[pairs[-1][0]][pairs[-1][1]] == -1:
        pairs.pop()
      else:
        if board_state[pairs[-1][0]][pairs[-1][1]] == 0:
          return pairs.pop() 
    
    while True:
      x = ri(0, len(board_state)-1)
      y = ri(0, len(board_state[x-1])-1)
      pic = board_pic[x][y]
      
      if board_state[x][y] == 0:
        if pic in possible_moves:
          if len(possible_moves[pic]) == 2:
            pairs.append(possible_moves[pic][0])
            pairs.append(possible_moves[pic][1])
            del possible_moves[pic]
          else:
            if (x,y) not in possible_moves[pic]:
              possible_moves[pic].append((x,y))
        else:
          possible_moves.setdefault(pic,[(x,y)])
        return (x, y)


def get_name(list_of_players) -> str:
  while True:
    name = r_choice(NAMES)
    if not name in list_of_players:
      return name
