import clearscreen
import gamefield
from player import Player

# This is the classic game of Memory
# Verson: 2.2.0

# Player ranging by highest pairs and lowest attempts
def sort_player_list(player_list):
	# sorted by highest pairs
	if len(player_list) > 1:
		for i in range(len(player_list)):
			for j in range(i + 1, len(player_list)):
				if player_list[j].get_pairs() > player_list[i].get_pairs():
					player_list[i], player_list[j] = player_list[j], player_list[i]
		
		# sorted by lowest attempts            
		for i in range(len(player_list)):
			for j in range(i + 1, len(player_list)):
				if (((player_list[j].get_pairs() == player_list[i].get_pairs()) and
				(player_list[j].get_trials() < player_list[i].get_trials()))):
					player_list[i], player_list[j] = player_list[j], player_list[i]
	return player_list
	

def get_name_of_player(player_id):
	while True:
		print('  Player {}'.format(player_id))
		user_name = input('  What is your name? (max 10 character):\n  > ')[:10]
		if (len(user_name) >= 3 and user_name.isalnum()):
			return user_name
		print(' You can use only letters and digits.\n (But min 3 of that.)\n Try it again')
		
		
def is_name_in_list(name, list_of_players):
	for player in list_of_players:
		if name.lower() == player.name.lower():
			print(' Sorry! your name is already taken!')
			return True
	return False
	

def get_number_of_players():
	while True:
		try:
			number_of_player = int(input('  How many players want to play? '))
		except ValueError:
			print(' Please enter ONLY numbers!')
			continue
		
		if 0 < number_of_player <= 4:
			return number_of_player
		else:
			print(' Please enter only numbers from 1 to 4')

			
def init_game():
	list_of_players = []
	for i in range(get_number_of_players()):
		clearscreen.clear()
		print()
		while True:
			name = get_name_of_player(i+1)
			if not is_name_in_list(name, list_of_players):
				list_of_players.append(Player(name))
				break
	return list_of_players
	

def new_game(option_list):
	print('\tWelcome to the Memory Game.')
	print()
	player_list = init_game()
	while True:
		clearscreen.clear()
		game = gamefield.Gamefield(option_list[0], option_list[1])
		for player in player_list:
			player.reset_points()
			
		# changed player until board is not empty
		i = 0
		length_of_playerlist = len(player_list)
		while not game.bord_is_empty():
		
			player_list[i].add_trials()
			game.print_board()
			choice_return = game.choose_field(player_list[i].name)
			
			print()
			if choice_return == 2:      # Mainmenu
				clearscreen.clear()
				return
				
			elif choice_return == 0:    # No error
				print(' hmm... maybe next time...')
				i = (i + 1) % length_of_playerlist
				print('\n  {}'.format(player_list[i].get_name()))
				
			elif choice_return == 1:    # right try
				player_list[i].add_pairs()
				print('  Right! Keep it up!')
				
				if not game.bord_is_empty():
					print()
					print('  {} It\'s your turn again'.format( player_list[i].get_name() ))
					
			input(' Press Enter to continue...')
	
		clearscreen.clear()
		player_list = sort_player_list(player_list) # sorted Player after numbers of pairs and Trials
		Player.print_statistics_head()  # print the first player in table
		for player in player_list:
			Player.print_statistics_body(player)      # print all other player
			
		if not input('\n  Play again?(Y/N) ').lower().startswith('y'):
			clearscreen.clear()         
			break
			
	
def options_menu(option_list):
	clearscreen.clear()
	length, height = option_list
	while True:
		print()
		print('\t ****************')
		print('\t * Options Menu *')
		print('\t ****************')
		print('\n')
		print('\tGamefield Settings')
		print()
		print('\t(L)ength: {}'.format(length))
		print('\t(H)eight: {}'.format(height))
		print()
		print('     (R)eturn    (S)ave settings')
		print()
		print('    Please choose the first letter')
		user_input = input('     (L or H etc.): ')
		
		clearscreen.clear()
		if not user_input:
			continue
		if user_input[0].lower() in ['l', 'h', 'r', 's']:
			user_input = user_input[0].lower()
			while True:
				try:
					if user_input == 'l':
						length = int(input('\n  Enter length (1-9): '))
					elif user_input == 'h':
						height = int(input('\n  Enter height (1-9): '))
				except ValueError:
					print('Please enter only Integer!')
				except Exception as e:
					print(e)
				else:
					clearscreen.clear()
					break

			# go back without saveing
			if user_input == 'r':
				return option_list
				
			elif user_input == 's':
				if 4 <= length*height <= 81 and 1 <= length <= 9 and 1 <= height <= 9:
					return [length, height]
				else:
					print('\n The valid range of (LENGTH x HEIGHT) must be between 4 and 81!')
					print(' And the valid range of LENGTH and HEIGHT must be between 1 and 9!')
					
					
def print_rules():
	pass
	

def exit_game():
	if input('\n  Are you sure you want quitting the game? (Y/N) ').lower().startswith('y'):
		exit("   -={ Thanks for Playing }=-")
		
	
COMMANDS = {
	'1': new_game,
	'2': options_menu,
	# '3': print_rules,
	'0': exit_game
	}

def main_menu():
	options = [4, 4]        #  Length, Height of Gamefield
	while True:
		clearscreen.clear()
		print()
		print('\t**********')
		print('\t* Memory *')
		print('\t**********')
		print('\n')
		print('\t1) New Game')
		print('\t2) Options')
		# print('\t3) Game Rules')
		print('\t0) Exit Game')
		print()
		user_input = input("   Please choose a number: ")

		clearscreen.clear()
		if not user_input:
			continue

		if user_input[0] in COMMANDS:
			user_input = user_input[0]
			print()
			if user_input == '1':
				COMMANDS[user_input](options)               # function call with param
			elif user_input == '2':
				options = COMMANDS[user_input](options)     # function call with param and return
			else:
				COMMANDS[user_input]()                      # only a function call
	
main_menu()
