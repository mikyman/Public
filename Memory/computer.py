from field_state import Field_State

from random import randint as ri
from random import choice as r_choice


class Computer:
  NAMES = ['Nina_com', 'Steve_com', 'Marike_com', 'Lena_com', 'Aimie_com',
           'Alfred_com', 'Dean_com', 'Dexter_com', 'Myla_com', 'Eduard_com']

  possible_moves = dict()
  pairs = list()

  @classmethod
  def make_move(cls, board_state: list, board_pic: list, column_length) -> tuple:
    if cls.pairs:
      # if board_state is EMPTY => pair was already found
      if board_state[cls.pairs[-1][-1]] == Field_State.EMPTY:
        cls.pairs.pop()
      # else return this coord's
      elif board_state[cls.pairs[-1][-1]] == Field_State.BACKSITE:
          return cls.pairs.pop()

    while True:
      rnd_index = ri(0, len(board_state)-1)
      x = rnd_index % column_length
      y = rnd_index // column_length

      # if board[x][y] is not empty or always selected
      # save the pic with that coord's in possible_moves
      # are 2 coord's in from same pic, the copy this coord'S
      # in 'pairs' and remove it from the possible moves
      if board_state[rnd_index] == Field_State.BACKSITE:
        pic = board_pic[y][x]
        if pic in cls.possible_moves:
          if len(cls.possible_moves[pic]) == 2:
            cls.pairs.extend(cls.possible_moves[pic])
            del cls.possible_moves[pic]
          elif (x, y, rnd_index) in cls.possible_moves[pic]:
            continue
          else:
            cls.possible_moves[pic].append((x, y, rnd_index))
        else:
          cls.possible_moves.setdefault(pic, [(x, y, rnd_index)])
        return (x, y, rnd_index)

  @classmethod
  def get_name(cls, list_of_players) -> str:
    while True:
      name = r_choice(cls.NAMES)
      if name not in list_of_players:
        return name
