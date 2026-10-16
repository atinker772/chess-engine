import random
import chess
from engine.players import Player
from engine.evaluate import material_eval

MATE_SCORE = 100_000

def order_moves(board, moves):
    moves = list(moves)
    random.shuffle(moves)                      # random tie-break among equals
    return sorted(moves, key=lambda m: board.is_capture(m), reverse=True)

def negamax(board, depth, alpha, beta, evaluate):
    if depth == 0:
        if board.is_check() and board.is_checkmate():   # is_check is cheap, gates the expensive call
            return -MATE_SCORE
        return evaluate(board)
    moves = list(board.legal_moves)
    if not moves:
        return -MATE_SCORE - depth if board.is_check() else 0
    best = -float("inf")
    for move in order_moves(board, moves):
        board.push(move)
        score = -negamax(board, depth - 1, -beta, -alpha, evaluate)
        board.pop()
        best = max(best, score)
        alpha = max(alpha, best)
        if alpha >= beta:
            break
    return best


class AlphaBetaPlayer(Player):
    def __init__(self, depth=3, evaluate=material_eval):
        self.depth = depth
        self.evaluate = evaluate

    def choose_move(self, board):
        best_move, best_score = None, -float("inf")
        for move in order_moves(board, board.legal_moves):
            board.push(move)
            if board.is_repetition(2):          # this position has occurred before -> heading for a draw
                score = 0
            else:
                score = -negamax(board, self.depth - 1, -float("inf"), float("inf"), self.evaluate)
            board.pop()
            if score > best_score:
                best_move, best_score = move, score
        return best_move
