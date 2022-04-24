from random import randint as ri
from random import choice as r_choice

NAMES = ['Nina_com', 'Steve_com', 'Marike_com', 'Lena_com', 'Aimie_com', 'Alfred_com', 'Dean_com', 'Dexter_com', 'Myla_com', 'Eduard_com']

possible_moves = dict()
pairs = list()


def make_move(board_state: list, board_pic: list, column_length) -> tuple:
  if pairs:
    # if board_state -1 => pair was already found
    if board_state[pairs[-1][-1]] == -1:
      pairs.pop()
    else:
      # else return this coord's
      if board_state[pairs[-1][-1]] == 0:
        return pairs.pop() 
  
  while True:
    rnd_index = ri(0, len(board_state)-1)
    x = rnd_index % column_length
    y = rnd_index // column_length
    
    # if board[x][y] is not empty or always selected
    # save the pic with that coord's in possible_moves
    # are 2 coord's in from same pic, the copy this coord'S
    # in pairs and remove it from the possible moves
    if board_state[rnd_index] == 0:
      pic = board_pic[y][x]
      if pic in possible_moves:
        if len(possible_moves[pic]) == 2:
          pairs.append(possible_moves[pic][0])
          pairs.append(possible_moves[pic][1])
          del possible_moves[pic]
        elif (x,y,rnd_index) in possible_moves[pic]:
          continue
        else:
          possible_moves[pic].append((x,y,rnd_index))
      else:
        possible_moves.setdefault(pic,[(x,y,rnd_index)])
      return (x, y, rnd_index)


def get_name(list_of_players) -> str:
  while True:
    name = r_choice(NAMES)
    if not name in list_of_players:
      return name
