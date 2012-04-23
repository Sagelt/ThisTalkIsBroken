# -*- coding: latin-1 -*-
from connectfourboard import ConnectFourBoard

class ConnectFour:
	
	def __init__(self, input_func=raw_input, start=True):
		self._game = ConnectFourBoard()
		self._input_func = input_func
		self.breakloop = False
		print "Welcome to Connect Four"
		print "There are two colors: black and white. Each player plays one color."
		print "They take turns choosing a column, a piece of their color is dropped into the chosen column."
		print "If there are four pieces of the same color in a row (horizontal, vertical, or diagonal) the player of that color wins."
		print "Black goes first. Good luck!"
		if start:
			self.gameloop()
	
			
		
	def gameloop(self):
		while(not self.breakloop):
			print self._game
			if self._game.isgameover():
				if self._game.winner() == "Tie":
					print "Tie game!"
				else:
					print self._game.winner()+" wins!"
				self.reset()
			else:
				print "It's "+self._getplayer()+"'s move."
				self._docommand(self._input_func("What column would you like to drop in? [0–6] "))

	
	def reset(self):
		option = self._input_func("Would you like to play again? [Y/N] ")
		if (option == 'Y') or (option == 'y'):
			self._game = ConnectFourBoard()
			self.gameloop()
		elif (option == 'N') or (option == 'n'):
			self.breakloop = True
		else:
			print "That's not an option"
			self.reset()
			
	def _docommand(self, command):
		if command in ['0', '1', '2', '3', '4', '5', '6']:
			try:
				self._game.play(int(command))
			except ColumnFullException:
				print "No can do, hombre, that column's full. Try again."
			except GameOverException:
				print "We're not playing anymore, the game is over."
		elif command == 'q':
			self.breakloop = True
		elif command == 'u':
			self._game.undo()
		elif command == 'r':
			try:
				self._game.redo()
			except InvalidMoveException:
				print "You can't redo what you haven't undone (no moves to redo)"
	
	def _getplayer(self):
		if self._game._nextplayer == ConnectFourBoard.blackpiece:
			return "Black"
		else:
			return "White"
	



if __name__ == '__main__':
	g = ConnectFour()
	
	