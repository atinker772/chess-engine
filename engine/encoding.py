import numpy as np
import chess

PIECE_TO_PLANE = {
    (chess.PAWN, chess.WHITE): 0, (chess.KNIGHT, chess.WHITE): 1,
    (chess.BISHOP, chess.WHITE): 2, (chess.ROOK, chess.WHITE): 3,
    (chess.QUEEN, chess.WHITE): 4, (chess.KING, chess.WHITE): 5,
    (chess.PAWN, chess.BLACK): 6, (chess.KNIGHT, chess.BLACK): 7,
    (chess.BISHOP, chess.BLACK): 8, (chess.ROOK, chess.BLACK): 9,
    (chess.QUEEN, chess.BLACK): 10, (chess.KING, chess.BLACK): 11,
}
NUM_PLANES = 12 + 1 + 4 + 1  # pieces, side to move, castling, en passant

def board_to_tensor(board: chess.Board) -> np.ndarray:
    t = np.zeros((NUM_PLANES, 8, 8), dtype=np.float32)
    for square, piece in board.piece_map().items():
        plane = PIECE_TO_PLANE[(piece.piece_type, piece.color)]
        t[plane, chess.square_rank(square), chess.square_file(square)] = 1.0
    t[12, :, :] = 1.0 if board.turn == chess.WHITE else 0.0
    t[13, :, :] = board.has_kingside_castling_rights(chess.WHITE)
    t[14, :, :] = board.has_queenside_castling_rights(chess.WHITE)
    t[15, :, :] = board.has_kingside_castling_rights(chess.BLACK)
    t[16, :, :] = board.has_queenside_castling_rights(chess.BLACK)
    if board.ep_square is not None:
        t[17, chess.square_rank(board.ep_square), chess.square_file(board.ep_square)] = 1.0
    return t
