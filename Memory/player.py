
class Player(object):
	def __init__(self, name):
		self.name = name
		self.number_of_trials = 0
		self.number_of_pairs = 0
	
	def get_name(self):
		return self.name
		
	def add_trials(self):
		self.number_of_trials += 1
		
	def add_pairs(self):
		self.number_of_pairs += 1
		
	def reset_points(self):
		self.number_of_trials = self.number_of_pairs = 0
		
	def print_statistics_head(self):
		# ----------------------------------------
		# |    Name    |   Trials   |    Pairs   |		length per field = 12 - 2 Spaces left and right
		# ----------------------------------------
		# |  Player1   |     99     |      7     |
		# ----------------------------------------
		
		print()
		print(' {}'.format('-'*40))
		print(' |', end = '')
		for value in ['Name', 'Trials', 'Pairs']:
			left_site = right_side = 6
			for i in range(1, len(value)+1):
				if i%2 == 1:
					left_site -= 1
				else:
					right_side -= 1
			print('{}{}{}|'.format(' '*left_site, value, ' '*right_side), end = '')
		print()
		print(' {}'.format('-'*40))		
		
	def print_statistics_body(self):
		# | Player 1   |     99     |      7     |
		# ----------------------------------------
		print(' |', end = '')
		for value in [self.name, self.number_of_trials, self.number_of_pairs]:
			left_site = right_side = 6
			for i in range(1, len(str(value)[:10])+1):
				if i%2==1:
					left_site -= 1
				else:
					right_side -= 1
			print('{}{}{}|'.format(' '*left_site, str(value)[:10], ' '*right_side), end = '')
		print()
		print(' {}'.format('-'*40))
