# -*- coding: latin-1 -*-

class InvalidMoveException(Exception):
	def __init__(self, message=None):
		Exception.__init__(self, message)
	

class ColumnFullException(InvalidMoveException):
	def __init__(self, col):
		Exception.__init__(self, "Invalid move: column "+str(col)+" is full")
	

class GameOverException(InvalidMoveException):
	def __init__(self):
		Exception.__init__(self, "Invalid move: game is over")
	

class ConnectFourBoard:
	"""A game board for playing Connect Four"""
	
	blackpiece = u'●'
	whitepiece = u'○'
	emptyspace = ' '
	_columns = 7
	_rows = 6
	
	def __init__(self):
		"""Create a new empty Connect Four board with black to play next"""
		self._board = [[ConnectFourBoard.emptyspace for x in range(0,ConnectFourBoard._columns)] for y in range(0,ConnectFourBoard._rows)]
		self._isgameover = False
		self._winner = None
		self._nextplayer = ConnectFourBoard.blackpiece
		self._moves = []
		self._lastMove = -1
	
	def isgameover(self):
		"""Return true if game is over (board is full or someone won)"""
		return self._isgameover
	
	def winner(self):
		"""Return the winner if there is one or the empty string otherwise"""
		return self._winner.encode("iso-8859-1")
	
		
	def play(self, column):
		"""Play the next piece into the specified column"""
		if not isinstance(column, int):
			raise TypeError("Argument is not an int")
			
		
		if self.isgameover():
			raise GameOverException()
		
		row = ConnectFourBoard._rows-1
		try:
			while(self._board[row][column] != ConnectFourBoard.emptyspace):
				row -= 1
			
			self._board[row][column] = self._nextplayer
			self._recordmove(column)
			self._checkgameover(row, column)
			self._turnover()
		except IndexError:
			raise ColumnFullException(column)
	
	def undo(self):
		"""Undo the last move"""
		column = self._moves[self._lastMove]
		for row in range(0, ConnectFourBoard._rows):
			if(self._board[row][column] != ConnectFourBoard.emptyspace):
				self._board[row][column] = ConnectFourBoard.emptyspace
				self._turnover()
				break
		self._lastMove -= 1
	
	def redo(self):
		"""Redo the next move"""
		if self._lastMove < len(self._moves)-1:
			self.play(self._moves[self._lastMove+1])
		else:
			raise InvalidMoveException("No move to redo")
	
		
	def _recordmove(self, move):
		if self._lastMove == len(self._moves)-1:
			self._moves.append(move)
			self._lastMove += 1
		else:
			self._lastMove += 1
			self._moves[self._lastMove] = move
	
			
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
	
		

