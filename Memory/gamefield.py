import picture
import clearscreen
import computer
from platform import system
# https://docs.python.org/3.7/library/stdtypes.html?highlight=list


class Gamefield(object):
  def __init__(self, length, height):
    # if 52 >= length*height >= 4
    if (length*height) > 81 or (length*height) < 4:
      raise Exception(
        '\nThe valid range of (LENGTH x HEIGHT) must be between 4 and 81!')
    elif length < 1 or length > 9:
      raise Exception('\nThe valid range of length must be between 1 and 9!')
    elif height < 1 or height > 9:
      raise Exception('\nThe valid range of height must be between 1 and 9!')
    else:
      self.LENGTH = length
      self.HEIGHT = height
      self.FIELD_SIZE = self.LENGTH * self.HEIGHT
      self.board = ['~'] * self.FIELD_SIZE
      self.picture = picture.Picture(
        self.FIELD_SIZE // 4, self.LENGTH, (self.FIELD_SIZE % 4) > 1)
      self.state = self.reset_board()
      self.construct = self.__init_board()

  def reset_board(self):
    state = [0] * self.picture.number_of_pairs * 4
    while self.FIELD_SIZE - len(state) > 0:
      if self.FIELD_SIZE - len(state) == 1:
        state.append(-1)
      else:
        state.append(0)
        state.append(0)
    return state

  def __init_board(self):
    # ╔ ═ ╗║╚ ╝╠ ╣╦ ╬ ╩
    # ╔ U+2554,═ U+2550,╗ U+2557,║ U+2551,╚ U+255A,╝ U+255D,╠ U+2560,╣ U+2563,╦ U+2564,╬ U+256C,╩ U+2569
    # ┌ ─ ┐│└ ┘├ ┤┬ ┼ ┴
    # ┌ U+250C,─ U+2500,┐ U+2510,│ U+2502,└ U+2514,┘ U+2518,├ U+251C,┤ U+2524,┬ U+252C,┼ U+253C,┴ U+2534
    # print that as print(u'\u251C\u253C\u2524') for ├┼┤ (the first 'u' in print is obtional)
    board = []
    # unicode for Windows OS
    if system() == 'Windows':
      # head of board
      if self.LENGTH > 1:
        board.append('╔' + ('═══' + '╦') * (self.LENGTH - 1) + '═══' + '╗')
      else:
        board.append('╔═══╗')
      # center of board
      # old
      # if self.LENGTH == 1:
        # board.append('║ ' + self.picture.backsite + ' ║')
      # else:
        # board.append(('║ ' + self.picture.backsite + ' ')*self.LENGTH + '║')
      # new
      board.append(' ║ ')
      # end of board
      if self.HEIGHT > 1 and self.LENGTH >= 1:
        board.append('╠' + '═══╬' * (self.LENGTH - 1) + '═══╣')
      if self.LENGTH == 1:
        board.append('╚' + '═══' + '╝')
      else:
        board.append('╚' + ('═══' + '╩') * (self.LENGTH - 1) + '═══' + '╝')
    # asciicode for Android OS
    else:
      # head of board
      if self.LENGTH > 1:
        board.append('.' + ('---' + '-') * (self.LENGTH - 1) + '---' + '.')
      else:
        board.append('.---.')
      # center of board
      # old
      # if self.LENGTH == 1:
        # board.append('| ' + self.picture.backsite + ' |')
      # else:
        # board.append(('| ' + self.picture.backsite + ' ')*self.LENGTH + '|')
      # new
      board.append(' | ')
      # end of board
      if self.HEIGHT > 1 and self.LENGTH >= 1:
        board.append('|' + '---+' * (self.LENGTH - 1) + '---|')
      if self.LENGTH == 1:
        board.append('\'' + '---' + '\'')
      else:
        board.append('\'' + ('---' + '-') * (self.LENGTH - 1) + '---' + '\'')
    return board

  def __update(self):
    '''
      # Note for convert single list to multi list and back:
      # one dimensional list to two dimensional list is:
      # iterator % length of line's per column = x-coodinate
      # iterator // length of line's per column = y-coodinate
      # back:
      # two dimensional list to one dimensional list is:
      # y-coordinate times to length of line's per column plus x-coodinate = x,y list
      # x-coordinate times to length of line's per column plus y-coodinate = y,x list
    '''

    # build body of table
    for column in range(self.FIELD_SIZE):
      # show the boardstate
      # for row in range(self.LENGTH):
      # show the backsite
      # | ~ | ~ | ~ |
      if self.state[column] == 0:
        if self.board[column] == self.picture.backsite:
          continue
        self.board[column] = self.picture.backsite
      # show an empty field
      # | ~ |   | ~ |
      elif self.state[column] == -1:
        if self.board[column] == ' ':
          continue
        self.board[column] = ' '
      # show the picture
      # | ~ | M | ~ |
      elif self.state[column] == 1:
        if self.board[column] == self.picture.frontsite[column // self.LENGTH][column % self.LENGTH]:
          continue
        self.board[column] = self.picture.frontsite[column // self.LENGTH][column % self.LENGTH]

  def build_board(self):
    board_lines = []
    for i in range(0, self.FIELD_SIZE+1, self.LENGTH):
      board_lines.append(self.construct[1] +
                         self.construct[1].join(self.board[i:i + self.LENGTH]) +
                         self.construct[1])
    return board_lines

  def print_board(self):
    self.__update()
    game_board = self.build_board()
    clearscreen.clear()
    # print head of table
    print()
    print(end='   ')
    for i in range(self.LENGTH):
      print('   {}'.format(i + 1), end='')
    print()
    print('    {}'.format(self.construct[0]))

    for column in range(self.HEIGHT):
      print('   {} {}'.format(game_board[column], (column + 1)))
      if column < self.HEIGHT-1:
        print('    {}'.format(self.construct[2]))
    print('    {}'.format(self.construct[-1]))

  def board_not_empty(self):
    '''
      check of 0 in state
      if the value 0 in state,
      minimum 2 pictures are on the bord.
    '''
    return (0 in self.state)

  # take two times Coordinates for picture one and picture two
  def choose_field(self, player_name):
    pos_x = [0, 0]
    pos_y = [0, 0]
    index = [0, 0]
    invalid = False
    move = 0

    if player_name.endswith('_com'):
      move_com = []

    while(move < 2):
      if invalid:
        input(' Press Enter to continue...')
        invalid = False
        self.print_board()

      if not player_name.endswith('_com'):
        try:
          print('\n   {}, please choose your field'.format(player_name))
          print('   (e.g. {length}1 for the top right corner or'.format(length=self.LENGTH))
          print('    0 for the Mainmenu)')
          inp = input('   >> ')[:2]
          inp_int = int(inp)

          # Mainmenu
          if inp_int == 0:
            print(' Are you sure, you want to the Mainmenu?')
            if input(' (This Game will not be saved) (Yes/No): ').lower().startswith('y'):
              return 2
            self.print_board()
            continue

          # if Invalid Input try it again
          if (
              (inp_int < 11) or
              (int(inp[0]) > self.LENGTH) or
              (inp[1] == '0' or int(inp[1]) > self.HEIGHT)
             ):
            print()
            print('  INVALID MOVE!')
            print(' Please enter the first number as Length')
            print(' und the second number as Height')
            print(' e.g. {}1 for the right-up-corner'.format(self.LENGTH))
            invalid = True

        except ValueError:
          print()
          print('  INVALID VALUE!\n Please enter ONLY a number of digits!')
          invalid = True
        except Exception as e:
          exit(e)

        if not invalid:
          # set user input as coordinates x,y
          pos_x[move] = int(inp[0])-1
          pos_y[move] = int(inp[1])-1
          index[move] = pos_y[move] * self.LENGTH + pos_x[move]

          # if field is empty: picture has already been found
          if self.state[index[move]] == -1:
            print()
            print('  INVALID MOVE!\n This picture has already been found!')
            invalid = True
          # already selected field
          elif self.state[index[move]] == 1:
            print()
            print('  INVALID MOVE!\n This field has already been selected!')
            invalid = True
          # No complications
          else:
            self.state[index[move]] = 1
            self.print_board()
            move += 1
      else:
        # print comuter's move
        inp = computer.make_move(
          self.state, self.picture.frontsite, self.LENGTH)
        # for better visual user output
        move_com.append(str(inp[0] + 1) + str(inp[1] + 1))
        
        pos_x[move] = inp[0]
        pos_y[move] = inp[1]
        index[move] = inp[2]
        self.state[index[move]] = 1
        move += 1
        if move == 2:
          self.print_board()
          print()
          print('  {} choosed {} and {}'.format(player_name, move_com[0], move_com[1]))

    # choose fields are same
    if self.picture.frontsite[pos_y[0]][pos_x[0]] == self.picture.frontsite[pos_y[1]][pos_x[1]]:
      self.state[index[0]] = self.state[index[1]] = -1
      return 1
    # else next players round
    else:
      self.state[index[0]] = self.state[index[1]] = 0
    return 0
