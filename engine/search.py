import chess
from engine.players import Player
from engine.evaluate import material_eval

MATE_SCORE = 100_000

def negamax(board: chess.Board, depth: int, alpha: int, beta: int, evaluate) -> int:
    if board.is_checkmate():
        return -MATE_SCORE - depth          # prefer faster mates
    if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_draw():
        return 0
    if depth == 0:
        return evaluate(board)

    best = -float("inf")
    for move in board.legal_moves:
        board.push(move)
        score = -negamax(board, depth - 1, -beta, -alpha, evaluate)
        board.pop()
        if score > best:
            best = score
        if best > alpha:
            alpha = best
        if alpha >= beta:
            break                            # opponent would never allow this line
    return best


class AlphaBetaPlayer(Player):
    def __init__(self, depth=3, evaluate=material_eval):
        self.depth = depth
        self.evaluate = evaluate

    def choose_move(self, board):
        best_move, best_score = None, -float("inf")
        for move in board.legal_moves:
            board.push(move)
            score = -negamax(board, self.depth - 1, -float("inf"), float("inf"), self.evaluate)
            board.pop()
            if score > best_score:
                best_move, best_score = move, score
        return best_move
