from connectfour import ConnectFour, ConnectFourBoard
import unittest

class BoardTests(unittest.TestCase):
	def setUp(self):
		self.board = ConnectFourBoard()
		
	def playmoves(self, moves):
		for move in moves:
			self.board.play(move)
			
	def verifyboard(self, blacklocations=[], whitelocations=[]):
		for location in blacklocations:
			self.assertEqual(self.board._board[location[0]][location[1]], ConnectFourBoard.blackpiece)
		for location in whitelocations:
			self.assertEqual(self.board._board[location[0]][location[1]], ConnectFourBoard.whitepiece)
			
	def test_one_move(self):
		self.board.play(0)
		self.verifyboard([[5,0]])


if __name__ == '__main__':
    unittest.main()