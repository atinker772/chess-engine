import random
import chess

class Player:
    def choose_move(self, board: chess.Board) -> chess.Move:
        raise NotImplementedError

class RandomPlayer(Player):
    def choose_move(self, board):
        return random.choice(list(board.legal_moves))
