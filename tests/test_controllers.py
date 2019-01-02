import unittest
from unittest.mock import patch
from models import Game
from controllers import *
import io

class TestGameControllerPlayAgain(unittest.TestCase):
    """ GameController.play_again """

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, stdout):
        game = GameController()
        try:
            game.play_again()
        except StopIteration:
            pass
        self.assertIn(expected_output, stdout.getvalue())

    @patch('builtins.input', side_effect=['Y'])
    def test_play_again__yes(self, input):
        self.assert_stdout('Tic Tac Toe')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=['n'])
    def test_play_again__no(self, input):
        self.assert_stdout('')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=['N'])
    def test_play_again__no_capital(self, input):
        self.assert_stdout('')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=[''])
    def test_play_again__default(self, input):
        self.assert_stdout('Tic Tac Toe')
        self.assertTrue(input.called)

class TestGameControllerPlay(unittest.TestCase):
    """ GameController.play """

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, player1, player2, expected_output, stdout):
        game = GameController()
        try:
            game.play(player1, player2)
        except StopIteration:
            pass
        self.assertIn(expected_output, stdout.getvalue())

    @patch('builtins.input', side_effect=[1, 4, 2, 5, 3])
    def test_play__human(self, input):
        player1 = HumanController(player=1)
        player2 = HumanController(player=2)
        self.assert_stdout(player1, player2, 'Player 1 won!')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=[5, 6, 7, 2, 9])
    def test_play__computer_draw(self, input):
        player1 = HumanController(player=1)
        player2 = ComputerController(player=2)
        self.assert_stdout(player1, player2, 'Game ended in draw')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=[1, 2, 4])
    def test_play__computer_win(self, input):
        player1 = HumanController(player=1)
        player2 = ComputerController(player=2)
        self.assert_stdout(player1, player2, 'Player 2 won!')
        self.assertTrue(input.called)

@patch('sys.stdout', new_callable=io.StringIO)
class TestGameControllerGameResults(unittest.TestCase):
    """ GameController.game_results """

    def setUp(self):
        self.game = Game()
        self.controller = GameController()
        self.player1 = HumanController(player=1)
        self.player2 = HumanController(player=2)

    def test_draw(self, stdout):
        self.controller.game_results(self.player1, self.player2)
        self.assertIn('Game ended in draw', stdout.getvalue())

    def test_win_player1(self, stdout):
        self.controller.game.winner = 'X'
        self.player1.marker = 'X'
        self.controller.game_results(self.player1, self.player2)
        self.assertIn('Player 1 won', stdout.getvalue())

    def test_win_player2(self, stdout):
        self.controller.game.winner = 'O'
        self.player2.marker = 'O'
        self.controller.game_results(self.player1, self.player2)
        self.assertIn('Player 2 won', stdout.getvalue())


class TestPlayerController(unittest.TestCase):
    """ PlayerController """

    def test_player1(self):
        controller = PlayerController(player=1)
        self.assertEqual(controller.player, 1)
        self.assertEqual(controller.marker, 'X')
        self.assertEqual(controller.opponent, 'O')

    def test_player2(self):
        controller = PlayerController(player=2)
        self.assertEqual(controller.player, 2)
        self.assertEqual(controller.marker, 'O')
        self.assertEqual(controller.opponent, 'X')

    def test_move(self):
        game = Game()
        controller = PlayerController(player=1)
        with self.assertRaises(NotImplementedError):
            controller.move(game)

