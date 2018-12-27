#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GameView:

    @property
    def intro(self):
        return '\nTic Tac Toe\n'

    @property
    def number_of_players(self):
        return 'Enter number of players (1-2): '
    
    @property
    def number_of_players_error(self):
        return '\nPlease enter 1 or 2'

    def board(self, board):
        return '''
        ╔═══╦═══╦═══╗
        ║ {0} ║ {1} ║ {2} ║ 
        ╠═══╬═══╬═══╣
        ║ {3} ║ {4} ║ {5} ║ 
        ╠═══╬═══╬═══╣
        ║ {6} ║ {7} ║ {8} ║ 
        ╚═══╩═══╩═══╝
        '''.format(*board)

    def win_player(self, player):
        return 'Player {} won!'.format(player)

    @property
    def draw(self):
        return '\nGame ended in draw.'

    @property
    def play_again(self):
        return '\nPlay again? (Y/n): '

    def next_move(self, player, move=''):
        return 'Player {}: {}'.format(player, move)

    @property
    def move_not_valid(self):
        return 'Not a valid move'
