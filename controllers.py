#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Game
from views import GameView

class GameController:

    def __init__(self):
        self.game = Game()
        self.view = GameView()

    def run(self):

        print(self.view.intro())

        while(True):
            players = input(self.view.number_of_players())
            if players == "1":
                self.play(
                    HumanController(player=1), 
                    ComputerController(player=2)
                )
            elif players == "2":
                self.play(
                    HumanController(player=1), 
                    HumanController(player=2)
                )
            else:
                print(self.view.number_of_players_error())
                continue
            break

        self.play_again()

    def play_again(self):
        resp = input(self.view.play_again)
        if resp.lower() != 'n':
            self.game = Game()
            print(self.view.newlines())
            self.run()

    def play(self, player1, player2):

        self.display_board()

        for i in range(9):

            if i % 2 == 0:
                player1.move(self.game)
            else:
                player2.move(self.game)

                self.display_board()

            if self.game.is_won():
                return self.game_results(player1, player2)

    def game_results(self, player1, player2):

        if self.game.winner:
            if player1.marker == self.game.winner:
                print(self.view.win_player(player=1))
            elif player2.marker == self.game.winner:
                print(self.view.win_player(player=2))
        else:
            print(self.view.draw())

    def display_board(self):
        print(self.view.board(self.game.board))

class PlayerController:

    def __init__(self, player):
        self.player = player
        self.view = GameView()

        if player == 1:
            self.marker = 'X'
            self.opponent = 'O'
        else:
            self.marker = 'O'
            self.opponent = 'X'

    def move(self, game):
        raise NotImplementedError()

class HumanController(PlayerController):

    def move(self, game):

        while True:
            move = input(self.view.next_move(self.player))
            try:
                move = int(move) - 1
            except ValueError:
                move = -1
        
            if move not in game.available_positions:
                print(self.view.move_not_valid)
            else:
                break
    
        game.mark(self.marker, move)
         
class ComputerController(PlayerController):

    def move(self, game):
        move, _ = game.maximized(self.marker, self.opponent)
        game.mark(self.marker, move)
        print(self.view.next_move(self.player, move + 1))
