# -*- coding: latin-1 -*-
from connectfour import ConnectFour
import unittest
from cStringIO import StringIO
import sys

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
	
	quit_moves = ["q"]
	
	@staticmethod
	def quit(x):
		return GameTests.playbackmoves(GameTests.quit_moves)
	
	def test_startup(self):
		"""Test creating a game and quitting"""
		self.game = ConnectFour(GameTests.quit)
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
	
	win_and_repeat_moves = ['0','1','0','1','0','1','0','y']
	

if __name__ == '__main__':
    unittest.main()