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

if __name__ == '__main__':
    unittest.main()