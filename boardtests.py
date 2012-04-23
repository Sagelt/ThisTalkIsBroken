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
		self.verifyboard()
		self.board.play(0)
		self.verifyboard([[5,0]])
	
	def test_isgameover(self):
		"""Verify that isgameover returns the correct values"""
		moves = [0,1,0,1,0,1]
		
		for move in moves:
			self.board.play(move)
			self.assertEqual(self.board.isgameover(), False)
			
		self.board.play(0)
		self.assertEqual(self.board.isgameover(), True)
		
	def test_winner(self):
		"""Verify the winner is correct"""
		self.assertRaises(AttributeError, self.board.winner)
		moves = [0,1,0,1,0,1,0]
		
		for move in moves:
			self.board.play(move)
		
		self.assertEqual(self.board.winner(), self.board.blackpiece.encode("iso-8859-1"))
		
		self.setUp()
		
		moves = [0,1,0,1,0,1,2,1]
		
		for move in moves:
			self.board.play(move)
		
		self.assertEqual(self.board.winner(), self.board.whitepiece.encode("iso-8859-1"))
		
	def test_undo(self):
		"""Test undo"""
		self.assertRaises(Exception, self.board.undo)
		
		moves = [0,1,2,3,4,5,4,0,5,3,2]
		
		for move in moves:
			self.board.play(move)
			
		blackmoves = [[5,0], [5,2], [5,4], [4,4], [4,5], [4,2]]
		whitemoves = [[5,1], [5,3], [5,5], [4,0], [4,3]]
		self.verifyboard(blackmoves, whitemoves)
			
		for x in range(0,10):
			self.board.undo()
			if len(blackmoves) > len(whitemoves):
				blackmoves.pop()
			else:
				whitemoves.pop()
			self.verifyboard(blackmoves, whitemoves)
			
	
	def test_redo(self):
		"""Test redo"""
		self.assertRaises(Exception, self.board.redo)
		
		moves = [0,1,2,3,4,5,4,0,5,3,2]
		
		for move in moves:
			self.board.play(move)
			
		blackmoves = [[5,0], [5,2], [5,4], [4,4], [4,5], [4,2]]
		whitemoves = [[5,1], [5,3], [5,5], [4,0], [4,3]]
		undoneblackmoves = []
		undonewhitemoves = []
		self.verifyboard(blackmoves, whitemoves)
			
		for x in range(0,10):
			self.board.undo()
			if len(blackmoves) > len(whitemoves):
				undoneblackmoves.append(blackmoves.pop())
			else:
				undonewhitemoves.append(whitemoves.pop())
			self.verifyboard(blackmoves, whitemoves)
			
		for x in range(0,10):
			self.board.redo()
			if len(blackmoves) <= len(whitemoves):
				blackmoves.append(undoneblackmoves.pop())
			else:
				whitemoves.append(undonewhitemoves.pop())
			self.verifyboard(blackmoves, whitemoves)
			
		
	
	

if __name__ == '__main__':
    unittest.main()