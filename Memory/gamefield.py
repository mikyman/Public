import picture
import clearscreen
import computer
from platform import system
# https://docs.python.org/3.7/library/stdtypes.html?highlight=list

class Gamefield(object):
  def __init__(self, length, height):
    # if 52 >= length*height >= 4
    if (length*height) > 81 or (length*height) < 4:
      raise Exception('\nThe valid range of (LENGTH x HEIGHT) must be between 4 and 81!')
    elif length < 1 or length > 9:
      raise Exception('\nThe valid range of length must be between 1 and 9!')
    elif height < 1 or height > 9:
      raise Exception('\nThe valid range of height must be between 1 and 9!')
    else:
      self.LENGTH = length
      self.HEIGHT = height
      self.picture = picture.Picture((self.LENGTH*self.HEIGHT)//4, self.LENGTH, ((self.LENGTH*self.HEIGHT)%4) > 1)
      self.state = self.reset_board()
      self.board = self.__init_board()

  def reset_board(self):
    state = [0] * self.picture.number_of_pairs * 4

    while (self.LENGTH * self.HEIGHT) - len(state) > 0:
      if (self.LENGTH * self.HEIGHT) - len(state) == 1:
        state.append(-1)
      else:
        state.append(0)
        state.append(0)
 
    return [state[i:i+self.LENGTH] for i in range(0, len(state), self.LENGTH)]
  
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
        board.append('╔' + ('═══' + '╦')*(self.LENGTH-1) + '═══' + '╗')
      else:
        board.append('╔═══╗')
      # center of board
      if self.LENGTH == 1:
        board.append('║ ' + self.picture.backsite + ' ║')
      else:
        board.append(('║ ' + self.picture.backsite + ' ')*self.LENGTH + '║')
      # end of board
      if self.HEIGHT > 1 and self.LENGTH >= 1:
        board.append('╠' + '═══╬'*(self.LENGTH-1) + '═══╣')
      if self.LENGTH == 1:
        board.append('╚' + '═══' + '╝')
      else:
        board.append('╚' + ('═══' + '╩')*(self.LENGTH-1) + '═══' + '╝')
    # asciicode for Android OS
    else:
      # head of board
      if self.LENGTH > 1:
        board.append('.' + ('---' + '-')*(self.LENGTH-1) + '---' + '.')
      else:
        board.append('.---.')
      # center of board
      if self.LENGTH == 1:
        board.append('| ' + self.picture.backsite + ' |')
      else:
        board.append(('| ' + self.picture.backsite + ' ')*self.LENGTH + '|')
      # end of board
      if self.HEIGHT > 1 and self.LENGTH >= 1:
        board.append('|' + '---+'*(self.LENGTH-1) + '---|')
      if self.LENGTH == 1:
        board.append('\'' + '---' + '\'')
      else:
        board.append('\'' + ('---' + '-')*(self.LENGTH-1) + '---' + '\'')
    return board
  
  def __build_board(self):
    total_board = []
    # build body of table
    for column in range(self.HEIGHT):

      # convert String(board[1]) to List => reset
      detail_board = list(self.board[1])
      
      # show the boardstate
      for row in range(self.LENGTH):

        # show the backsite
        # | ~ | ~ | ~ |
        if self.state[column][row] == 0:
          if detail_board[(row*4)+2] == self.picture.backsite:
            continue
          detail_board[(row*4)+2] = self.picture.backsite

        # show an empty field
        # | ~ |   | ~ |
        elif self.state[column][row] == -1:
          if detail_board[(row*4)+2] == ' ':
            continue
          detail_board[(row*4)+2] = ' '
    
        # show the picture
        # | ~ | M | ~ |
        elif self.state[column][row] == 1:
          if detail_board[(row*4)+2] == self.picture.frontsite[column][row]:
            continue
          detail_board[(row*4)+2] = self.picture.frontsite[column][row]
  
      # convert List to String back
      total_board.append("".join(detail_board))
    return total_board
      
  def print_board(self):
    game_board = self.__build_board()
    clearscreen.clear()
    # print head of table
    print()
    print(end = '   ')
    for i in range(self.LENGTH):
      print('   {}'.format(i+1), end = '')
    print()
    print('    {}'.format(self.board[0]))
    
    for column in range(self.HEIGHT):
      print('    {} {}'.format(game_board[column], (column+1)))
      if column < self.HEIGHT-1:
        print('    {}'.format(self.board[2]))
    print('    {}'.format(self.board[-1]))
    return 0
    
  def bord_is_empty(self):
    for i in range(len(self.state)):
      for j in range(len(self.state[i])):
        if self.state[i][j] == 0:
          return False
    return True
      
  def choose_field(self, player_name):
    pos_x = [0, 0]
    pos_y = [0, 0]
    invalid = False
    move = 0
    
    if player_name.endswith('_com'):
      move_com = []
    
    while(move < 2):
      if invalid:
        input(' Press Enter to continue...')
        self.print_board()
        invalid = False
      
      if not player_name.endswith('_com'):
        try:
          print('\n   {}, please enter a number'.format(player_name))
          print('   (e.g. {length}1 for the right-up-corner or'.format(length = self.LENGTH))
          print('    0 for the Mainmenu)')
          inp = input('   Choose your field: ')[:2]

          #Mainmenu
          if int(inp) == 0:
            if input(' Are you sure, you want to the Mainmenu?\n (This Game will not be saved) (Yes/No): ').lower().startswith('y'):
              return 2
            self.print_board()
            continue

          # if Invalid Input try it again
          if len(inp) < 2 or int(inp) <= 9 or inp[1] == '0' or int(inp[1]) > self.HEIGHT or int(inp[0]) > self.LENGTH:
            print()
            print('  INVALID MOVE!')
            print(" Please enter the first number as Length\n und the second number as Height\n e.g. {}1 for the right-up-corner".format(self.LENGTH))
            invalid = True

        except ValueError:
          print()
          print('  INVALID VALUE!\n Please enter ONLY a number of digits!')
          invalid = True
        except Exception as e:
          exit(e)
              
        if not invalid:
          # set user input as coordinates
          pos_x[move] = int(inp[1])-1
          pos_y[move] = int(inp[0])-1

          # if field is empty: picture has already been found
          if self.state[pos_x[move]][pos_y[move]] == -1:
            print()
            print('  INVALID MOVE!\n This picture has already been found!')
            invalid = True
          # already selected field
          elif self.state[pos_x[move]][pos_y[move]] == 1:
            print()
            print('  INVALID MOVE!\n This field has already been selected!')
            invalid = True
          # No complications  
          else:
            self.state[pos_x[move]][pos_y[move]] = 1
            self.print_board()
            move += 1
      else:
        # print comuter's move
        inp = computer.make_move(self.state)
        move_com.append(str(int(inp[1]) + 1) + str(int(inp[0]) + 1))
        pos_x[move] = int(inp[0])
        pos_y[move] = int(inp[1])
        self.state[pos_x[move]][pos_y[move]] = 1
        move += 1
        if move == 2:
          self.print_board()
          print()
          print('  {} choosed {} and {}'.format(player_name, move_com[0], move_com[1]))
          
    # choose fields are same 
    if self.picture.frontsite[pos_x[0]][pos_y[0]] == self.picture.frontsite[pos_x[1]][pos_y[1]]:
      self.state[pos_x[0]][pos_y[0]] = self.state[pos_x[1]][pos_y[1]] = -1
      return 1
    # else next players round
    else:
      self.state[pos_x[0]][pos_y[0]] = self.state[pos_x[1]][pos_y[1]] = 0
    return 0
