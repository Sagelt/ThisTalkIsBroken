# -*- coding: latin-1 -*-
from connectfour import ConnectFour, ConnectFourBoard
import unittest
from cStringIO import StringIO
import sys

class BoardTests(unittest.TestCase):
	"""Test the ConnectFourBoard class"""
	def setUp(self):
		"""Instantiate a ConnectFourBoard for testing"""
		self.board = ConnectFourBoard()
	
	def playmoves(self, moves):
		"""For each move in moves, play that move on the board."""
		for move in moves:
			self.board.play(move)
		
	
	def verifyboard(self, blacklocations=[], whitelocations=[]):
		"""Verify that the board reflects the expected plays.
		
		All verification is done through asserts, no return value.
		
		blacklocations and whitelocations are the (row,column) coordinates
		of each expected piece. Any location not listed in these collections
		is expected to be empty."""
		for location in blacklocations:
			self.assertEqual(self.board._board[location[0]][location[1]], ConnectFourBoard.blackpiece)
		for location in whitelocations:
			self.assertEqual(self.board._board[location[0]][location[1]], ConnectFourBoard.whitepiece)
		otherlocations = []
		for col in range(0,ConnectFourBoard._columns):
			for row in range(0,ConnectFourBoard._rows):
				if ([row, col] not in blacklocations) and ([row, col] not in whitelocations):
					otherlocations.append([row, col])
		
		for location in otherlocations:
			self.assertEqual(self.board._board[location[0]][location[1]], ConnectFourBoard.emptyspace)
		
	
			
	def test_one_move(self):
		"""Create a board and play one move"""
		self.board.play(0)
		self.verifyboard([[5,0]])
	



class GameTests(unittest.TestCase):
	def setUp(self):
		"""Switch stdout but DO NOT start the game yet"""
		self.output = self.switchstdout()
	
	def switchstdout(self):
		"""Redirect stdout to a string for verification"""
		self.old_stdout = sys.stdout
		sys.stdout = result = StringIO()
		return result
		
	def unswitchstdout(self):
		"""Return stdout to normal"""
		sys.stdout = self.old_stdout
	
	def test_startup(self):
		"""Test creating a game and quitting"""
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
	
	@staticmethod
	def playbackmoves(moves):
		"""Playback the listed moves, one at a time"""
		result = moves[GameTests.nextMove]
		GameTests.nextMove += 1
		if GameTests.nextMove >= len(moves):
			GameTests.nextMove = 0
			GameTests.repititions += 1
		return result
	
	
	
	win_and_repeat_moves = ['0','1','0','1','0','1','0','y']
	
	@staticmethod
	def win_and_repeat(x):
		"""Playback a series of moves where black wins, then repeat"""
		result = GameTests.playbackmoves(GameTests.win_and_repeat_moves)
		if GameTests.repititions >= sys.getrecursionlimit():
			result = 'q'
		return result
	
	
	def test_restart(self):
		self.game = ConnectFour(GameTests.win_and_repeat)
	

if __name__ == '__main__':
    unittest.main()