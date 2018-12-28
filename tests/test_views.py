import unittest
from views import GameView

class TestGameView(unittest.TestCase):

    def setUp(self):
        self.view = GameView()

    def test_board(self):
        board = [1, 'O', 'O', 'X', 5, 'X', 7, 8, 9]
        self.assertEqual(self.view.board(board), '''
        ╔═══╦═══╦═══╗
        ║ 1 ║ O ║ O ║ 
        ╠═══╬═══╬═══╣
        ║ X ║ 5 ║ X ║ 
        ╠═══╬═══╬═══╣
        ║ 7 ║ 8 ║ 9 ║ 
        ╚═══╩═══╩═══╝
        ''')
    
    def test_new_lines(self):
        self.assertEqual(self.view.newlines(), '\n')
        self.assertEqual(self.view.newlines(3), '\n\n\n')

    def test_win_player(self):
        self.assertEqual(self.view.win_player(1), 'Player 1 won!')
        self.assertEqual(self.view.win_player(2), 'Player 2 won!')

    def test_next_move(self):
        self.assertEqual(self.view.next_move(1, 1), 'Player 1: 1')
        self.assertEqual(self.view.next_move(1, 5), 'Player 1: 5')
        self.assertEqual(self.view.next_move(2, 6), 'Player 2: 6')
