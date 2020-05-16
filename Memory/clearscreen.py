from subprocess import call
from platform import system

'''
  clearscreen for the python console
  use clear()
'''
def clear():
	if system() == 'Windows':
		call(['cls'], shell = True)
	elif system() == 'Linux':
		call(['clear'], shell = True)