# -*- coding: latin-1 -*-
from os import system

class InvalidMoveException(Exception):
	pass
	
class ColumnFullException(InvalidMoveException):
	def __init__(self, col):
		Exception.__init__(self, "Invalid move: column "+str(col)+" is full")
		
class GameOverException(InvalidMoveException):
	def __init__(self):
		Exception.__init__(self, "Invalid move: game is over")

class ConnectFourBoard:
	
	blackpiece = u'●'
	whitepiece = u'○'
	emptyspace = ' '
	_columns = 7
	_rows = 6
	
	def __init__(self):
		self._board = [[ConnectFourBoard.emptyspace for x in range(0,ConnectFourBoard._columns)] for y in range(0,ConnectFourBoard._rows)]
		self._isgameover = False
		self._winner = None
		self._nextplayer = ConnectFourBoard.blackpiece
		self._moves = []
		
	def isgameover(self):
		return self._isgameover
		
	def winner(self):
		return self._winner.encode("iso-8859-1")
		
	def play(self, column):
		if not isinstance(column, int):
			raise TypeError("Argument is not an int")
			
		
		if self.isgameover():
			raise GameOverException()
		
		row = ConnectFourBoard._rows-1
		try:
			while(self._board[row][column] != ConnectFourBoard.emptyspace):
				row -= 1
			
			self._board[row][column] = self._nextplayer
			self._moves.append(column)
			self._checkgameover(row, column)
			self._turnover()
		except IndexError:
			raise ColumnFullException(column)
	
	def undo(self):
		column = self._moves.pop()
		for row in range(0, ConnectFourBoard._rows):
			if(self._board[row][column] != ConnectFourBoard.emptyspace):
				self._board[row][column] = ConnectFourBoard.emptyspace
				self._turnover()
				break
			
	def _turnover(self):
		if(self._nextplayer == ConnectFourBoard.blackpiece):
			self._nextplayer = ConnectFourBoard.whitepiece
		else:
			self._nextplayer = ConnectFourBoard.blackpiece
			
	def _checkgameover(self, row, column):
		full = True
		for col in range(0,ConnectFourBoard._columns):
			if self._board[ConnectFourBoard._rows-1][col] == ConnectFourBoard.emptyspace:
				full = False
				
		
		if full:
			self._isgameover = True
			self._winner = "Tie"
		
		if self._checkrowfour(row, column):
			self._isgameover = True
			self._winner = self._nextplayer
			
		if self._checkcolumnfour(row, column):
			self._isgameover = True
			self._winner = self._nextplayer
			
		if self._checkupleftdiagfour(row, column):
			self._isgameover = True
			self._winner = self._nextplayer
			
		if self._checkuprightdiagfour(row, column):
			self._isgameover = True
			self._winner = self._nextplayer
			
		
	def _checkrowfour(self, row, column):
		count = 1
		for x in range(column+1, ConnectFourBoard._columns):
			if self._board[row][x] == self._nextplayer:
				count += 1
			else:
				break
		for x in range(column-1, -1, -1):
			if self._board[row][x] == self._nextplayer:
				count += 1
			else:
				break
		if count >= 4:
			return True
		else:
			return False
			
	def _checkcolumnfour(self, row, column):
		count = 1
		for y in range(row+1, ConnectFourBoard._rows):
			if self._board[y][column] == self._nextplayer:
				count += 1
			else:
				break
		for y in range(row-1, -1, -1):
			if self._board[y][column] == self._nextplayer:
				count += 1
			else:
				break
		if count >= 4:
			return True
		else:
			return False
			
	def _checkupleftdiagfour(self, row, column):
		count = 1
		for i in range(1,ConnectFourBoard._columns):
			try:
				if self._board[row+i][column+i] == self._nextplayer:
					count += 1
				else:
					break
			except:
				pass
		for i in range(1,ConnectFourBoard._columns):
			try:
				if self._board[row-i][column-i] == self._nextplayer:
					count += 1
				else:
					break
			except:
				pass
		if count >= 4:
			return True
		else:
			return False
			
	def _checkuprightdiagfour(self, row, column):
		count = 1
		for i in range(1,ConnectFourBoard._columns):
			try:
				if self._board[row+i][column-i] == self._nextplayer:
					count += 1
				else:
					break
			except:
				pass
		for i in range(1,ConnectFourBoard._columns):
			try:
				if self._board[row-i][column+i] == self._nextplayer:
					count += 1
				else:
					break
			except:
				pass
		if count >= 4:
			return True
		else:
			return False		
			
	def __str__(self):
		result = "-----------------\n"
		for row in range(0, ConnectFourBoard._rows):
			result += "| "
			for column in range(0,ConnectFourBoard._columns):
				result += self._board[row][column]
				result += " " 
			result += "|\n"
		result += "-----------------\n"
		return result.encode("iso-8859-1")
			

class ConnectFour:
	
	def __init__(self, input_func=raw_input):
		self._game = ConnectFourBoard()
		self._input_func = input_func
		self.breakloop = False
		print "Welcome to Connect Four"
		print "There are two colors: black and white. Each player plays one color."
		print "They take turns choosing a column, a piece of their color is dropped into the chosen column."
		print "If there are four pieces of the same color in a row (horizontal, vertical, or diagonal) the player of that color wins."
		print "Black goes first. Good luck!"
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
		elif command == 'q':
			self.breakloop = True
		elif command == 'u':
			self._game.undo()
		
	def _getplayer(self):
		if self._game._nextplayer == ConnectFourBoard.blackpiece:
			return "Black"
		else:
			return "White"

if __name__ == '__main__':
	g = ConnectFour()
	
	