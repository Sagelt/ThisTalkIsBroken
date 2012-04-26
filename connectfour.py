# -*- coding: latin-1 -*-
from connectfourboard import ConnectFourBoard

class ConnectFour:
	
	def __init__(self, input_func=raw_input, start=True):
		"""Create a new game of Connect Four.
		
		If start is True (default) then the game starts playing immediately.
		
		If input_func is specified input will be pulled from there instead of
		raw_input."""
		self._game = ConnectFourBoard()
		self._input_func = input_func
		self.breakloop = False
		if start:
			self.gameloop()
	
			
		
	def gameloop(self):
		"""Start the game and continue until the user quits."""
		print "Welcome to Connect Four"
		print "There are two colors: black and white. Each player plays one color."
		print "They take turns choosing a column, a piece of their color is dropped into the chosen column."
		print "If there are four pieces of the same color in a row (horizontal, vertical, or diagonal) the player of that color wins."
		print "Black goes first. Good luck!"
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
		"""Reset the game to the initial state"""
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
		else:
			try:
				limit = int(command)
				i = 0
				for p in self.eratosthenes():
					print p
					i += 1
					if i >= limit:
						break
			except:
				pass
	
	
	def eratosthenes(self):
		D = { }
		q = 2
		while 1:
			if q not in D:
				yield q
				D[q*q] = [q]
			else:
				for p in D[q]:
					D.setdefault(p+q, []).append(p)
				del D[q]
			q += 1
	
	
	def _getplayer(self):
		if self._game._nextplayer == ConnectFourBoard.blackpiece:
			return "Black"
		else:
			return "White"
	



if __name__ == '__main__':
	game = ConnectFour()
	
	