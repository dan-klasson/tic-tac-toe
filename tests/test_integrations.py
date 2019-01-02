import unittest
from unittest.mock import patch
from controllers import GameController
import io

class TestIntegrations(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, stdout):
        try:
            GameController().run()
        except StopIteration:
            pass
        self.assertIn(expected_output, stdout.getvalue())

    @patch('builtins.input', side_effect=['2', '1', '4', '2', '5', '3'])
    def test_human__player1_win(self, input):
        self.assert_stdout('Player 1 won!')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=['2', '1', '4', '2', '5', '7', '6'])
    def test_human__player2_win(self, input):
        self.assert_stdout('Player 2 won!')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=['1', '5', '6', '7', '2', '9'])
    def test_computer__draw(self, input):
        self.assert_stdout('Game ended in draw')
        self.assertTrue(input.called)

    @patch('builtins.input', side_effect=['1', '1', '2', '4'])
    def test_computer__win(self, input):
        self.assert_stdout('Player 2 won!')
        self.assertTrue(input.called)
