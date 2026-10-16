import chess

PIECE_VALUES = {
    chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330,
    chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 0,
}

# How much each piece type cares about being central (centipawns per step toward the centre).
CENTRE_WEIGHT = {chess.KNIGHT: 10, chess.BISHOP: 6, chess.QUEEN: 3, chess.ROOK: 2}


def _centrality(sq):
    """0 on the edge, 3 on the four centre squares."""
    return 3.5 - max(abs(chess.square_file(sq) - 3.5), abs(chess.square_rank(sq) - 3.5)) - 0.5


def material_eval(board: chess.Board) -> int:
    """Material + light positional terms, centipawns, from the side to move's perspective."""
    score = 0
    for sq, piece in board.piece_map().items():
        value = PIECE_VALUES[piece.piece_type]
        if piece.piece_type in CENTRE_WEIGHT:
            value += int(CENTRE_WEIGHT[piece.piece_type] * _centrality(sq))
        elif piece.piece_type == chess.PAWN:
            rank = chess.square_rank(sq)
            advance = rank - 1 if piece.color == chess.WHITE else 6 - rank   # 0 on start rank .. 5
            value += 6 * advance
        score += value if piece.color == chess.WHITE else -value

    # Mop-up: when clearly ahead, push the enemy king to the edge and approach it.
    if abs(score) >= 300:
        winner = chess.WHITE if score > 0 else chess.BLACK
        wk, lk = board.king(winner), board.king(not winner)
        edge_dist = max(abs(chess.square_file(lk) - 3.5), abs(chess.square_rank(lk) - 3.5))
        bonus = int(10 * edge_dist + 4 * (7 - chess.square_distance(wk, lk)))
        score += bonus if winner == chess.WHITE else -bonus

    return score if board.turn == chess.WHITE else -score
