import chess
import numpy as np
from engine.encoding import board_to_tensor, NUM_PLANES


def test_shape():
    t = board_to_tensor(chess.Board())
    assert t.shape == (NUM_PLANES, 8, 8)
    assert t.dtype == np.float32


def test_start_position_piece_count():
    t = board_to_tensor(chess.Board())
    assert t[:12].sum() == 32


def test_white_king_location():
    t = board_to_tensor(chess.Board())
    assert t[5, 0, 4] == 1.0          # plane 5 = white king, rank 0, file e
    assert t[5].sum() == 1.0          # only one white king


def test_side_to_move_flips():
    board = chess.Board()
    assert board_to_tensor(board)[12].all()
    board.push_san("e4")
    assert not board_to_tensor(board)[12].any()


def test_en_passant_square():
    board = chess.Board()
    board.push_san("e4")
    t = board_to_tensor(board)
    assert t[17, 2, 4] == 1.0         # e3 = rank index 2, file index 4
    assert t[17].sum() == 1.0


def test_castling_rights_lost():
    board = chess.Board()
    board.push_san("e4"); board.push_san("e5")
    board.push_san("Ke2")
    t = board_to_tensor(board)
    assert not t[13].any() and not t[14].any()   # white lost both
    assert t[15].all() and t[16].all()           # black still has both
