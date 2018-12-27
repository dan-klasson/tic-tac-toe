#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Game:

    winnable_positions = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]

    def __init__(self):
        self.board = [None for _ in range(9)]
        self.moves = []
        self.winner = None

    @property
    def board_positions(self):
        return [i + 1 if not x else x for i, x in enumerate(self.board)]

    @property
    def available_positions(self):
        return [i for i, v in enumerate(self.board) if not v]

    def mark(self, marker, pos):
        self.moves.append(pos)
        self.board[pos] = marker

    @property
    def undo_move(self):
        self.winner = None
        self.board[self.moves.pop()] = None

    def is_won(self):

        board = self.board

        if None not in self.board:
            self.winner = None
            return True

        for a, b, c in self.winnable_positions:
            if board[a] and board[a] == board[b] == board[c]:
                self.winner = board[a]
                return True

        return False
