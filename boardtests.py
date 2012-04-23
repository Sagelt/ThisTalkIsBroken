# -*- coding: latin-1 -*-
from connectfourboard import ConnectFourBoard
import unittest

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
	
	

if __name__ == '__main__':
    unittest.main()