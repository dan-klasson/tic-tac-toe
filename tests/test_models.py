import unittest
from unittest.mock import patch
from models import Game
import sys

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_board_positions(self):
        self.game.board = [None, 'X', 'O', None]
        self.assertEqual(self.game.board_positions, [1, 'X', 'O', 4])

        self.game.board = ['X', 'O', None, None]
        self.assertEqual(self.game.board_positions, ['X', 'O', 3, 4])


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

    def test_is_won__false(self):
        self.game.board = ['X', 'X', None, 'X', None, None, None, None, None]
        self.assertFalse(self.game.is_won())

    def test_is_won__true(self):
        self.game.board = ['X', 'X', 'X', None, None, None, None, None, None]
        self.assertTrue(self.game.is_won())

    def test_is_won__full_board(self):
        self.game.board = ['X'] * 9
        self.assertTrue(self.game.is_won())

    def test_maximized(self):
        self.game.board = ['X', 'X', 'X', None, None, None, None, None, None]
        self.assertEqual(self.game.maximized('X', 'O'), (3, 1))

    def test_minimized(self):
        self.game.board = ['X', 'X', 'X', 'O', 'O', None, None, None, None]
        self.assertEqual(self.game.minimized('X', 'O'), (5, 1))

    def test_score(self):
        self.game.board = ['X', 'X', 'X', None, None, None, None, None, None]
        self.assertEqual(self.game.score(marker='X', opponent='O'), 1)

        self.game.board = ['O', 'O', 'O', None, None, None, None, None, None]
        self.assertEqual(self.game.score(marker='X', opponent='O'), -1)

        self.game.board = ['X', 'X', None, None, None, None, None, None, None]
        self.assertEqual(self.game.score(marker='X', opponent='O'), 0)
