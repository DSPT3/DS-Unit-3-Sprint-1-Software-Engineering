"""
Classes to represent Games.
"""
from random import random

class Game:

    fun_level = 5

    def __init__(self, rounds=2,player1='Alice', player2='Bob'):
        self.rounds = rounds
        self.current_round = 0
        self.player1 = player1
        self.player2 = player2

    def add_round(self):
        self.rounds += 1

    def print_players(self):
        print("{} is playing {}".format(self.player1, self.player2))

    def winner(self):
        """Randomly pick and return the winner of the game."""
        return self.player1 if random() > 0.5 else self.player2

class TicTacToe(Game):
    """TicTacToe Game representations"""
    def __init__(self, rounds=3,player1="Will", player2="Mac"):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print('{} is playing Tic-Tac-Toe with {}'.format(self.player1, self.player2))
