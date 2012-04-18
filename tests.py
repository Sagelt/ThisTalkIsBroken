# -*- coding: latin-1 -*-
from connectfour import ConnectFour, ConnectFourBoard
import unittest
from cStringIO import StringIO
import sys

class BoardTests(unittest.TestCase):
	def setUp(self):
		self.board = ConnectFourBoard()
		
	def playmoves(self, moves):
		for move in moves:
			self.board.play(move)
			
	def switchstdout(self):
		self.old_stdout = sys.stdout
		sys.stdout = result = StringIO()
		return result
			
	def verifyboard(self, blacklocations=[], whitelocations=[]):
		for location in blacklocations:
			self.assertEqual(self.board._board[location[0]][location[1]], ConnectFourBoard.blackpiece)
		for location in whitelocations:
			self.assertEqual(self.board._board[location[0]][location[1]], ConnectFourBoard.whitepiece)
			
	def test_one_move(self):
		self.board.play(0)
		self.verifyboard([[5,0]])


class GameTests(unittest.TestCase):
	def setUp(self):
		self.output = self.switchstdout()
		
	def switchstdout(self):
		self.old_stdout = sys.stdout
		sys.stdout = result = StringIO()
		return result
		
	def test_startup(self):
		self.game = ConnectFour(lambda x: "q")
		result = self.output.getvalue()
		expectedresult = ("Welcome to Connect Four\n"
		"There are two colors: black and white. Each player plays one color.\n"
		"They take turns choosing a column, a piece of their color is dropped into the chosen column.\n"
		"If there are four pieces of the same color in a row (horizontal, vertical, or diagonal) the player of that color wins.\n"
		"Black goes first. Good luck!\n"
		"-----------------\n"
		"|               |\n"
		"|               |\n"
		"|               |\n"
		"|               |\n"
		"|               |\n"
		"|               |\n"
		"-----------------\n"
		"\n"
		"It's Black's move.\n")
		self.assertEqual(result, expectedresult)
	
	nextMove = 0
	repititions = 0
	win_and_repeat_moves = ['0','1','0','1','0','1','0','y']
	
	@staticmethod
	def win_and_repeat(x):
		result = GameTests.win_and_repeat_moves[GameTests.nextMove]
		GameTests.nextMove += 1
		if GameTests.nextMove >= len(GameTests.win_and_repeat_moves):
			GameTests.repititions += 1
			GameTests.nextMove = 0
		if GameTests.repititions >= sys.getrecursionlimit():
			result = 'q'
		return result
		
	
	def test_restart(self):
		self.game = ConnectFour(GameTests.win_and_repeat)

if __name__ == '__main__':
    unittest.main()