import unittest
from unittest.mock import patch
from models import Game
import sys

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_available_positions(self):
        self.game.board = [None, 'X', 'O', None]
        self.assertEqual(self.game.available_positions, [0, 3])

        self.game.board = ['X', 'O', None, None]
        self.assertEqual(self.game.available_positions, [2, 3])

    def test_mark(self):
        game = self.game
        game.mark('O', 2)
        self.assertEqual(game.moves, [2])
        self.assertEqual(game.board.count('O'), 1)
        self.assertEqual(game.board.count('X'), 0)

        self.game.mark('X', 5)
        self.assertEqual(game.moves, [2, 5])
        self.assertEqual(game.board.count('O'), 1)
        self.assertEqual(game.board.count('X'), 1)

    def test_undo_move(self):
        game = self.game
        game.board = [None, 'O', None, 'X']
        game.moves = [1, 3]
        game.winner = 'O'

        game.undo_move
        self.assertIsNone(game.winner)
        self.assertEqual(game.moves, [1])
        self.assertEqual(game.board, [None, 'O', None, None])

        game.undo_move
        self.assertIsNone(game.winner)
        self.assertEqual(game.moves, [])
        self.assertEqual(game.board, [None, None, None, None])

